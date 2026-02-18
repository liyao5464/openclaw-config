# README.md - 高级育儿师配置说明

## 快速配置

### Step 1: 创建Telegram Bot
1. 在Telegram搜索 @BotFather
2. 发送 `/newbot`
3. 设置名字：`育儿师` 或 `宝宝管家`
4. 设置用户名：`leo_baby_bot`（必须以bot结尾）
5. 保存Bot Token

### Step 2: 配置config.json
编辑 `/root/.openclaw/agents/baby-care/config.json`：

```json
{
  "channel": "telegram",
  "gateway": {
    "port": 18794
  },
  "plugins": {
    "entries": {
      "telegram": {
        "enabled": true,
        "botToken": "你的育儿师_Bot_Token",
        "chatId": "你的Telegram_ID",
        "allowedUsers": ["你的Telegram_ID"],
        "polling": true,
        "pollingInterval": 5000
      }
    }
  }
}
```

### Step 3: 启动育儿师
```bash
cd /root/.openclaw/agents/baby-care
openclaw gateway start --port 18794
```

## 育儿师职责
- 10个月宝宝护理指导
- 辅食添加建议
- 疫苗接种提醒
- 早教游戏推荐
- 健康问题初步建议（非医疗诊断）

## 使用方式
给 @leo_baby_bot 发送消息：
- "今天辅食吃什么？"
- "宝宝发烧了怎么办？"
- "明天该打疫苗吗？"
- "10个月应该学什么？"

## 重要提醒
⚠️ 育儿师提供的是建议和经验分享，**不能替代医生诊断**。
宝宝如有严重疾病症状，请及时就医。
