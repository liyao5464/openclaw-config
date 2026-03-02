
## 2026-03-02 经验总结

### GitHub 推送踩坑
- openclaw.json 含 Discord/Telegram token，GitHub push protection 会拦截历史提交
- 解决方案：删除整个 env 块，而不是逐个脱敏
- gitconfig 有 `insteadOf` 重写规则时，需要临时移除才能正常 push

### openclaw.json 废弃字段
- `streaming` 字段已废弃（telegram accounts + discord）
- `commands.ownerDisplay` 已废弃
- 用 python3 json 解析删除，比 sed 更安全

### Obsidian + OpenClaw 同步
- 软链接跨机器不可用（本地路径不存在）
- 正确方案：在 sync.sh 里 cp 关键文件到 Obsidian vault
- 已同步文件：SOUL.md / MEMORY.md / AGENTS.md / USER.md / NOW.md

### clawhub 限流
- 批量安装会触发 rate limit，需要手动逐个安装
