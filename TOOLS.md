# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

Add whatever helps you do your job. This is your cheat sheet.

## Web Content Extraction

### Jina AI Reader
网页内容提取神器，自动过滤广告和导航，输出干净的文章内容。

**提取网页内容：**
```
https://r.jina.ai/https://任意网址
```

**搜索功能：**
```
https://s.jina.ai/?q=关键词
```

**优点：**
- 比传统爬虫更稳定
- 自动提取正文，过滤广告
- 输出格式干净，适合直接阅读或处理
