# 📺 CCTV 全频道直播源 · 多客户端支持

> 🔄 **每天自动更新** | ✅ **源可用性验证** | 🚀 **全球 CDN 加速** | 📱 **多格式支持**

[![每日自动更新](https://github.com/cbbdft/tvbox-cctv-live/actions/workflows/daily-update.yml/badge.svg)](https://github.com/cbbdft/tvbox-cctv-live/actions/workflows/daily-update.yml)

---

## ⚡ 快速使用

### 各客户端订阅地址

| 适用客户端 | 格式 | 订阅地址 |
|-----------|------|---------|
| **TVBox** / Televizo / IPTV Smarters / TiviMate / Kodi | M3U | `https://cdn.jsdelivr.net/gh/cbbdft/tvbox-cctv-live@master/CCTV直播源.m3u` |
| **KO影视** / 简单播放器 | TXT | `https://cdn.jsdelivr.net/gh/cbbdft/tvbox-cctv-live@master/CCTV直播源.txt` |
| **KO影视** (带分组) | TXT | `https://cdn.jsdelivr.net/gh/cbbdft/tvbox-cctv-live@master/KO影视.txt` |
| 自定义客户端 / 开发者 | JSON | `https://cdn.jsdelivr.net/gh/cbbdft/tvbox-cctv-live@master/CCTV直播源.json` |
| TVBox 接口配置 | JSON | `https://cdn.jsdelivr.net/gh/cbbdft/tvbox-cctv-live@master/tvbox.json` |

> 每个频道内置多个源，一个超时自动切下一个，无需手动配置备用。

---

## 📱 各客户端配置方法

### TVBox
设置 → 直播 → 添加订阅 → 粘贴 M3U 地址

### Televizo
设置 → 播放列表 → 添加 → 粘贴 M3U 地址

### KO影视
设置 → 直播源 → 导入 → 粘贴 TXT 地址

### IPTV Smarters Pro
Settings → Playlists → Add → 粘贴 M3U 地址

### TiviMate
设置 → 播放列表 → 添加 → 粘贴 M3U 地址

### Kodi (PVR IPTV Simple)
设置 → PVR → IPTV Simple Client → Remote Path → M3U URL

---

## 📡 覆盖频道

| 频道 | 说明 | 频道 | 说明 |
|------|------|------|------|
| CCTV-1 | 综合 | CCTV-10 | 科教 |
| CCTV-2 | 财经 | CCTV-11 | 戏曲 |
| CCTV-3 | 综艺 | CCTV-12 | 社会与法 |
| CCTV-4 | 中文国际 | CCTV-13 | 新闻 |
| ⚽ CCTV-5 | 体育 | CCTV-14 | 少儿 |
| ⚽ CCTV-5+ | 体育赛事 | CCTV-15 | 音乐 |
| CCTV-6 | 电影 | CCTV-16 | 奥林匹克 |
| CCTV-7 | 国防军事 | CCTV-17 | 农业农村 |
| CCTV-8 | 电视剧 | CCTV-4K | 超高清 |
| CCTV-9 | 纪录 | | |

---

## 🌐 自动更新

GitHub Actions 每天 4 次自动运行（06:00 / 12:00 / 18:00 / 23:00 北京时间），从多个上游源拉取、验证可用性（含TS分片下载测速）、按速度排序，每个频道保留最快的 5 个源，失效的自动淘汰。每次更新自动生成所有格式的播放列表。

---

## 📊 验证报告

每次自动更新后，可在 [验证报告.md](./验证报告.md) 查看各频道的源可用性详情。详细订阅地址见 [订阅地址.md](./订阅地址.md)。

---

## ⚠️ 免责声明

- 直播源来自公开网络，仅供学习研究使用
- 源的有效性取决于第三方服务器状态
- 请遵守当地法律法规
