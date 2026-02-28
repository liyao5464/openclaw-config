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
HTML转换由发布脚本自动处理，无需手动转换。

## 踩坑记录
- ❌ 发错号（主号发成实验室）
- ❌ 封面提示词太复杂→超时，要简洁
- ❌ 忘删备用标题→发布失败
- ❌ 关键信息只存文件没发聊天→老里看不到
- ✅ 封面提示词用英文简洁描述，一次成功不超时
- ✅ 同选题写两版（冷静版+燃文版）让老里选，效率高
- ✅ 同素材拆两篇给不同账号：大号贴读者画像，小号偏技术/创业
- ❌ gen-image.sh生成的图片无扩展名，需手动mv加.png
- ❌ wechat-api.ts的--cover路径相对于cwd，不要写成articles/xxx（会变成articles/articles/xxx）
- ❌ md2html-pro.js有marked库bug，直接用wechat-api.ts自带的markdown转换即可
- ✅ wechat-api.ts可直接发布.md文件，自动转HTML+上传图片+发草稿，一条龙
- ✅ 配图提示词用中文描述，老里要求图片文字必须是中文
- ✅ 情绪类文章用故事性插图（6张），比信息图更受欢迎（2026-02-28）
- ✅ 排版发布用 Opus 模型效果好（2026-02-28）
- ✅ 发全文时直接发文件，不在聊天里展示文字（2026-02-28）
- ✅ 抓微信公众号文章：web_fetch只拿到标题，需用curl+python解析id="js_content"的div（2026-02-28）
- ✅ curl用iPhone UA请求微信文章，限制少（2026-02-28）
- ✅ bun可运行wechat-api.ts，npx tsx不行（top-level await报错）（2026-02-28）
- ✅ wechat-api.ts文件参数是位置参数，不是--file（2026-02-28）
- ❌ gen-image.sh提示词太长会超时SIGTERM，要精简（2026-02-28）
- ❌ 老里不喜欢AI生成的复杂科技风配图，喜欢简洁干净风格（2026-02-28）
- ✅ **配图风格确定**：手绘笔记/白板草图风格 —— 简单线条、柔和配色、不花哨、像人手随手画的（2026-02-28）
- ✅ 配图路径用相对路径（agent-handdrawn/01.png），不要用绝对路径（2026-02-28）
