# CCTV 全频道直播源 - 完整参考手册

> 更新日期: 2026-06-10
> 数据来源: GitHub best-fan/iptv-sources (每日自动更新)

---

## 一、TVBox 使用方法

### 方式1：直接导入 M3U 文件
将 `CCTV直播源.m3u` 文件放入 TVBox 的配置目录，在"直播"中导入。

### 方式2：订阅在线源（推荐）
在 TVBox 直播设置中添加以下订阅地址：

```
https://raw.githubusercontent.com/best-fan/iptv-sources/master/cn_cctv.m3u8
```

这个地址每天自动更新，无需手动维护！

---

## 二、自动更新源（推荐用于 TVBox）

| 格式 | 地址 | 说明 |
|------|------|------|
| M3U | `https://raw.githubusercontent.com/best-fan/iptv-sources/master/cn_cctv.m3u8` | 央视专用 |
| M3U | `https://raw.githubusercontent.com/best-fan/iptv-sources/master/cn_all.m3u8` | 央视+卫视+付费 |
| TXT | `https://raw.githubusercontent.com/best-fan/iptv-sources/master/cn_cctv.txt` | 央视TXT格式 |
| TXT | `https://raw.githubusercontent.com/best-fan/iptv-sources/master/cn_all.txt` | 全频道TXT格式 |

### 其他优质自动更新源

| 项目 | 地址 | 更新频率 |
|------|------|----------|
| zhi35/iptv | `https://github.com/zhi35/iptv` | 每天 |
| cs3306/IPTV-Sources | `https://github.com/cs3306/IPTV-Sources` | 每天 |
| mytv-android | `https://github.com/mytv-android/China-TV-Live-M3U8` | 每天 |

---

## 三、CCTV 全频道直播源详细列表

### CCTV-1 综合 (13个源)
```
http://69.30.245.50/live/cctv1.m3u8
http://74.91.26.218:82/live/cctv1hd.m3u8
http://39.165.39.49:85/tsfile/live/1001_1.m3u8?key=txiptv&playlive=1&authid=0
http://222.223.41.27:8888/hls/1/index.m3u8
http://116.128.243.121:9905/tsfile/live/0001_1.m3u8?key=txiptv&playlive=1&authid=0
http://60.10.139.113:8801/hls/1/index.m3u8
http://183.129.255.66:8480/hls/1/index.m3u8
http://120.202.94.181:9446/tsfile/live/0001_1.m3u8?key=txiptv
http://58.56.162.102:4466/newlive/live/hls/1/live.m3u8
http://192.151.150.154/live/cctv1hd.m3u8
http://207.56.13.146:81/cdnlive/cctv1.m3u8
http://38.75.136.137:98/gslb/dsdqbv/cctv1hd.m3u8?auth=test20251009
http://play.kankanlive.com/live/1698234869325962.m3u8
```

### CCTV-2 财经 (13个源)
```
http://112.123.243.37:50085/tsfile/live/0002_1.m3u8?key=txiptv&playlive=0&authid=0
http://39.165.39.49:85/tsfile/live/1002_1.m3u8?key=txiptv&playlive=1&authid=0
http://222.223.41.27:8888/hls/2/index.m3u8
http://221.226.51.220:50081/newlive/live/hls/2/live.m3u8
http://116.128.243.121:9905/tsfile/live/0002_1.m3u8?key=txiptv&playlive=1&authid=0
http://60.10.139.113:8801/hls/2/index.m3u8
http://107.150.60.122/live/cctv2hd.m3u8
http://63.141.230.178:82/gslb/zbdq5.m3u8?id=cctv2hd
http://183.129.255.66:8480/hls/2/index.m3u8
http://120.202.94.181:9446/tsfile/live/0002_1.m3u8?key=txiptv
http://74.91.26.218:82/live/cctv2hd.m3u8
http://207.56.13.146:81/cdnlive/cctv2.m3u8
https://epg.pw/stream/f86540c126a751cc707e3805911549bd077fb5a7f0f53a824212d75addea3747.m3u8
```

### CCTV-3 综艺 (15个源)
```
http://112.123.243.37:50085/tsfile/live/0003_1.m3u8?key=txiptv&playlive=0&authid=0
http://39.165.39.49:85/tsfile/live/1003_1.m3u8?key=txiptv&playlive=1&authid=0
http://222.223.41.27:8888/hls/3/index.m3u8
http://58.56.162.102:4466/newlive/live/hls/3/live.m3u8
http://116.128.243.121:9905/tsfile/live/0003_1.m3u8?key=txiptv&playlive=1&authid=0
http://120.202.94.181:9446/tsfile/live/0003_1.m3u8?key=txiptv
http://60.10.139.113:8801/hls/3/index.m3u8
http://118.193.115.2:9901/tsfile/live/0003_1.m3u8?key=txiptv
http://107.150.60.122/live/cctv3hd.m3u8
http://74.91.26.218:82/live/cctv3hd.m3u8
http://207.56.13.146:81/cdnlive/cctv3.m3u8
http://198.204.228.26/live/cctv3hd.m3u8
http://38.75.136.137:98/gslb/dsdqbv/cctv3hd.m3u8?auth=test20251009
http://63.141.230.178:82/gslb/zbdq5.m3u8?id=cctv3hd
```

### CCTV-4 中文国际 (15个源)
```
http://112.123.243.37:50085/tsfile/live/0004_1.m3u8?key=txiptv&playlive=0&authid=0
http://120.198.95.220:9901/tsfile/live/1018_1.m3u8?key=txiptv&playlive=1&down=1
http://39.165.39.49:85/tsfile/live/1004_1.m3u8?key=txiptv&playlive=1&authid=0
http://222.223.41.27:8888/hls/4/index.m3u8
http://58.56.162.102:4466/newlive/live/hls/4/live.m3u8
http://60.10.139.113:8801/hls/4/index.m3u8
http://74.91.26.218:82/live/cctv4hd.m3u8
http://63.141.230.178:82/gslb/zbdq5.m3u8?id=cctv4k
http://38.75.136.137:98/gslb/dsdqbv/cctv4hd.m3u8?auth=test20251009
http://63.141.230.178:82/gslb/zbdq5.m3u8?id=cctv4hd
http://38.75.136.137:98/gslb/dsdqpub/cctv4k.m3u8?auth=testpub
http://221.226.51.220:50081/newlive/live/hls/4/live.m3u8
http://113.25.252.226:9901/tsfile/live/1008_1.m3u8?key=txiptv&playlive=1&authid=0
```

### ⚽ CCTV-5 体育 (15个源) - 重点！
```
http://112.123.243.37:50085/tsfile/live/0005_1.m3u8?key=txiptv&playlive=0&authid=0
http://120.198.95.220:9901/tsfile/live/1019_1.m3u8?key=txiptv&playlive=1&down=1
http://39.165.39.49:85/tsfile/live/1005_1.m3u8?key=txiptv&playlive=1&authid=0
http://222.223.41.27:8888/hls/5/index.m3u8
http://69.30.245.50/live/cctv5.m3u8
http://fuxin.yunjifei.top:999/tsfile/live/0005_1.m3u8?key=txiptv
http://120.202.94.181:9446/tsfile/live/0005_1.m3u8?key=txiptv
http://60.10.139.113:8801/hls/5/index.m3u8
http://183.129.255.66:8480/hls/5/index.m3u8
http://218.15.183.23:9901/tsfile/live/23022_1.m3u8
http://38.75.136.137:98/gslb/dsdqbv/cctv5hd.m3u8?auth=test20251009
http://38.75.136.137:98/gslb/dsdqpub/cctv5hd.m3u8?auth=testpub
http://207.56.13.146:81/cdnlive/cctv5.m3u8
http://74.91.26.218:82/live/cctv5hd.m3u8
http://221.226.51.220:50081/newlive/live/hls/5/live.m3u8
```

### ⚽ CCTV-5+ 体育赛事 (9个源)
```
http://112.123.243.37:50085/tsfile/live/0006_1.m3u8?key=txiptv&playlive=0&authid=0
http://39.165.39.49:85/tsfile/live/1089_1.m3u8?key=txiptv&playlive=1&authid=0
http://116.128.243.121:9905/tsfile/live/0016_1.m3u8?key=txiptv&playlive=1&authid=0
http://60.10.139.113:8801/hls/15/index.m3u8
http://183.129.255.66:8480/hls/6/index.m3u8
http://118.193.115.2:9901/tsfile/live/0141_1.m3u8?key=txiptv
http://58.56.162.102:4466/newlive/live/hls/6/live.m3u8
http://74.91.26.218:82/live/cctv5p.m3u8
http://207.56.13.146:81/cdnlive/cctv5p.m3u8
```

### CCTV-6 电影 (10个源)
```
http://112.123.243.37:50085/tsfile/live/0007_1.m3u8?key=txiptv&playlive=0&authid=0
http://198.204.240.250:82/live/cctv6.m3u8
http://222.223.41.27:8888/hls/6/index.m3u8
http://60.10.139.113:8801/hls/6/index.m3u8
http://39.165.39.49:85/tsfile/live/1006_1.m3u8?key=txiptv&playlive=1&authid=0
http://183.129.255.66:8480/hls/7/index.m3u8
http://116.128.243.121:9905/tsfile/live/0006_1.m3u8?key=txiptv&playlive=1&authid=0
http://192.151.150.154/live/cctv6hd.m3u8
http://198.204.228.26/live/cctv6hd.m3u8
http://221.226.51.220:50081/newlive/live/hls/6/live.m3u8
```

### CCTV-7 国防军事 (13个源)
```
http://222.223.41.27:8888/hls/7/index.m3u8
http://39.165.39.49:85/tsfile/live/1007_1.m3u8?key=txiptv&playlive=1&authid=0
http://116.128.243.121:9905/tsfile/live/0007_1.m3u8?key=txiptv&playlive=1&authid=0
http://183.129.255.66:8480/hls/8/index.m3u8
http://120.202.94.181:9446/tsfile/live/0007_1.m3u8?key=txiptv
http://60.10.139.113:8801/hls/7/index.m3u8
http://74.91.26.218:82/live/cctv7hd.m3u8
http://207.56.13.146:81/cdnlive/cctv7.m3u8
http://192.151.150.154/live/cctv7hd.m3u8
http://38.75.136.137:98/gslb/dsdqpub/cctv7hd.m3u8?auth=testpub
http://38.75.136.137:98/gslb/dsdqbv/cctv7hd.m3u8?auth=test20251009
http://63.141.230.178:82/gslb/zbdq5.m3u8?id=cctv7hd
http://113.25.252.226:9901/tsfile/live/1011_1.m3u8?key=txiptv&playlive=1&authid=0
```

### CCTV-8 电视剧 (6个源)
```
http://112.123.243.37:50085/tsfile/live/0009_1.m3u8?key=txiptv&playlive=0&authid=0
http://60.10.139.113:8801/hls/8/index.m3u8
http://120.202.94.181:9446/tsfile/live/0008_1.m3u8?key=txiptv
http://74.91.26.218:82/live/cctv8hd.m3u8
http://38.75.136.137:98/gslb/dsdqpub/cctv8hd.m3u8?auth=testpub
http://198.204.228.26/live/cctv8hd.m3u8
```

### CCTV-9 纪录 (9个源)
```
http://112.123.243.37:50085/tsfile/live/0010_1.m3u8?key=txiptv&playlive=0&authid=0
http://222.223.41.27:8888/hls/9/index.m3u8
http://39.165.39.49:85/tsfile/live/1009_1.m3u8?key=txiptv&playlive=1&authid=0
http://60.10.139.113:8801/hls/9/index.m3u8
http://183.129.255.66:8480/hls/10/index.m3u8
http://58.56.162.102:4466/newlive/live/hls/10/live.m3u8
http://38.75.136.137:98/gslb/dsdqpub/cctv9hd.m3u8?auth=testpub
http://38.75.136.137:98/gslb/dsdqbv/cctv9hd.m3u8?auth=test20251009
```

### CCTV-10 科教 (10个源)
```
http://101.66.195.125:9901/tsfile/live/0010_1.m3u8?key=txiptv&playlive=0&authid=0
http://39.165.39.49:85/tsfile/live/1010_1.m3u8?key=txiptv&playlive=1&authid=0
http://183.129.255.66:8480/hls/11/index.m3u8
http://116.128.243.121:9905/tsfile/live/0010_1.m3u8?key=txiptv&playlive=1&authid=0
http://120.202.94.181:9446/tsfile/live/0010_1.m3u8?key=txiptv
http://58.56.162.102:4466/newlive/live/hls/11/live.m3u8
http://60.10.139.113:8801/hls/10/index.m3u8
http://59.39.89.130:60901/tsfile/live/0010_1.m3u8?key=txiptv&playlive=1&authid=0
http://74.91.26.218:82/live/cctv10hd.m3u8
http://38.75.136.137:98/gslb/dsdqbv/cctv10hd.m3u8?auth=test20251009
```

### CCTV-11 戏曲 (12个源)
```
http://112.123.243.37:50085/tsfile/live/0012_1.m3u8?key=txiptv&playlive=0&authid=0
http://39.165.39.49:85/tsfile/live/1011_1.m3u8?key=txiptv&playlive=1&authid=0
http://222.223.41.27:8888/hls/11/index.m3u8
http://58.56.162.102:4466/newlive/live/hls/12/live.m3u8
http://183.129.255.66:8480/hls/12/index.m3u8
http://60.10.139.113:8801/hls/96/index.m3u8
http://74.91.26.218:82/live/cctv11hd.m3u8
http://38.75.136.137:98/gslb/dsdqbv/cctv11hd.m3u8?auth=test20251009
http://38.75.136.137:98/gslb/dsdqpub/cctv11hd.m3u8?auth=testpub
http://cd-live-stream.news.cctvplus.com/live/smil:CHANNEL1.smil/chunklist_w744036192_b1000000.m3u8
http://101.66.199.175:9901/tsfile/live/0011_1.m3u8?key=txiptv&playlive=0&authid=0
http://101.66.195.125:9901/tsfile/live/0011_1.m3u8?key=txiptv&playlive=0&authid=0
```

### CCTV-12 社会与法 (12个源)
```
http://112.123.243.37:50085/tsfile/live/0013_1.m3u8?key=txiptv&playlive=0&authid=0
http://39.165.39.49:85/tsfile/live/1000_1.m3u8?key=txiptv&playlive=1&authid=0
http://222.223.41.27:8888/hls/12/index.m3u8
http://120.202.94.181:9446/tsfile/live/0012_1.m3u8?key=txiptv
http://60.10.139.113:8801/hls/11/index.m3u8
http://116.128.243.121:9905/tsfile/live/0012_1.m3u8?key=txiptv&playlive=1&authid=0
http://183.129.255.66:8480/hls/13/index.m3u8
http://74.91.26.218:82/live/cctv12hd.m3u8
http://38.75.136.137:98/gslb/dsdqpub/cctv12hd.m3u8?auth=testpub
http://38.75.136.137:98/gslb/dsdqbv/cctv12hd.m3u8?auth=test20251009
http://63.141.230.178:82/gslb/zbdq5.m3u8?id=cctv12hd
https://epg.pw/stream/aedb71e61961cd2a5a5b9a8a83b8ae489c9408e6b420593aecb92cc36de628fe.m3u8
```

### CCTV-13 新闻 (9个源)
```
http://222.223.41.27:8888/hls/13/index.m3u8
https://event.pull.hebtv.com/jishi/cp1.m3u8
http://39.165.39.49:85/tsfile/live/1084_1.m3u8?key=txiptv&playlive=1&authid=0
http://183.129.255.66:8480/hls/14/index.m3u8
http://60.10.139.113:8801/hls/12/index.m3u8
http://fuxin.yunjifei.top:999/tsfile/live/0013_1.m3u8?key=txiptv
http://38.75.136.137:98/gslb/dsdqbv/cctv13hd.m3u8?auth=test20251009
http://63.141.230.178:82/gslb/zbdq5.m3u8?id=cctv13hd
http://198.204.228.26/live/cctv13hd.m3u8
```

### CCTV-14 少儿 (11个源)
```
http://39.165.39.49:85/tsfile/live/1085_1.m3u8?key=txiptv&playlive=1&authid=0
http://222.223.41.27:8888/hls/14/index.m3u8
https://event.pull.hebtv.com/jishi/cp2.m3u8
http://116.128.243.121:9905/tsfile/live/0014_1.m3u8?key=txiptv&playlive=1&authid=0
http://183.129.255.66:8480/hls/15/index.m3u8
http://58.56.162.102:4466/newlive/live/hls/15/live.m3u8
http://74.91.26.218:82/live/cctv14hd.m3u8
http://38.75.136.137:98/gslb/dsdqbv/cctv14hd.m3u8?auth=test20251009
http://192.151.150.154/live/cctv14hd.m3u8
http://38.75.136.137:98/gslb/dsdqpub/cctv14hd.m3u8?auth=testpub
http://113.25.252.226:9901/tsfile/live/1018_1.m3u8?key=txiptv&playlive=1&authid=0
```

### CCTV-15 音乐 (12个源)
```
http://112.123.243.37:50085/tsfile/live/0016_1.m3u8?key=txiptv&playlive=0&authid=0
https://xykt-fix.github.io/play/a02e/index.m3u8
http://39.165.39.49:85/tsfile/live/1086_1.m3u8?key=txiptv&playlive=1&authid=0
http://222.223.41.27:8888/hls/15/index.m3u8
http://116.128.243.121:9905/tsfile/live/0015_1.m3u8?key=txiptv&playlive=1&authid=0
http://60.10.139.113:8801/hls/97/index.m3u8
http://120.202.94.181:9446/tsfile/live/0015_1.m3u8?key=txiptv
http://74.91.26.218:82/live/cctv15hd.m3u8
http://38.75.136.137:98/gslb/dsdqpub/cctv15hd.m3u8?auth=testpub
http://38.75.136.137:98/gslb/dsdqbv/cctv15hd.m3u8?auth=test20251009
http://101.66.195.125:9901/tsfile/live/0015_1.m3u8?key=txiptv&playlive=0&authid=0
http://101.66.199.175:9901/tsfile/live/0015_1.m3u8?key=txiptv&playlive=0&authid=0
```

### CCTV-16 奥林匹克 (4个源)
```
http://183.129.255.66:8480/hls/17/index.m3u8
http://107.150.60.122/live/cctv16hd.m3u8
http://74.91.26.218:82/live/cctv16hd.m3u8
http://38.75.136.137:98/gslb/dsdqbv/cctv16hd.m3u8?auth=test20251009
```

### CCTV-17 农业农村 (4个源)
```
http://74.91.26.218:82/live/cctv17hd.m3u8
http://39.165.39.49:85/tsfile/live/1088_1.m3u8?key=txiptv&playlive=1&authid=0
http://60.10.139.113:8801/hls/98/index.m3u8
http://183.129.255.66:8480/hls/18/index.m3u8
```

### CCTV-4K 超高清 (1个源)
```
http://198.204.240.250:82/live/cctv4k.m3u8
```

---

## 四、如何自己维护和更新

### 方法1：直接订阅自动更新源（零维护）
在 TVBox 中直接使用以下订阅地址，源会自动更新：
```
https://raw.githubusercontent.com/best-fan/iptv-sources/master/cn_cctv.m3u8
```

### 方法2：定期手动拉取最新源
```bash
# Windows PowerShell
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/best-fan/iptv-sources/master/cn_cctv.m3u8" -OutFile "CCTV最新.m3u8"
```

### 方法3：自己搭建自动更新（技术方案）
1. Fork 项目: `https://github.com/best-fan/iptv-sources`
2. 启用 GitHub Actions 自动更新
3. 使用自己的 Raw 链接作为 TVBox 订阅地址

### 方法4：多源冗余策略
同时订阅多个自动更新源，TVBox 会自动选择可用的：
```
# 源1
https://raw.githubusercontent.com/best-fan/iptv-sources/master/cn_cctv.m3u8
# 源2
https://raw.githubusercontent.com/zhi35/iptv/main/cn_cctv.m3u8
# 源3
https://raw.githubusercontent.com/cs3306/IPTV-Sources/main/data/output/iptv_collection.m3u
```

---

## 五、常见问题

**Q: 为什么有些源播放不了？**
A: 直播源依赖第三方服务器，可能因网络、地区限制、服务器维护等原因暂时失效。每个频道都提供了多个备用源，换一个试试。

**Q: CCTV-5 看球赛卡顿怎么办？**
A: 建议同时添加 CCTV-5 和 CCTV-5+，比赛通常两个频道都有转播。如果都卡，切换到其他备用源。

**Q: 需要 IPv6 吗？**
A: 部分源需要 IPv6 网络。如果你的网络不支持 IPv6，优先使用 `74.91.26.218` 和 `39.165.39.49` 开头的源（IPv4）。

**Q: 源失效了怎么更新？**
A: 直接重新下载最新的 M3U 文件，或者使用自动更新订阅地址。
