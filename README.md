# OpenClaw 配置文件备份

> 脱敏后的配置备份，API Key 已用占位符替换。

## 包含

- `openclaw.json` — 主配置（模型、agents、插件）
- `config.json` — 基本设置
- `.env` — 环境变量

## 不含

- credentials/ — 敏感凭证
- skills/ — 技能配置（已在另一个 repo）
- agents/*/sessions/ — 会话历史
- agents/*/agent/auth*.json — 认证信息
