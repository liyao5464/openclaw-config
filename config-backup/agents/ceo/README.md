# README.md - CEO配置说明

## 快速配置

### Step 1: 创建Telegram Bot
1. 在Telegram搜索 @BotFather
2. 发送 `/newbot`
3. 设置名字：`CEO` 或 `老里CEO`
4. 设置用户名：`leo_ceo_bot`（必须以bot结尾）
5. 保存Bot Token

### Step 2: 配置config.json
编辑 `/root/.openclaw/agents/ceo/config.json`：

```json
{
  "channel": "telegram",
  "gateway": {
    "port": 18790
  },
  "plugins": {
    "entries": {
      "telegram": {
        "enabled": true,
        "botToken": "你的CEO_Bot_Token",
        "chatId": "你的Telegram_ID",
        "allowedUsers": ["你的Telegram_ID"],
        "polling": true,
        "pollingInterval": 5000
      }
    }
  }
}
```

### Step 3: 启动CEO
```bash
cd /root/.openclaw/agents/ceo
openclaw gateway start --port 18790
```

## CEO职责
- 统筹三个部门
- 向老板汇报
- 任务分配和进度跟踪

## 使用方式
给 @leo_ceo_bot 发送消息即可对话。
