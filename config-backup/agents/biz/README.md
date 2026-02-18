# README.md - 商务部配置说明

## 快速配置

### Step 1: 创建Telegram Bot
1. 在Telegram搜索 @BotFather
2. 发送 `/newbot`
3. 设置名字：`商务总监` 或 `BizDirector`
4. 设置用户名：`leo_biz_bot`
5. 保存Bot Token

### Step 2: 配置config.json
编辑 `/root/.openclaw/agents/biz/config.json`：

```json
{
  "channel": "telegram",
  "gateway": {
    "port": 18793
  },
  "plugins": {
    "entries": {
      "telegram": {
        "enabled": true,
        "botToken": "你的Biz_Bot_Token",
        "chatId": "你的Telegram_ID",
        "allowedUsers": ["你的Telegram_ID"],
        "polling": true,
        "pollingInterval": 5000
      }
    }
  }
}
```

### Step 3: 启动商务部
```bash
cd /root/.openclaw/agents/biz
openclaw gateway start --port 18793
```

## 商务部职责
- 变现产品设计
- 销售转化
- 商务合作

## 使用方式
给 @leo_biz_bot 发送消息即可对话。
