#!/usr/bin/env python3
"""
CCTV 直播源 M3U 清洗脚本
功能：
  1. 读取当前 M3U 文件
  2. 去重（同一频道内相同 URL 只保留一个）
  3. 统一 tvg-id 格式
  4. 重新编号 label（主源, 备1, 备2...）
  5. 每个频道最多保留 5 个源
  6. 写入新文件
"""

import re
import os
from datetime import datetime, timezone, timedelta

# 频道映射与顺序应与 validate_sources.py 中 CHANNEL_ALIASES / CHANNEL_ORDER 保持一致
# 如需修改频道列表，请同步更新两个文件

CHANNEL_MAP = {
    "CCTV-1 综合": "CCTV1",
    "CCTV-2 财经": "CCTV2",
    "CCTV-3 综艺": "CCTV3",
    "CCTV-4 中文国际": "CCTV4",
    "CCTV-5 体育": "CCTV5",
    "CCTV-5+ 体育赛事": "CCTV5PLUS",
    "CCTV-6 电影": "CCTV6",
    "CCTV-7 国防军事": "CCTV7",
    "CCTV-8 电视剧": "CCTV8",
    "CCTV-9 纪录": "CCTV9",
    "CCTV-10 科教": "CCTV10",
    "CCTV-11 戏曲": "CCTV11",
    "CCTV-12 社会与法": "CCTV12",
    "CCTV-13 新闻": "CCTV13",
    "CCTV-14 少儿": "CCTV14",
    "CCTV-15 音乐": "CCTV15",
    "CCTV-16 奥林匹克": "CCTV16",
    "CCTV-17 农业农村": "CCTV17",
    "CCTV-4K 超高清": "CCTV4K",
}

SPORTS_CHANNELS = {"CCTV-5 体育", "CCTV-5+ 体育赛事"}

# 频道顺序（与 validate_sources.py CHANNEL_ORDER 保持一致）
CHANNEL_ORDER = [
    "CCTV-1 综合", "CCTV-2 财经", "CCTV-3 综艺", "CCTV-4 中文国际",
    "CCTV-5 体育", "CCTV-5+ 体育赛事", "CCTV-6 电影", "CCTV-7 国防军事",
    "CCTV-8 电视剧", "CCTV-9 纪录", "CCTV-10 科教", "CCTV-11 戏曲",
    "CCTV-12 社会与法", "CCTV-13 新闻", "CCTV-14 少儿", "CCTV-15 音乐",
    "CCTV-16 奥林匹克", "CCTV-17 农业农村", "CCTV-4K 超高清",
]


def get_channel_logo(ch_name):
    code = CHANNEL_MAP.get(ch_name, "CCTV1")
    return f"https://epg.pw/channel/{code}.png"


def main():
    # 从脚本所在目录推导 M3U 文件路径（与 validate_sources.py 保持一致）
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(script_dir)
    m3u_path = os.path.join(project_dir, "CCTV直播源.m3u")

    # 读取文件
    if not os.path.exists(m3u_path):
        print(f"❌ 文件不存在: {m3u_path}")
        return

    with open(m3u_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # 解析频道和 URL
    channels = {}  # ch_name -> list of unique urls
    current_name = None

    for line in lines:
        line = line.strip()
        if not line:
            continue
        if line.startswith("#EXTINF:"):
            # 提取 tvg-name
            m = re.search(r'tvg-name="([^"]+)"', line)
            if m:
                current_name = m.group(1)
            else:
                current_name = None
        elif not line.startswith("#") and line.startswith("http") and current_name:
            if current_name not in channels:
                channels[current_name] = []
            if line not in channels[current_name]:
                channels[current_name].append(line)
            else:
                print(f"  🗑️  重复源已移除: {current_name} -> {line[:60]}...")
            current_name = None

    # 按频道顺序生成
    tz = timezone(timedelta(hours=8))
    now = datetime.now(tz)

    # 生成新 M3U
    output = [
        '#EXTM3U x-tvg-url="https://epg.pw/test_channel_page.html"',
        f"# CCTV 全频道直播源 - 自动验证优化版",
        f"# 更新时间: {now.strftime('%Y-%m-%d %H:%M:%S')} CST",
        f"# 验证超时: 5s | 每频道保留 Top5 最快源",
        f"# 仓库: https://github.com/cbbdft/tvbox-cctv-live",
        f"# 订阅地址: https://cdn.jsdelivr.net/gh/cbbdft/tvbox-cctv-live@master/CCTV直播源.m3u",
        f"# 每个频道多个源，TVBox 会自动切换",
        "",
    ]

    total_sources = 0
    for ch in CHANNEL_ORDER:
        if ch not in channels or not channels[ch]:
            print(f"  ⚠️  频道缺失: {ch}")
            continue

        urls = channels[ch][:5]  # 最多 5 个
        total_sources += len(urls)

        for i, url in enumerate(urls):
            label = ch
            if ch in SPORTS_CHANNELS:
                label += " ⚽"
            if i > 0:
                label += f"(备{i})"

            tvg_id = CHANNEL_MAP.get(ch, "CCTV1")
            logo = get_channel_logo(ch)

            output.append(
                f'#EXTINF:-1 tvg-id="{tvg_id}" tvg-name="{ch}" tvg-logo="{logo}" group-title="央视",{label}'
            )
            output.append(url)

        output.append("")

    # 写入文件
    with open(m3u_path, "w", encoding="utf-8") as f:
        f.write("\n".join(output))

    print(f"✅ 清洗完成!")
    valid_channels = [ch for ch in CHANNEL_ORDER if ch in channels and channels[ch]]
    print(f"   频道数: {len(valid_channels)}")
    print(f"   总源数: {total_sources}")
    print(f"   文件: {m3u_path}")


if __name__ == "__main__":
    main()
