# README.md - 内容部配置说明

## 快速配置

### Step 1: 创建Telegram Bot
1. 在Telegram搜索 @BotFather
2. 发送 `/newbot`
3. 设置名字：`内容总监` 或 `ContentDirector`
4. 设置用户名：`leo_content_bot`
5. 保存Bot Token

### Step 2: 配置config.json
编辑 `/root/.openclaw/agents/content/config.json`：

```json
{
  "channel": "telegram",
  "gateway": {
    "port": 18791
  },
  "plugins": {
    "entries": {
      "telegram": {
        "enabled": true,
        "botToken": "你的Content_Bot_Token",
        "chatId": "你的Telegram_ID",
        "allowedUsers": ["你的Telegram_ID"],
        "polling": true,
        "pollingInterval": 5000
      }
    }
  }
}
```

### Step 3: 启动内容部
```bash
cd /root/.openclaw/agents/content
openclaw gateway start --port 18791
```

## 内容部职责
- 选题策划
- 内容生产
- 质量审核

## 使用方式
给 @leo_content_bot 发送消息即可对话。
