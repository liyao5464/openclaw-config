---
name: wechat-fetcher
description: 抓取微信公众号文章全文。输入 mp.weixin.qq.com 链接，返回标题、作者、正文。无需登录，无需 API Key。触发词：抓微信文章、读公众号、fetch 微信链接。
---

# 微信公众号文章抓取

无需登录，直接抓取公开微信文章全文。

## 原理

微信公众号文章正文存放在 `id="js_content"` 的 div 里。
用 iPhone UA 发请求，绕过部分限制，直接解析 HTML 提取正文。

## 使用方法

### 方式1：调用脚本（推荐）

```bash
python3 skills/wechat-fetcher/scripts/fetch_mp.py "https://mp.weixin.qq.com/s/xxx"
```

### 方式2：AI 直接调用（exec）

```python
exec(command="""
python3 /root/.openclaw/workspace/skills/wechat-fetcher/scripts/fetch_mp.py \
  "https://mp.weixin.qq.com/s/xxx"
""")
```

### 方式3：Jina AI Reader（备用）

```
web_fetch(url="https://r.jina.ai/https://mp.weixin.qq.com/s/xxx")
```
适合简单场景，但有时会超时。

## 输出格式

```
标题: xxx
作者: xxx
字数: 3000
==================================================
正文内容...
```

## 限制

| 情况 | 能否抓取 |
|------|---------|
| 公开文章 | ✅ |
| 需关注才能看 | ❌ |
| 付费内容 | ❌ |
| 已删除文章 | ❌ |

## 注意

- 文章内图片是微信 CDN，转载需重新上传
- 部分文章有防爬措施，失败时换 Jina 方式重试
