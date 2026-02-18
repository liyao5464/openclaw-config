# README.md - 运营部配置说明

## 快速配置

### Step 1: 创建Telegram Bot
1. 在Telegram搜索 @BotFather
2. 发送 `/newbot`
3. 设置名字：`运营总监` 或 `OpsDirector`
4. 设置用户名：`leo_ops_bot`
5. 保存Bot Token

### Step 2: 配置config.json
编辑 `/root/.openclaw/agents/ops/config.json`：

```json
{
  "channel": "telegram",
  "gateway": {
    "port": 18792
  },
  "plugins": {
    "entries": {
      "telegram": {
        "enabled": true,
        "botToken": "你的Ops_Bot_Token",
        "chatId": "你的Telegram_ID",
        "allowedUsers": ["你的Telegram_ID"],
        "polling": true,
        "pollingInterval": 5000
      }
    }
  }
}
```

### Step 3: 启动运营部
```bash
cd /root/.openclaw/agents/ops
openclaw gateway start --port 18792
```

## 运营部职责
- 数据分析
- 用户增长
- 社群运营

## 使用方式
给 @leo_ops_bot 发送消息即可对话。
