"""
频道配置共享模块
所有频道相关配置集中于此，validate_sources.py 和 clean_m3u.py 统一 import
"""

# 频道名称 → 短标识（用于 Logo URL 和 tvg-id）
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
    "CCTV-11 戏曲": "CCTV11",
    "CCTV-12 社会与法": "CCTV12",
    "CCTV-13 新闻": "CCTV13",
    "CCTV-14 少儿": "CCTV14",
    "CCTV-15 音乐": "CCTV15",
    "CCTV-16 奥林匹克": "CCTV16",
    "CCTV-17 农业农村": "CCTV17",
    "CCTV-4K 超高清": "CCTV4K",
}

# 频道名称别名（上游源常见缩写 → 标准名称）
CHANNEL_ALIASES = {
    "CCTV1": "CCTV-1 综合",
    "CCTV2": "CCTV-2 财经",
    "CCTV3": "CCTV-3 综艺",
    "CCTV4": "CCTV-4 中文国际",
    "CCTV5+": "CCTV-5+ 体育赛事",
    "CCTV5PLUS": "CCTV-5+ 体育赛事",
    "CCTV5": "CCTV-5 体育",
    "CCTV6": "CCTV-6 电影",
    "CCTV7": "CCTV-7 国防军事",
    "CCTV8": "CCTV-8 电视剧",
    "CCTV9": "CCTV-9 纪录",
    "CCTV11": "CCTV-11 戏曲",
    "CCTV12": "CCTV-12 社会与法",
    "CCTV13": "CCTV-13 新闻",
    "CCTV14": "CCTV-14 少儿",
    "CCTV15": "CCTV-15 音乐",
    "CCTV16": "CCTV-16 奥林匹克",
    "CCTV17": "CCTV-17 农业农村",
    "CCTV4K": "CCTV-4K 超高清",
}

# 频道顺序（M3U 输出和报告按此顺序排列）
CHANNEL_ORDER = [
    "CCTV-1 综合", "CCTV-2 财经", "CCTV-3 综艺", "CCTV-4 中文国际",
    "CCTV-5 体育", "CCTV-5+ 体育赛事", "CCTV-6 电影", "CCTV-7 国防军事",
    "CCTV-8 电视剧", "CCTV-9 纪录", "CCTV-11 戏曲",
    "CCTV-12 社会与法", "CCTV-13 新闻", "CCTV-14 少儿", "CCTV-15 音乐",
    "CCTV-16 奥林匹克", "CCTV-17 农业农村", "CCTV-4K 超高清",
]

# 需要特殊标记的频道（体育类）
SPORTS_CHANNELS = {"CCTV-5 体育", "CCTV-5+ 体育赛事"}

# 被排除的频道（不收录）
IGNORED_CHANNELS = {"CCTV-10 科教"}


def get_channel_logo(ch_name):
    """获取频道 Logo URL"""
    code = CHANNEL_MAP.get(ch_name, "CCTV1")
    return f"https://epg.pw/channel/{code}.png"


def get_channel_code(num_int):
    """将 CCTV 频道数字映射为标准名称"""
    channel_map = {
        1: "CCTV-1 综合", 2: "CCTV-2 财经", 3: "CCTV-3 综艺",
        4: "CCTV-4 中文国际", 5: "CCTV-5 体育", 6: "CCTV-6 电影",
        7: "CCTV-7 国防军事", 8: "CCTV-8 电视剧", 9: "CCTV-9 纪录",
        11: "CCTV-11 戏曲", 12: "CCTV-12 社会与法",
        13: "CCTV-13 新闻", 14: "CCTV-14 少儿", 15: "CCTV-15 音乐",
        16: "CCTV-16 奥林匹克", 17: "CCTV-17 农业农村",
    }
    return channel_map.get(num_int, f"CCTV-{num_int}")