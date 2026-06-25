# 📺 CCTV 全频道直播源 · TVBox 专用

> 🔄 **每天自动更新** | ✅ **源可用性验证** | 🚀 **全球 CDN 加速**

[![每日自动更新](https://github.com/cbbdft/tvbox-cctv-live/actions/workflows/daily-update.yml/badge.svg)](https://github.com/cbbdft/tvbox-cctv-live/actions/workflows/daily-update.yml)

---

## ⚡ 快速使用

### TVBox 订阅地址（一个就够了）

```
https://cdn.jsdelivr.net/gh/cbbdft/tvbox-cctv-live@master/CCTV直播源.m3u
```

> 每个频道内置多个源，一个超时 TVBox 自动切下一个，无需手动配置备用。

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

- 直播源来自公开网络，仅供学习研究使用
- 源的有效性取决于第三方服务器状态
- 请遵守当地法律法规
