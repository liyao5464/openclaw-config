---
title: "公众号发布经验"
date: 2026-02-14
category: lessons
priority: 🔴
status: active
last_verified: 2026-02-27
tags: [wechat, publishing, workflow]
---

# 公众号发布经验

## 发布流程
1. 确认发哪个号（主号/实验室）— 必问！
2. 读 style-agent.md + writing-guide.md
3. 要真实素材，不编造
4. 写情绪大纲，老里确认
5. 写初稿 → 配图 → 转HTML → 推草稿 → 老里确认发布

## 转HTML命令
```bash
node scripts/md2html-pro.js article.md wechat
```

## 踩坑记录
- ❌ 发错号（主号发成实验室）
- ❌ 封面提示词太复杂→超时，要简洁
- ❌ 忘删备用标题→发布失败
- ❌ 关键信息只存文件没发聊天→老里看不到
