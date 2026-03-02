# OpenClaw 配置备份

> 脱敏后的配置备份，敏感信息已移除。

## 包含

- `openclaw.json` — 模型配置、agents 列表（不含 API Key）
- `config.json` — 基本设置（已脱敏）
- `.env` — 环境变量模板（需手动填写）

## 不含

- API Keys / Bot Tokens（安全考虑）
- 会话历史
- 认证文件
- 记忆数据

## 恢复

复制此配置到 `~/.openclaw/`，然后手动填入真实的 API Key。
