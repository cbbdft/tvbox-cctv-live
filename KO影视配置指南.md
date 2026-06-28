# 🎬 KO影视 + TVBox 完整配置指南

> 更新时间: 2026-06-28
> 主力: KO影视 | 备用: TVBox

---

## 📋 订阅地址总览

### 直播源（CCTV + 卫视）

| 格式 | 适用 | 订阅地址 |
|------|------|---------|
| M3U | TVBox/Televizo/TiviMate/Kodi | `https://cdn.jsdelivr.net/gh/cbbdft/tvbox-cctv-live@master/CCTV直播源.m3u` |
| TXT(卫视+点播) | KO影视 | `https://cdn.jsdelivr.net/gh/cbbdft/tvbox-cctv-live@master/KO影视完整配置.txt` |
| TXT(仅CCTV) | KO影视 | `https://cdn.jsdelivr.net/gh/cbbdft/tvbox-cctv-live@master/KO影视.txt` |

### 点播源（影视采集站 - 已验证可用）

| 采集站 | 影片数 | API地址 |
|--------|--------|---------|
| 暴风 | 147,120 | `https://bfzyapi.com/api.php/provide/vod` |
| 红牛 | 106,534 | `https://www.hongniuzy2.com/api.php/provide/vod` |
| 量子 | 141,383 | `https://cj.lziapi.com/api.php/provide/vod` |
| 360资源 | 65,532 | `https://360zy.com/api.php/provide/vod` |
| 非凡 | 97,082 | `http://cj.ffzyapi.com/api.php/provide/vod` |
| 闪电 | 119,597 | `http://sdzyapi.com/api.php/provide/vod` |
| 豪华 | 105,877 | `https://hhzyapi.com/api.php/provide/vod` |
| 极速 | 105,121 | `https://jszyapi.com/api.php/provide/vod` |
| 索尼 | 139,148 | `https://suoniapi.com/api.php/provide/vod` |
| U酷 | 54,612 | `https://api.ukuapi.com/api.php/provide/vod` |

### TVBox多仓接口（备用）

| 名称 | 地址 |
|------|------|
| 飞龙VIP源 | `https://gitee.com/tvkj/fl/raw/main/svip.json` |
| 运输车多仓 | `https://weixine.net/api.json` |
| 巧儿源 | `http://pandown.pro/tvbox/tvbox.json` |

---

## 📱 KO影视配置方法

### 方法1: 导入完整配置（推荐）

1. 复制订阅地址:
   ```
   https://cdn.jsdelivr.net/gh/cbbdft/tvbox-cctv-live@master/KO影视完整配置.txt
   ```
2. 打开KO影视 → 设置 → 直播源 → 导入(URL) → 粘贴 → 确认
3. 直播和点播源一次性导入完成

### 方法2: 分别导入

**直播:**
- 设置 → 直播源 → 导入 → 粘贴 `KO影视.txt` 的订阅地址

**点播:**
- 设置 → 点播源 → 添加 → 粘贴采集站API地址（一次添加一个）
- 推荐优先添加: 暴风 → 红牛 → 量子 → 索尼

### 方法3: 扫码导入
- 用手机浏览器打开订阅地址 → 生成二维码 → KO影视扫码导入

---

## 📺 TVBox配置方法（备用）

### 单仓配置
1. 设置 → 配置地址 → 粘贴:
   ```
   https://cdn.jsdelivr.net/gh/cbbdft/tvbox-cctv-live@master/CCTV直播源.m3u
   ```

### 多仓配置（含点播）
1. 设置 → 配置地址 → 粘贴飞龙VIP源:
   ```
   https://gitee.com/tvkj/fl/raw/main/svip.json
   ```

---

## 🔄 自动更新

- **直播源**: GitHub Actions 每天4次自动验证+更新（含TS测速）
- **点播源**: 采集站自行维护，通常长期稳定
- **多仓接口**: 社区维护，可能随时变更

---

## ⚠️ 免责声明

- 所有源来自公开网络，仅供学习研究使用
- 请遵守当地法律法规
- 源的有效性取决于第三方服务器
