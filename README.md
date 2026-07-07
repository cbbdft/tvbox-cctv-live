# 📺 CCTV 直播源 + 影视点播 · 多客户端支持

> 🔄 **每天自动更新** | ✅ **源可用性验证** | 🚀 **全球 CDN 加速** | 📱 **多客户端支持**

[![每日自动更新](https://github.com/cbbdft/tvbox-cctv-live/actions/workflows/daily-update.yml/badge.svg)](https://github.com/cbbdft/tvbox-cctv-live/actions/workflows/daily-update.yml)

---

## ⚡ 快速使用

### KO影视（主力）— JSON 配置（点播+直播一体）

```
https://cdn.jsdelivr.net/gh/cbbdft/tvbox-cctv-live@master/KO影视.json
```

> 包含15个点播源（电影/电视剧/综艺/动漫）+ CCTV直播 + 解析器，一个地址搞定。

### TVBox（备用）— M3U 直播

```
https://cdn.jsdelivr.net/gh/cbbdft/tvbox-cctv-live@master/CCTV直播源.m3u
```

---

## 📋 全部订阅地址

| 客户端 | 格式 | 订阅地址 |
|--------|------|---------|
| **KO影视** (takagen99/Box) | JSON | `https://cdn.jsdelivr.net/gh/cbbdft/tvbox-cctv-live@master/KO影视.json` |
| **TVBox** / Televizo / TiviMate / Kodi | M3U | `https://cdn.jsdelivr.net/gh/cbbdft/tvbox-cctv-live@master/CCTV直播源.m3u` |
| **KO影视** (仅直播) | TXT | `https://cdn.jsdelivr.net/gh/cbbdft/tvbox-cctv-live@master/KO影视.txt` |
| 简单播放器 | TXT | `https://cdn.jsdelivr.net/gh/cbbdft/tvbox-cctv-live@master/CCTV直播源.txt` |
| 开发者/自定义 | JSON | `https://cdn.jsdelivr.net/gh/cbbdft/tvbox-cctv-live@master/CCTV直播源.json` |

---

## 📱 配置方法

### KO影视（主力）
设置 → 配置地址 → 粘贴 `KO影视.json` 的地址 → 确认

> JSON配置包含点播源+直播源+解析器，一次导入全部可用。

### TVBox（备用）
设置 → 配置地址 → 粘贴 M3U 地址

### Televizo / TiviMate / IPTV Smarters
设置 → 播放列表 → 添加 → 粘贴 M3U 地址

---

## 🎬 KO影视 JSON 配置说明

KO影视（基于 takagen99/Box）使用 JSON 配置文件，结构如下：

| 模块 | 说明 | 数量 |
|------|------|------|
| **sites** (点播源) | 苹果CMS采集站，via csp_AppYsV2 | 15个 |
| **lives** (直播源) | CCTV全频道直播 | 2个( TXT + M3U ) |
| **parses** (解析器) | 视频解析接口 | 3个 |
| **flags** | VIP解析标识 | 9个平台 |
| **ijk** | 播放器解码配置 | 软解码+硬解码 |
| **ads** | 广告拦截 | 5个域名 |
| **rules** | 嗅探规则 | m3u8/mp4等 |

### 点播源列表

| 采集站 | API地址 |
|--------|---------|
| 黑木耳 | heimuer.tv |
| 暴风 | bfzyapi.com |
| 量子 | cj.lziapi.com |
| 索尼 | suoniapi.com |
| 闪电 | sdzyapi.com |
| 红牛 | hongniuzy2.com |
| 豪华 | hhzyapi.com |
| 极速 | jszyapi.com |
| 非凡 | cj.ffzyapi.com |
| 360资源 | 360zy.com |
| 飞速 | feisuzyapi.com |
| 卧龙 | wolongzyw.com |
| U酷 | ukuapi.com |
| 熊掌 | xzcjz.com |
| 樱花 | apiyhzy.com |

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

GitHub Actions 每天 4 次自动运行（06:00 / 12:00 / 18:00 / 23:00 北京时间），从 6 个上游源拉取、验证可用性、按速度排序，每个频道保留最快的 5 个源，失效的自动淘汰。源已通过本地网络验证，无需额外 DNS 配置。

---

## 📊 验证报告

每次自动更新后，可在 [验证报告.md](./验证报告.md) 查看各频道的源可用性详情。

---

## ⚠️ 免责声明

- 所有源来自公开网络，仅供学习研究使用
- 软件基于 takagen99/Box 开源库，只提供聚合展示功能
- 软件不参与任何制作、上传、储存、下载等内容
- 请遵守当地法律法规，于安装后24小时内删除
- 源的有效性取决于第三方服务器状态
