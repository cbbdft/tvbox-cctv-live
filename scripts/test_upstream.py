#!/usr/bin/env python3
"""快速测试上游源的频道数量"""
import urllib.request, urllib.error, ssl, re, sys, time

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

UPSTREAM_SOURCES = [
    "https://raw.githubusercontent.com/best-fan/iptv-sources/master/cn_cctv.m3u8",
    "https://raw.githubusercontent.com/best-fan/iptv-sources/master/cn_all.m3u8",
    "https://raw.githubusercontent.com/best-fan/iptv-sources/master/cn_province.m3u8",
    "https://raw.githubusercontent.com/cs3306/IPTV-Sources/main/data/output/iptv_collection.m3u",
    "https://raw.githubusercontent.com/fanmingming/live/main/tv/m3u/ipv6.m3u",
    "https://raw.githubusercontent.com/YanG-1989/m3u/main/Gather.m3u",
    "https://iptv-org.github.io/iptv/countries/cn.m3u",
    "https://raw.githubusercontent.com/zhi35/iptv/master/iptv.m3u",
    "https://raw.githubusercontent.com/zhi35/iptv/master/live-china.m3u",
    "https://git.neofung.org/neo/iptv/raw/branch/master/iptv.m3u",
    "https://raw.githubusercontent.com/YueChan/Live/main/IPTV.m3u",
    "https://raw.githubusercontent.com/best-fan/iptv-sources/master/cn_cctv_status.m3u8",
    "https://raw.githubusercontent.com/best-fan/iptv-sources/master/cn_all_status.m3u8",
]

def count_entries(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=15, context=ctx) as resp:
            content = resp.read().decode("utf-8", errors="ignore")
        entries = []
        lines = content.split("\n")
        for line in lines:
            line = line.strip()
            if line.startswith("#EXTINF:"):
                parts = line.split(",", 1)
                if len(parts) > 1:
                    name = parts[1].strip()
                    entries.append(name)
        # 去重
        unique = len(set(entries))
        return len(entries), unique, len(content)
    except Exception as e:
        return 0, 0, f"FAIL: {e}"

print(f"{'源名称':<60} {'总频道':>8} {'去重':>8} {'大小':>8}")
print("-"*90)
for url in UPSTREAM_SOURCES:
    name = url.split("/")[-1] if "/" in url else url
    name = name[:60]
    total, unique, size = count_entries(url)
    if isinstance(size, str):
        print(f"{name:<60} {'-':>8} {'-':>8} {size}")
    else:
        print(f"{name:<60} {total:>8} {unique:>8} {size//1024:>5}KB")
    time.sleep(0.3)