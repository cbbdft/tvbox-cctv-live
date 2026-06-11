# 📺 CCTV 全频道直播源 · TVBox 专用

> 🔄 **每天自动更新** | ✅ **源可用性验证** | 🚀 **全球 CDN 加速**

[![每日自动更新](https://github.com/cbbdft/tvbox-cctv-live/actions/workflows/daily-update.yml/badge.svg)](https://github.com/cbbdft/tvbox-cctv-live/actions/workflows/daily-update.yml)

---

## ⚡ 快速使用

### TVBox 订阅地址（推荐用 CDN 加速版）

| 优先级 | 类型 | 订阅地址 |
|--------|------|----------|
| ⭐ 推荐 | jsDelivr CDN | `https://cdn.jsdelivr.net/gh/cbbdft/tvbox-cctv-live@master/CCTV直播源.m3u` |
| 备选 | Statically CDN | `https://cdn.statically.io/gh/cbbdft/tvbox-cctv-live/master/CCTV直播源.m3u` |
| 兜底 | GitHub Raw | `https://raw.githubusercontent.com/cbbdft/tvbox-cctv-live/master/CCTV直播源.m3u` |

> 💡 **建议**：在 TVBox 中同时添加以上 3 个地址，系统会自动选择最快的。

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

## 🤖 自动化机制

```
┌─────────────────────────────────────────────────┐
│  GitHub Actions 每天 4 次自动运行                  │
│  (06:00 / 12:00 / 18:00 / 23:00 北京时间)         │
├─────────────────────────────────────────────────┤
│  1. 从 3 个上游源拉取最新直播源                      │
│  2. 并发验证每个源的可用性 (HTTP + 内容校验)          │
│  3. 按响应速度排序，每频道保留最快的 3 个源            │
│  4. 生成优化后的 M3U 文件 + 验证报告                  │
│  5. 自动提交到 GitHub                               │
│  6. jsDelivr CDN 自动同步 (全球 200+ 节点)           │
└─────────────────────────────────────────────────┘
```

---

## 📊 验证报告

每次自动更新后，可在 [验证报告.md](./验证报告.md) 查看各频道的源可用性详情。

---

## 🛠️ 手动运行

```bash
# 安装 Python 3.11+
pip install -r requirements.txt  # (空，仅用标准库)

# 运行验证
python scripts/validate_sources.py

# 自定义参数
python scripts/validate_sources.py --timeout 5 --workers 30 --top-n 3
```

---

## 🌐 CDN 加速说明

| CDN | 节点数 | 刷新延迟 | 适用场景 |
|-----|--------|----------|----------|
| jsDelivr | 全球 200+ | 24h 内 | 国内+海外，推荐首选 |
| Statically | 全球 100+ | 即时 | 海外用户 |
| GitHub Raw | 美国 | 即时 | 兜底备用 |

---

## ⚠️ 免责声明

- 直播源来自公开网络，仅供学习研究使用
- 源的有效性取决于第三方服务器状态
- 请遵守当地法律法规
