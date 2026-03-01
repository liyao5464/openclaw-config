---
title: "Obsidian内容工厂搭建经验"
updated: 2026-03-01
---

# Obsidian + OpenClaw 内容工厂搭建经验

## L0 核心结论
OpenClaw 在云服务器上，Obsidian 在本地 Windows，需要 Git 做中转同步。

## L1 关键配置

### Vault 路径
- 服务器实体路径：`/root/Documents/laoli-content`
- workspace 软链接：`/root/.openclaw/workspace/laoli-content`
- GitHub repo：`https://github.com/liyao5464/laoli-obsidian-vault`

### 目录结构
```
01-灵感与素材库/
  1-日常灵感剪报/
  2-爆款素材片段/
02-选题池/待写选题库/
03-内容工厂/
  1-大纲挑选区/
  2-初稿打磨区/
  3-终稿确认区/
04-已发布归档/公众号已发布/
```

### 自动同步
- 服务器 → GitHub：cron 每10分钟，model=minimax/MiniMax-M2.5
- 本地 OB → GitHub：obsidian-git 插件，每5分钟 auto pull/push

## L2 踩坑记录
- ❌ Windows PowerShell 的 `curl` 是 Invoke-WebRequest 别名，不支持 `-L` 参数，要用 `Invoke-WebRequest -Uri ... -OutFile ...`
- ❌ cron job 必须用 minimax/MiniMax-M2.5，newcli 在 isolated session 会报 membership 验证失败
- ✅ obsidian-cli 需要先关闭 OB 安全模式才能在插件市场搜到
