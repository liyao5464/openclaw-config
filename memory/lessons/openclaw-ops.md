
## 2026-03-02 踩坑记录

### GitHub 推送
- push protection 拦截历史提交中的 secrets → 解决：删整个 env 块
- gitconfig insteadOf 重写规则会导致 push 失败 → 临时注释掉

### openclaw.json 废弃字段
- `streaming`（telegram accounts + discord 顶层）已废弃
- `commands.ownerDisplay` 已废弃
- 用 python3 json 解析删除比 sed 更安全

### Obsidian 同步
- 软链接跨机器不可用（本地路径不存在）
- 正确方案：sync.sh 里 cp 关键文件到 Obsidian vault

### clawhub
- 批量安装触发 rate limit，需逐个安装
- document-skills 是 Claude Code 命令，不是 OpenClaw 技能
