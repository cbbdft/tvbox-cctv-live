#!/usr/bin/env python3
"""
CCTV 直播源验证 & 更新脚本
功能:
  1. 从多个上游源拉取最新直播源
  2. 逐个验证源的可用性 (HTTP 连通性 + 响应速度)
  3. 按响应速度排序，每个频道保留最快的 5 个源
  4. 生成优化后的 M3U 文件
  5. 输出验证报告

用法:
  python scripts/validate_sources.py
  python scripts/validate_sources.py --timeout 5 --workers 20
"""

import argparse
import concurrent.futures
import os
import re
import sys
import time
import urllib.request
import urllib.error
import ssl
from datetime import datetime, timezone, timedelta

# 从共享模块导入频道配置
from scripts.channels import (
    CHANNEL_ALIASES, CHANNEL_ORDER, SPORTS_CHANNELS,
    get_channel_logo, get_channel_code as _num_to_channel,
)

# ─── 配置 ───────────────────────────────────────────────
UPSTREAM_SOURCES = [
    # ═══ 一级源：独立采集/每日更新 ═══
    # best-fan：央视专用源（每日更新，CCTV 最全）
    "https://raw.githubusercontent.com/best-fan/iptv-sources/master/cn_cctv.m3u8",
    # best-fan：全频道源（央视+卫视+付费 46+频道，每日更新）
    "https://raw.githubusercontent.com/best-fan/iptv-sources/master/cn_all.m3u8",
    # best-fan：卫视专用源（37个省级卫视，每日更新）
    "https://raw.githubusercontent.com/best-fan/iptv-sources/master/cn_province.m3u8",
    # cs3306：40+源聚合，自动分类/检测，每日更新（8128个频道）
    "https://raw.githubusercontent.com/cs3306/IPTV-Sources/main/data/output/iptv_collection.m3u",
    # fanmingming：经典 IPv6 源（长期稳定）
    "https://raw.githubusercontent.com/fanmingming/live/main/tv/m3u/ipv6.m3u",
    # YanG-1989：聚合源（长期维护）
    "https://raw.githubusercontent.com/YanG-1989/m3u/main/Gather.m3u",

    # ═══ 二级源：社区聚合（稳定性较好） ═══
    # iptv-org：全球最大IPTV聚合项目（88K+ Stars）
    "https://iptv-org.github.io/iptv/countries/cn.m3u",
    # zhi35/iptv：每日自动更新（Github Actions）
    "https://raw.githubusercontent.com/zhi35/iptv/master/iptv.m3u",
    # zhi35/iptv：中国频道专用
    "https://raw.githubusercontent.com/zhi35/iptv/master/live-china.m3u",
    # neofung：每日自动更新
    "https://git.neofung.org/neo/iptv/raw/branch/master/iptv.m3u",
    # YueChan/Live：社区源
    "https://raw.githubusercontent.com/YueChan/Live/main/IPTV.m3u",

    # ═══ 三级源：辅助补充 ═══
    # best-fan：央视源含分辨率/流畅度信息
    "https://raw.githubusercontent.com/best-fan/iptv-sources/master/cn_cctv_status.m3u8",
    # best-fan：全频道含分辨率/流畅度
    "https://raw.githubusercontent.com/best-fan/iptv-sources/master/cn_all_status.m3u8",
]

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUTPUT_M3U = os.path.join(OUTPUT_DIR, "CCTV直播源.m3u")
REPORT_FILE = os.path.join(OUTPUT_DIR, "验证报告.md")

# 频道名称标准化映射
CHANNEL_ALIASES = CHANNEL_ALIASES  # noqa: F811

CHANNEL_ORDER = CHANNEL_ORDER  # noqa: F811

# 需要特殊标记的频道（体育类）
SPORTS_CHANNELS = SPORTS_CHANNELS  # noqa: F811

# 时效性URL黑名单域名（这些URL带鉴权参数，短期可用但很快失效）
EPHEMERAL_DOMAINS = [
    "douyinliving.com",   # 抖音直播流（wsSecret/wsTime 参数时效性短）
    "live.douyin.com",    # 抖音直播
    "hls.douyin.com",     # 抖音 HLS
]

# 每个频道保留的最优源数量
TOP_N = 5

# ─── 工具函数 ────────────────────────────────────────────

# 全局复用 SSL 上下文（避免每次请求都创建新的）
_SSL_CONTEXT = None

def get_ssl_context():
    """获取全局 SSL 上下文（不验证证书，部分 IPTV 服务器证书有问题）"""
    global _SSL_CONTEXT
    if _SSL_CONTEXT is None:
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        _SSL_CONTEXT = ctx
    return _SSL_CONTEXT


def fetch_url(url, timeout=15):
    """获取远程 URL 内容"""
    try:
        req = urllib.request.Request(url, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        })
        ctx = get_ssl_context()
        with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
            return resp.read().decode("utf-8", errors="ignore")
    except Exception as e:
        print(f"  ⚠ 获取失败: {url[:80]}... → {e}")
        return None


def parse_m3u(content):
    """解析 M3U/M3U8 内容，提取频道名和 URL"""
    entries = []
    lines = content.split("\n")
    current_name = None

    for line in lines:
        line = line.strip()
        if line.startswith("#EXTINF:"):
            # 提取频道名
            match = re.search(r'tvg-name="([^"]*)"', line)
            if match:
                current_name = match.group(1)
            else:
                # 尝试从逗号后提取
                parts = line.split(",", 1)
                if len(parts) > 1:
                    current_name = parts[1].strip()
        elif line and not line.startswith("#") and current_name:
            # 只保留 HTTP/HTTPS 源，过滤 rtp://, rtsp://, udp:// 等组播协议
            # （TVBox 在普通网络环境下无法播放组播流，且无法通过 HTTP 验证）
            if line.startswith("http://") or line.startswith("https://"):
                entries.append((current_name, line))
            current_name = None

    return entries


def normalize_channel_name(name):
    """标准化频道名称"""
    name = name.strip()
    # 移除多余的标记
    name = re.sub(r'\s*[\(（].*?[\)）]\s*$', '', name)
    name = re.sub(r'\s*(备\d*|备用|HD|高清|超清|4K|标清|HEVC|H265|AVS2?|AVS3)\s*$', '', name, flags=re.IGNORECASE)

    # 尝试别名映射 (精确匹配，避免 CCTV1 误匹配 CCTV10)
    upper = name.upper().replace(" ", "").replace("-", "").replace("_", "")
    for alias, standard in CHANNEL_ALIASES.items():
        alias_clean = alias.upper().replace(" ", "").replace("-", "")
        # 必须精确匹配或后跟非数字字符（避免 CCTV1 匹配到 CCTV10）
        if upper == alias_clean:
            return standard
        # 检查是否为前缀匹配且后面不是数字
        if upper.startswith(alias_clean):
            remaining = upper[len(alias_clean):]
            if not remaining or not remaining[0].isdigit():
                return standard

    # 尝试直接匹配 CCTV 数字 (支持各种格式: CCTV10, CCTV-10, CCTV 10, cctv10)
    match = re.search(r'CCTV[-\s]*(\d+)\+?', name, re.IGNORECASE)
    if match:
        num = match.group(1)
        if match.group(0).endswith("+"):
            return f"CCTV-{num}+ 体育赛事"
        result = _num_to_channel(int(num))
        return result

    # 匹配中文名称: "CCTV4K 超高清", "CCTV5+ 体育赛事" 等
    for ch_name in CHANNEL_ORDER:
        if ch_name in name:
            return ch_name

    return name


def is_ephemeral_url(url):
    """判断是否为时效性URL（带鉴权参数，短期可用但很快失效）"""
    url_lower = url.lower()
    for domain in EPHEMERAL_DOMAINS:
        if domain in url_lower:
            return True
    return False


def is_unsupported_url(url):
    """
    判断是否为当前网络环境不支持的URL：
    - IPv6 组播地址（[2409:...] 等需要 IPv6 + 特定运营商，普通网络不可用）
    - 运营商专网地址（chinamobile OTT 等，非公网可达）
    """
    url_lower = url.lower()
    # IPv6 地址（以 [ 开头）
    if "://[" in url_lower:
        return True
    # 中国移动 OTT 专网（非公网可达）
    if "chinamobile.com" in url_lower and "otttv" in url_lower:
        return True
    return False


def correct_channel_by_url(channel_name, url):
    """
    根据 URL 特征纠正频道分配。
    上游源可能把 CCTV-5+ 的源标记为 CCTV-5，或把 CCTV-4K 的源标记为 CCTV-4。
    同时过滤时效性URL和错误分配。
    """
    url_lower = url.lower()

    # 先过滤时效性URL
    if is_ephemeral_url(url):
        return None  # 抖音流等带鉴权参数，几小时后失效，不保留

    # 过滤不可达URL（IPv6/运营商专网）
    if is_unsupported_url(url):
        return None

    # CCTV-5 体育 vs CCTV-5+ 体育赛事
    if channel_name == "CCTV-5 体育" and ("cctv5p" in url_lower or "cctv5plus" in url_lower):
        return "CCTV-5+ 体育赛事"
    if channel_name == "CCTV-5+ 体育赛事" and ("cctv5hd" in url_lower or "cctv5/" in url_lower):
        return "CCTV-5 体育"
    # CCTV-4 中文国际 vs CCTV-4K
    if channel_name == "CCTV-4 中文国际" and ("cctv4k" in url_lower):
        return "CCTV-4K 超高清"
    if channel_name == "CCTV-4K 超高清" and ("cctv4hd" in url_lower or "cctv4/" in url_lower):
        return "CCTV-4 中文国际"
    # CCTV-8 电视剧 vs CCTV-8K（8K频道不在目标频道列表中）
    if channel_name == "CCTV-8 电视剧" and ("cctv8k" in url_lower):
        return None
    # CCTV-5 的源 URL 指向 CCTV-15（hls/15 是 CCTV-15 的流）
    if channel_name == "CCTV-5 体育" and "hls/15" in url_lower:
        return None  # 错误分配到 CCTV-5 的 CCTV-15 源
    return channel_name


def is_cctv_channel(name):
    """判断是否为 CCTV 频道"""
    normalized = normalize_channel_name(name)
    return normalized is not None and normalized in CHANNEL_ORDER


def test_source(url, timeout=5, retries=1):
    """
    测试单个直播源是否可用，返回 (url, latency_ms, status, ts_speed_kbps)
    
    两阶段验证 + 重试机制：
    1. 拉取 M3U8 播放列表，验证是否为有效 M3U8 结构
    2. 如果是主播放列表（#EXT-X-STREAM-INF），选最高码率子流递归测速
    3. 如果是媒体分片列表，下载 TS 分片测速
    4. 网络抖动时自动重试1次
    
    ts_speed_kbps: TS 分片下载速度 (kbps)，无法测速时为 None
    """
    for attempt in range(retries + 1):
        result = _test_source_once(url, timeout)
        # 如果 OK 或是 TS_FAIL（硬错误），直接返回
        if result[2] == "OK" or result[2].startswith("TS_FAIL"):
            return result
        # 网络类错误且还有重试次数，等 1 秒重试
        if attempt < retries and result[2] in ("TIMEOUT", "CONN_RESET"):
            time.sleep(1)
            continue
        return result
    return result


def _resolve_url(base_m3u8, ts_path):
    """将 M3U8 中的相对路径解析为绝对 URL"""
    if ts_path.startswith("http://") or ts_path.startswith("https://"):
        return ts_path
    if ts_path.startswith("/"):
        # 绝对路径：从域名拼接
        from urllib.parse import urlparse
        parsed = urlparse(base_m3u8)
        return f"{parsed.scheme}://{parsed.netloc}{ts_path}"
    # 相对路径
    return base_m3u8.rsplit("/", 1)[0] + "/" + ts_path


def _test_source_once(url, timeout):
    """单次源测试（无重试），供 test_source 内部调用"""
    import re
    start = time.time()
    ctx = get_ssl_context()
    
    # ─── 阶段1: 验证 M3U8 播放列表 ───
    try:
        req = urllib.request.Request(url, headers={
            "User-Agent": "Mozilla/5.0",
            "Accept": "*/*",
        })
        with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
            data = resp.read(65536)
            m3u8_latency = int((time.time() - start) * 1000)
            content = data.decode("utf-8", errors="ignore")
            
            if "#EXTM3U" not in content and "#EXTINF" not in content and "#EXT-X-TARGETDURATION" not in content:
                return (url, m3u8_latency, "INVALID_CONTENT", None)
    except urllib.error.HTTPError as e:
        return (url, int((time.time() - start) * 1000), f"HTTP_{e.code}", None)
    except urllib.error.URLError as e:
        reason = str(e.reason).lower()
        if "timed out" in reason:
            return (url, 9999, "TIMEOUT", None)
        if "reset" in reason or "refused" in reason:
            return (url, 9999, "CONN_RESET", None)
        return (url, int((time.time() - start) * 1000), f"URL_ERROR({reason[:20]})", None)
    except Exception as e:
        return (url, int((time.time() - start) * 1000), f"ERROR: {str(e)[:30]}", None)
    
    # ─── 阶段2: TS 分片下载测速 ───
    # 主播放列表：选最高码率子流递归测速
    if "#EXT-X-STREAM-INF" in content:
        streams = re.findall(
            r'#EXT-X-STREAM-INF:.*?BANDWIDTH=(\d+).*?\n\s*(.+?)\s*(?:\n|$)',
            content, re.MULTILINE
        )
        if streams:
            best = max(streams, key=lambda x: int(x[0]))
            sub_url = _resolve_url(url, best[1].strip())
            bw = int(best[0])
            # 递归测子流，但只测一次不重试
            sub_result = _test_source_once(sub_url, timeout)
            # 继承子流的测速结果
            _, lat, status, speed = sub_result
            if status == "OK":
                return (url, lat, "OK", speed or bw // 1000)
        return (url, m3u8_latency, "OK", None)
    
    # 媒体分片列表，找第一个 TS 分片 URL
    lines = content.strip().split("\n")
    ts_url = None
    for line in lines:
        line = line.strip()
        if line and not line.startswith("#"):
            if line.startswith("http"):
                ts_url = line
                break
            elif line.endswith(".ts") or ".ts?" in line:
                ts_url = _resolve_url(url, line)
                break
    
    if not ts_url:
        return (url, m3u8_latency, "OK", None)
    
    # 下载 TS 分片测速（最多下载 8 秒 / 3MB）
    ts_start = time.time()
    try:
        ts_req = urllib.request.Request(ts_url, headers={
            "User-Agent": "Mozilla/5.0",
            "Accept": "*/*",
        })
        with urllib.request.urlopen(ts_req, timeout=8, context=ctx) as ts_resp:
            downloaded = 0
            max_read = 3 * 1024 * 1024
            while downloaded < max_read:
                chunk = ts_resp.read(65536)
                if not chunk:
                    break
                downloaded += len(chunk)
            ts_time = time.time() - ts_start
            
            if ts_time > 0 and downloaded > 0:
                speed_kbps = int((downloaded * 8) / ts_time / 1000)
                # 保留所有能下到TS分片的源（无论快慢），慢的当备用
                return (url, m3u8_latency, "OK", speed_kbps)
            else:
                return (url, m3u8_latency, "OK", None)
    except Exception as e:
        err_msg = str(e)[:30]
        return (url, m3u8_latency, f"TS_FAIL({err_msg})", None)


# ─── 主流程 ───────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="CCTV 直播源验证 & 优化")
    parser.add_argument("--timeout", type=int, default=5, help="单个源超时时间(秒)")
    parser.add_argument("--workers", type=int, default=20, help="并发验证线程数")
    parser.add_argument("--top-n", type=int, default=TOP_N, help="每个频道保留最优源数")
    args = parser.parse_args()

    tz = timezone(timedelta(hours=8))
    now = datetime.now(tz)
    print(f"🔄 CCTV 直播源验证开始 | {now.strftime('%Y-%m-%d %H:%M:%S')} CST")
    print(f"   超时: {args.timeout}s | 并发: {args.workers} | 保留: Top{args.top_n}")
    print()

    # ─── Step 1: 拉取上游源 ───
    print("📥 Step 1/4: 拉取上游直播源...")
    all_entries = []
    for src in UPSTREAM_SOURCES:
        print(f"   → {src}")
        content = fetch_url(src)
        if content:
            entries = parse_m3u(content)
            cctv_entries = [(n, u) for n, u in entries if is_cctv_channel(n)]
            print(f"     ✓ 获取 {len(entries)} 条，其中 CCTV {len(cctv_entries)} 条")
            all_entries.extend(cctv_entries)
        else:
            print(f"     ✗ 获取失败")

    # 去重
    seen = set()
    unique_entries = []
    for name, url in all_entries:
        if url not in seen:
            seen.add(url)
            unique_entries.append((name, url))

    print(f"\n   总计: {len(all_entries)} 条 → 去重后 {len(unique_entries)} 条\n")

    # ─── Step 1.5: 从现有 M3U 文件补充缺失频道的源 ───
    print("📥 Step 1.5/4: 从现有文件补充缺失频道...")
    if os.path.exists(OUTPUT_M3U):
        with open(OUTPUT_M3U, "r", encoding="utf-8") as f:
            existing_content = f.read()
        existing_entries = parse_m3u(existing_content)
        existing_cctv = [(n, u) for n, u in existing_entries if is_cctv_channel(n)]
        for name, url in existing_cctv:
            if url not in seen:
                seen.add(url)
                unique_entries.append((name, url))
        print(f"   补充后总计: {len(unique_entries)} 条")
    else:
        print(f"   现有文件不存在，跳过补充")

    # ─── Step 2: 按频道分组 ───
    print("📊 Step 2/4: 按频道分组...")
    channels = {}
    discarded = 0
    ephemeral_discarded = 0
    for name, url in unique_entries:
        normalized = normalize_channel_name(name)
        # 根据 URL 特征纠正频道分配（CCTV-5 vs CCTV-5+, CCTV-4 vs CCTV-4K 等）
        # 同时过滤时效性URL（抖音流等带鉴权参数）
        corrected = correct_channel_by_url(normalized, url)
        if corrected is None:
            if is_ephemeral_url(url):
                ephemeral_discarded += 1
            else:
                discarded += 1
            continue
        if corrected not in channels:
            channels[corrected] = []
        # 同一频道内去重URL
        if url not in channels[corrected]:
            channels[corrected].append(url)

    if discarded:
        print(f"   丢弃 {discarded} 条明显错误的源")
    if ephemeral_discarded:
        print(f"   丢弃 {ephemeral_discarded} 条时效性源（抖音流等，鉴权参数短期有效）")

    low_channels = []   # 0 个源的频道
    weak_channels = []  # 仅 1 个源的频道
    for ch in CHANNEL_ORDER:
        if ch in channels:
            count = len(channels[ch])
            if count == 0:
                print(f"   {ch}: ⚠ 无源!")
                low_channels.append(ch)
            elif count == 1:
                print(f"   {ch}: ⚡ 仅 1 个源（脆弱）")
                weak_channels.append(ch)
            else:
                print(f"   {ch}: {count} 个源")
        else:
            print(f"   {ch}: ⚠ 无源!")
            low_channels.append(ch)
            channels[ch] = []

    if low_channels:
        print(f"\n   🔴 无源: {len(low_channels)} 个频道 ({', '.join(low_channels)})")
    if weak_channels:
        print(f"   🟡 脆弱: {len(weak_channels)} 个频道仅 1 源 ({', '.join(weak_channels)})")

    # ─── Step 3: 并发验证 ───
    print(f"\n🔍 Step 3/4: 并发验证源可用性 (超时 {args.timeout}s)...")
    all_urls = []
    for ch in CHANNEL_ORDER:
        for url in channels.get(ch, []):
            all_urls.append((ch, url))

    results = {}  # channel -> [(url, latency, status, ts_speed_kbps)]
    for ch in CHANNEL_ORDER:
        results[ch] = []

    tested = 0
    total = len(all_urls)

    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as executor:
        future_map = {}
        for ch, url in all_urls:
            future = executor.submit(test_source, url, args.timeout)
            future_map[future] = (ch, url)

        for future in concurrent.futures.as_completed(future_map):
            ch, url = future_map[future]
            try:
                url_out, latency, status, ts_speed = future.result()
                results[ch].append((url_out, latency, status, ts_speed))
                tested += 1
                if status == "OK":
                    speed_str = f" {ts_speed}kbps" if ts_speed else ""
                    print(f"   [{tested:3d}/{total}] ✓ {ch}: {latency:4d}ms{speed_str} {url[:60]}...")
                # 慢速源不再单独标记（所有能下到TS的都保留）
                else:
                    print(f"   [{tested:3d}/{total}] ✗ {ch}: {latency:4d}ms [{status}] {url[:60]}...")
            except Exception as e:
                results[ch].append((url, 9999, f"EXCEPTION: {e}", None))
                tested += 1
                print(f"   [{tested:3d}/{total}] ✗ {ch}: ERROR {url[:60]}...")

    # ─── Step 4: 排序 & 生成 M3U ───
    print(f"\n📝 Step 4/4: 生成优化后的 M3U 文件...")

    m3u_lines = [
        '#EXTM3U x-tvg-url="https://epg.pw/test_channel_page.html"',
        f"# CCTV 全频道直播源 - 自动验证优化版",
        f"# 更新时间: {now.strftime('%Y-%m-%d %H:%M:%S')} CST",
        f"# 验证超时: {args.timeout}s | 每频道保留 Top{args.top_n} 最快源",
        f"# 仓库: https://github.com/cbbdft/tvbox-cctv-live",
        f"# 订阅地址: https://cdn.jsdelivr.net/gh/cbbdft/tvbox-cctv-live@master/CCTV直播源.m3u",
        f"# 每个频道多个源，TVBox 会自动切换",
        "",
    ]

    report_lines = [
        f"# CCTV 直播源验证报告",
        f"",
        f"> 更新时间: {now.strftime('%Y-%m-%d %H:%M:%S')} CST",
        f"> 验证超时: {args.timeout}s | 并发: {args.workers} | 保留: Top{args.top_n}",
        f"> 总计验证: {total} 个源",
        f"",
        f"| 频道 | 总源数 | 可用 | 最快延迟 | 状态 |",
        f"|------|--------|------|----------|------|",
    ]

    total_ok = 0
    total_all = 0

    for ch in CHANNEL_ORDER:
        ch_results = results.get(ch, [])
        # 筛选可用的源（OK 状态），排除 SLOW_TS 慢速源
        ok_sources = [(url, lat, ts_speed) for url, lat, status, ts_speed in ch_results if status == "OK"]
        
        # 排序策略：有 TS 测速的按速度降序排最前，无测速的按 M3U8 延迟升序排后面
        # 这样最快的 TS 下载源排在第一位，TVBox 会优先使用它
        ok_sources.sort(key=lambda x: (-(x[2] or 0), x[1]))
        
        # 取 Top N
        top_sources = ok_sources[:args.top_n]

        total_all += len(ch_results)
        total_ok += len(ok_sources)

        if top_sources:
            best_lat = top_sources[0][1]
            best_speed = top_sources[0][2]
            if best_speed:
                best_lat = f"{best_lat}ms/{best_speed}kbps"
            # 🟢 至少3个可用源 | 🟡 1-2个 | 🔴 0个
            status_icon = "🟢" if len(ok_sources) >= 3 else ("🟡" if len(ok_sources) >= 2 else "🔴")
        else:
            best_lat = "-"
            status_icon = "🔴"

        report_lines.append(
            f"| {ch} | {len(ch_results)} | {len(ok_sources)} | {best_lat} | {status_icon} |"
        )

        # 写入 M3U
        for i, (url, latency, ts_speed) in enumerate(top_sources):
            label = f"{ch}"
            if ch in SPORTS_CHANNELS:
                label += " ⚽"
            if i > 0:
                label += f"(备{i})"

            logo = get_channel_logo(ch)
            # 生成干净的 tvg-id（从 logo URL 提取）
            tvg_id = logo.split("/")[-1].replace(".png", "")
            m3u_lines.append(
                f'#EXTINF:-1 tvg-id="{tvg_id}" tvg-name="{ch}" tvg-logo="{logo}" group-title="央视",{label}'
            )
            m3u_lines.append(url)

        m3u_lines.append("")

    # 统计
    report_lines.extend([
        "",
        f"## 📊 统计汇总",
        f"",
        f"| 指标 | 数值 |",
        f"|------|------|",
        f"| 总源数 | {total_all} |",
        f"| 可用源 | {total_ok} |",
        f"| 可用率 | {total_ok/total_all*100:.1f}% |" if total_all > 0 else "| 可用率 | N/A |",
        f"| 频道数 | {len(CHANNEL_ORDER)} |",
        f"| 有可用源的频道 | {sum(1 for ch in CHANNEL_ORDER if len([s for s in results.get(ch, []) if s[2]=='OK']) > 0)} |",
        "",
        f"## 📺 订阅地址",
        f"",
        f"在 TVBox 直播设置中添加以下地址即可：",
        f"",
        f"```",
        f"https://cdn.jsdelivr.net/gh/cbbdft/tvbox-cctv-live@master/CCTV直播源.m3u",
        f"```",
        f"",
        f"> 每个频道内置多个源，TVBox 会自动切换（一个超时自动用下一个）",
        "",
        f"## ⚠ 注意事项",
        f"",
        f"- 直播源依赖第三方服务器，可能随时失效",
        f"- 本仓库每天自动更新验证（GitHub Actions）",
        f"- 建议在 TVBox 中同时配置多个备用源",
        f"- 部分源需要 IPv6 网络支持",
    ])

    # 写入文件
    m3u_content = "\n".join(m3u_lines)
    with open(OUTPUT_M3U, "w", encoding="utf-8") as f:
        f.write(m3u_content)

    # ─── 生成 live.txt（TVBox/KO影视 TXT 格式）───
    LIVE_TXT = os.path.join(OUTPUT_DIR, "live.txt")
    txt_lines = ["央视,#genre#"]
    for ch in CHANNEL_ORDER:
        ch_results = results.get(ch, [])
        ok_sources = [(url, lat, ts_speed) for url, lat, status, ts_speed in ch_results if status == "OK"]
        ok_sources.sort(key=lambda x: (-(x[2] or 0), x[1]))
        top_sources = ok_sources[:args.top_n]
        for i, (url, lat, ts_speed) in enumerate(top_sources):
            label = ch
            if i > 0:
                label += f"(备{i})"
            txt_lines.append(f"{label},{url}")
    with open(LIVE_TXT, "w", encoding="utf-8") as f:
        f.write("\n".join(txt_lines) + "\n")

    report_content = "\n".join(report_lines)
    with open(REPORT_FILE, "w", encoding="utf-8") as f:
        f.write(report_content)

    print(f"\n✅ 完成!")
    print(f"   M3U 文件: {OUTPUT_M3U}")
    print(f"   TXT 文件: {LIVE_TXT}")
    print(f"   验证报告: {REPORT_FILE}")
    print(f"   可用率: {total_ok}/{total_all} ({total_ok/total_all*100:.1f}%)" if total_all > 0 else "   可用率: N/A")


if __name__ == "__main__":
    main()
