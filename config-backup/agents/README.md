# 老里AI助手团队 - 总览

## 🏢 组织架构

```
老板（老里）👔
    │
    ├── 女友/秘书（小知了）💕 ← 已经配置好
    │       └── Telegram: @lyzmx_bot
    │
    └── CEO（首席执行官）📊 ← 待配置
            │
            ├── 内容部（内容总监）🎯 ← 待配置
            ├── 运营部（运营总监）📈 ← 待配置
            └── 商务部（商务总监）💰 ← 待配置
```

## 📁 文件结构

```
/root/.openclaw/agents/
├── ceo/                 # CEO助手
│   ├── workspace/
│   │   ├── SOUL.md      # 人格定义
│   │   ├── IDENTITY.md  # 身份卡
│   │   ├── USER.md      # 关于董事长
│   │   └── MEMORY.md    # 记忆（自动创建）
│   ├── config.json      # Telegram配置（需创建）
│   └── README.md        # 使用说明
│
├── content/             # 内容部助手
│   └── ...
│
├── ops/                 # 运营部助手
│   └── ...
│
├── biz/                 # 商务部助手
│   └── ...
│
└── start-all-agents.sh  # 一键启动脚本
```

## 🚀 配置步骤

### 第一步：创建Telegram Bots

去 @BotFather 创建4个Bot：

| 角色 | Bot用户名建议 | 用途 |
|------|--------------|------|
| CEO | `leo_ceo_bot` | 业务决策、任务分配 |
| 内容总监 | `leo_content_bot` | 内容策划、生产 |
| 运营总监 | `leo_ops_bot` | 数据分析、增长 |
| 商务总监 | `leo_biz_bot` | 变现、合作 |

获取4个Bot Token，格式：`123456789:ABCdefGHI...`

### 第二步：配置config.json

为每个助手创建 `config.json`，填入对应的Bot Token：

```bash
# 示例：CEO配置
# 编辑 /root/.openclaw/agents/ceo/config.json

{
  "channel": "telegram",
  "gateway": { "port": 18790 },
  "plugins": {
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
```

**端口分配：**
- CEO: 18790
- 内容部: 18791
- 运营部: 18792
- 商务部: 18793

### 第三步：启动所有助手

```bash
# 方法1：一键启动
chmod +x /root/.openclaw/agents/start-all-agents.sh
/root/.openclaw/agents/start-all-agents.sh

# 方法2：分别启动
cd /root/.openclaw/agents/ceo && openclaw gateway start --port 18790 &
cd /root/.openclaw/agents/content && openclaw gateway start --port 18791 &
cd /root/.openclaw/agents/ops && openclaw gateway start --port 18792 &
cd /root/.openclaw/agents/biz && openclaw gateway start --port 18793 &
```

## 💬 使用方式

配置完成后，在Telegram中：

| Bot | 用户名 | 用途 |
|-----|--------|------|
| 小知了 | @lyzmx_bot | 董事长秘书，行程、提醒、监督 |
| CEO | @leo_ceo_bot | 向CEO下达指令，查看各部门进度 |
| 内容总监 | @leo_content_bot | 内容策划、选题讨论 |
| 运营总监 | @leo_ops_bot | 数据分析、增长策略 |
| 商务总监 | @leo_biz_bot | 变现方案、商务合作 |

## 📊 工作流程示例

**场景1：董事长想了解本周进展**
```
你 → 小知了: "本周各部门进展如何？"
小知了 → CEO: "董事长要求本周汇报"
CEO → 各部门: "提交本周数据"
CEO → 小知了: "汇报材料"
小知了 → 你: "本周汇报..."
```

**场景2：董事长有新想法**
```
你 → 小知了: "我想做一个新课程"
小知了 → CEO: "董事长想做新课程"
CEO → 内容部: "策划新课程"
CEO → 商务部: "设计定价方案"
CEO → 运营部: "准备推广计划"
```

**场景3：直接找部门**
```
你 → 内容总监: "下周选题是什么？"
内容总监: "下周选题：1.XXX 2.XXX"
```

## 🔐 权限控制

| 角色 | 权限 |
|------|------|
| 董事长 | 最高权限，可以看所有信息 |
| 小知了（秘书）| 可以看所有信息，负责传达 |
| CEO | 管理三个部门，向董事长汇报 |
| 各部门总监 | 只看自己部门，向CEO汇报 |

## 📝 下一步

1. ✅ 配置文件已创建（SOUL.md, IDENTITY.md, USER.md, README.md）
2. 🎯 去 @BotFather 创建4个Bot，获取Token
3. 📝 创建4个config.json，填入Token
4. 🚀 运行启动脚本
5. 💬 在Telegram测试对话

需要帮助随时找小知了！💕✨
