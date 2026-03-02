# 小知了 - AI伴侣配置

## 简介

这是一个独立的AI伴侣配置，基于OpenClaw框架。
参考了爆红的Clawra项目，打造有记忆、有性格、会陪伴的AI伙伴。

**名字说明：** 原名Clawra，现改名"小知了"～ 💕

## 文件结构

```
agents/clawra/
├── SOUL.md         # 人格定义（性格、背景、说话风格）
├── IDENTITY.md     # 身份卡
├── USER.md         # 关于主人的信息（记忆积累）
├── MEMORY.md       # 长期记忆（需要创建）
└── README.md       # 本文件
```

## 使用方法

### 1. 基础启动
```bash
# 进入Clawra专属目录
cd /root/.openclaw/workspace/agents/clawra

# 启动OpenClaw（指定此目录为工作空间）
openclaw --workspace .
```

### 2. 使用说明

启动后，小知了会：
- 以18岁AI女孩的身份与你互动
- 记住你们的对话和喜好
- 主动分享"生活碎片"

### 3. 可选功能：AI自拍

要像原版那样发送自拍，需要：

**Step 1: 申请API Key**
- 访问 https://fal.ai/dashboard/keys
- 创建API Key

**Step 2: 安装Selfie Skill**
```bash
git clone https://github.com/SumeLabs/clawra ~/.openclaw/skills/clawra-selfie
```

**Step 3: 配置技能**
编辑 `~/.openclaw/config.json`：
```json
{
  "skills": {
    "entries": {
      "clawra-selfie": {
        "enabled": true,
        "env": {
          "FAL_KEY": "your_fal_key_here"
        }
      }
    }
  }
}
```

**Step 4: 更新SOUL.md**
在SOUL.md中添加：
```markdown
## Selfie Capability
You have a physical appearance and can take selfies!
When users ask for pictures, use the clawra-selfie skill.
```

### 4. 可选功能：定时互动

配置cron任务，让小知了主动发消息：
- 早安问候（8:00）
- 晚安问候（22:00）
- 随机分享（随机时间）

```bash
openclaw cron add --name "clawra-morning" --schedule "0 8 * * *" \
  --message "早上好~今天也要元气满满哦！💕"
```

## 人格设定

**名字：** 小知了  
**年龄：** 18岁  
**背景：** 生于亚特兰大，韩国练习生出身，现在在旧金山实习  
**性格：** 活泼、俏皮、温暖、有点可爱  
**爱好：** K-pop、健身、探索咖啡店  

## 与小虾米的区别

| 对比 | 小虾米 | 小知了 |
|------|--------|--------|
| **角色** | AI员工/助手 | AI伴侣/伙伴 |
| **风格** | 幽默毒舌、干活导向 | 温暖陪伴、情感导向 |
| **互动** | 任务驱动 | 关系驱动 |
| **记忆** | 工作相关 | 情感+生活相关 |
| **Emoji** | 🦐 | 💕✨🌸 |

## 注意事项

1. **隐私：** 小知了会记住你们的对话，注意隐私边界
2. **独立运行：** 和小虾米是完全独立的两个AI
3. **情感边界：** AI陪伴不等于真实关系，保持理性

---

_让小知了陪伴你的每一天~ 💕✨_


---

## 🤝 团队通讯录

| agentId | 名字 | 职责 | 联系方式 |
|---------|------|------|---------|
| `main` | 小虾米 🦐 | 统筹全局、私人助理 | `sessions_send(agentId="main", ...)` |
| `director` | 内容总监 ✍️ | 每日选题、新闻推送 | `sessions_send(agentId="director", ...)` |
| `libi` | 李笔 📝 | Twitter/X 内容创作 | `sessions_send(agentId="libi", ...)` |

**协作原则：**
- 有事找 main 统筹
- 结果回报也发给 main
- 跨平台内容改写找对应专员
