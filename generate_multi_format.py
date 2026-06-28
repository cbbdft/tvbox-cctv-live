#!/usr/bin/env python3
"""
根据 CCTV直播源.m3u 生成多种格式的播放列表，适配不同客户端
"""
import os
import re
import json
from datetime import datetime, timezone, timedelta

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
M3U_FILE = os.path.join(SCRIPT_DIR, "CCTV直播源.m3u")

JSDELIVR = "https://cdn.jsdelivr.net/gh/cbbdft/tvbox-cctv-live@master"

tz = timezone(timedelta(hours=8))
now = datetime.now(tz)


def parse_m3u(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    entries = []
    current_info = None
    for line in content.split("\n"):
        line = line.strip()
        if line.startswith("#EXTINF:"):
            tvg_id = re.search(r'tvg-id="([^"]*)"', line)
            tvg_name = re.search(r'tvg-name="([^"]*)"', line)
            tvg_logo = re.search(r'tvg-logo="([^"]*)"', line)
            group = re.search(r'group-title="([^"]*)"', line)
            label_match = line.split(",", 1)
            label = label_match[1].strip() if len(label_match) > 1 else ""
            current_info = {
                "tvg_id": tvg_id.group(1) if tvg_id else "",
                "tvg_name": tvg_name.group(1) if tvg_name else "",
                "tvg_logo": tvg_logo.group(1) if tvg_logo else "",
                "group": group.group(1) if group else "央视",
                "label": label,
            }
        elif line and not line.startswith("#") and current_info:
            current_info["url"] = line
            entries.append(current_info)
            current_info = None
    return entries


def gen_txt(entries, output_path):
    lines = [
        f"# CCTV 直播源 TXT格式",
        f"# 更新时间: {now.strftime('%Y-%m-%d %H:%M:%S')} CST",
        f"# 格式: 频道名,URL",
        "",
    ]
    seen = set()
    for e in entries:
        ch = e["tvg_name"]
        if ch not in seen:
            seen.add(ch)
            clean = re.sub(r'\s*\(备\d+\)\s*', '', e["label"]).strip()
            lines.append(f"{clean},{e['url']}")
    lines.append("")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    return len(seen)


def gen_ko_txt(entries, output_path):
    lines = [
        f"# CCTV 直播源 - KO影视专用",
        f"# 更新时间: {now.strftime('%Y-%m-%d %H:%M:%S')} CST",
        "",
        "央视,#genre#",
    ]
    seen = set()
    for e in entries:
        ch = e["tvg_name"]
        if ch not in seen:
            seen.add(ch)
            clean = re.sub(r'\s*\(备\d+\)\s*', '', e["label"]).strip()
            lines.append(f"{clean},{e['url']}")
    lines.append("")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    return len(seen)


def gen_json(entries, output_path):
    channels = {}
    for e in entries:
        ch = e["tvg_name"]
        if ch not in channels:
            channels[ch] = {
                "name": ch,
                "tvg_id": e["tvg_id"],
                "logo": e["tvg_logo"],
                "group": e["group"],
                "urls": []
            }
        channels[ch]["urls"].append({"label": e["label"], "url": e["url"]})
    data = {
        "name": "CCTV 全频道直播源",
        "update_time": now.strftime("%Y-%m-%d %H:%M:%S CST"),
        "channel_count": len(channels),
        "source_count": len(entries),
        "channels": list(channels.values())
    }
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    return len(channels)


def gen_tvbox_json(entries, output_path):
    sites = []
    for e in entries:
        clean = re.sub(r'\s*\(备\d+\)\s*', '', e["label"]).strip()
        sites.append({
            "name": clean,
            "url": e["url"],
            "tvg_id": e["tvg_id"],
            "tvg_logo": e["tvg_logo"],
        })
    data = {
        "sites": sites,
        "lives": [{
            "name": "CCTV直播",
            "type": "0",
            "url": JSDELIVR + "/CCTV直播源.m3u",
            "epg": "https://epg.pw/test_channel_page.html",
            "logo": "https://epg.pw/channel/{tvg_id}.png"
        }]
    }
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    return len(sites)


def main():
    print(f"=== 生成多格式播放列表 ===")
    print(f"时间: {now.strftime('%Y-%m-%d %H:%M:%S')} CST\n")

    if not os.path.exists(M3U_FILE):
        print(f"找不到: {M3U_FILE}")
        return

    entries = parse_m3u(M3U_FILE)
    channels = set(e["tvg_name"] for e in entries)
    print(f"源文件: {len(entries)} 条, {len(channels)} 频道\n")

    outputs = []

    # 1. M3U (已有)
    outputs.append(("M3U (通用)", "TVBox/Televizo/IPTV Smarters/TiviMate/Kodi", JSDELIVR + "/CCTV直播源.m3u"))

    # 2. TXT
    txt_path = os.path.join(SCRIPT_DIR, "CCTV直播源.txt")
    n = gen_txt(entries, txt_path)
    print(f"TXT: {n}频道")
    outputs.append(("TXT", "KO影视/简单播放器", JSDELIVR + "/CCTV直播源.txt"))

    # 3. KO影视
    ko_path = os.path.join(SCRIPT_DIR, "KO影视.txt")
    n = gen_ko_txt(entries, ko_path)
    print(f"KO影视: {n}频道")
    outputs.append(("KO影视专用", "KO影视", JSDELIVR + "/KO影视.txt"))

    # 4. JSON
    json_path = os.path.join(SCRIPT_DIR, "CCTV直播源.json")
    n = gen_json(entries, json_path)
    print(f"JSON: {n}频道")
    outputs.append(("JSON", "自定义客户端/开发者", JSDELIVR + "/CCTV直播源.json"))

    # 5. TVBox JSON
    tvbox_path = os.path.join(SCRIPT_DIR, "tvbox.json")
    n = gen_tvbox_json(entries, tvbox_path)
    print(f"TVBox JSON: {n}条目")
    outputs.append(("TVBox JSON", "TVBox接口配置", JSDELIVR + "/tvbox.json"))

    # 6. 订阅说明
    readme_path = os.path.join(SCRIPT_DIR, "订阅地址.md")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write("# CCTV 直播源 - 多格式订阅地址\n\n")
        f.write(f"> 更新时间: {now.strftime('%Y-%m-%d %H:%M:%S')} CST\n")
        f.write("> 每天4次自动更新\n\n")
        f.write("## 各客户端订阅地址\n\n")
        f.write("| 格式 | 适用客户端 | 订阅地址 |\n")
        f.write("|------|-----------|---------|\n")
        for fmt, client, url in outputs:
            f.write(f"| {fmt} | {client} | `{url}` |\n")
        f.write("\n## 配置方法\n\n")
        f.write("### TVBox\n设置 → 直播 → 添加订阅 → 粘贴M3U地址\n\n")
        f.write("### Televizo\n设置 → 播放列表 → 添加 → 粘贴M3U地址\n\n")
        f.write("### KO影视\n设置 → 直播源 → 导入 → 粘贴TXT地址\n\n")
        f.write("### IPTV Smarters Pro\nSettings → Playlists → Add → 粘贴M3U地址\n\n")
        f.write("### TiviMate\n设置 → 播放列表 → 添加 → 粘贴M3U地址\n\n")
        f.write("### Kodi (PVR IPTV Simple)\n设置 → PVR → IPTV Simple Client → Remote Path → M3U URL\n")
    outputs.append(("订阅说明", "所有客户端配置说明", JSDELIVR + "/订阅地址.md"))

    print(f"\n=== 完成！订阅地址汇总 ===\n")
    for fmt, client, url in outputs:
        print(f"  {client}:")
        print(f"    {url}\n")


if __name__ == "__main__":
    main()
