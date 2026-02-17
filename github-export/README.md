# OpenClaw 多分身配置

> 一人公司，四个AI员工。个人AI基础设施完全指南。

作者：老里  
配置时间：2026年2月

---

## 🎯 项目简介

这是我在用的 **OpenClaw 多分身配置**，包含4个独立的AI助手，各司其职，协同工作。

**核心理念：** 从"一个AI助理"进化到"AI团队"，每个分身专精一个领域，效率提升10倍。

---

## 🤖 四个AI分身

| 分身 | 角色 | 专长 | Telegram |
|------|------|------|----------|
| **私人助理** | 生活管家 | 日常陪伴、情感支持、生活提醒 | @xiaoxiami_bot |
| **内容总监** | 内容专家 | 选题策划、文章生成、公众号发布 | @leo1_content_bot |
| **育儿师** | 育儿顾问 | 宝宝护理、辅食指导、发育咨询 | @llyuer_bot |
| **视频总监** | 视频专家 | AI视频生成、Seedance 2.0提示词 | @xxx_video_bot |

---

## 📁 目录结构

```
.
├── openclaw.json              # 主配置文件（脱敏）
├── workspace/                 # 私人助理工作区
│   ├── SOUL.md               # 人设定义
│   ├── TOOLS.md              # 工具配置
│   └── AGENTS.md             # 行为准则
├── workspace-director/        # 内容总监工作区
│   ├── SOUL.md
│   ├── TOOLS.md
│   └── AGENTS.md
├── workspace-nanny/           # 育儿师工作区
├── workspace-video-director/  # 视频总监工作区
├── templates/                 # 排版模板
│   ├── wechat-compatible-template.html    # 公众号发布用
│   └── tech-article-template.html         # 本地预览用
└── README.md                  # 本文件
```

---

## 🚀 快速开始

### 1. 安装 OpenClaw

```bash
# macOS/Linux
curl -fsSL https://openclaw.ai/install.sh | sh

# 或使用 npm
npm install -g openclaw
```

### 2. 克隆配置

```bash
git clone https://github.com/YOUR_USERNAME/openclaw-config.git
cd openclaw-config
```

### 3. 配置API Keys

复制 `openclaw.json` 中的占位符，替换为你的真实密钥：

```json
{
  "channels": {
    "telegram": {
      "accounts": {
        "bot_main": {
          "botToken": "8408136864:xxxxxxxxxx"  // 你的Bot Token
        }
      }
    },
    "feishu": {
      "appId": "cli_xxxxxxxx",
      "appSecret": "xxxxxxxx"
    }
  },
  "skills": {
    "baoyu-post-to-wechat": {
      "env": {
        "WECHAT_APP_ID": "wxbde0f982xxxxxxxx",
        "WECHAT_APP_SECRET": "xxxxxxxx"
      }
    }
  }
}
```

### 4. 启动OpenClaw

```bash
openclaw gateway start
```

---

## 🎨 排版模板

### 微信兼容模板
**用途：** 发布到微信公众号  
**特点：** 全部内联样式，微信编辑器不会过滤  
**使用方法：** 复制全文粘贴到公众号编辑器

### 科技风模板
**用途：** 本地预览/发送给用户  
**特点：** 视觉效果更好，支持阴影、渐变  
**使用方法：** 浏览器打开或发送HTML文件

---

## 🛠️ 已配置技能

| 技能 | 用途 | 状态 |
|------|------|------|
| baoyu-post-to-wechat | 公众号发布 | ✅ |
| baoyu-markdown-to-html | 格式转换 | ✅ |
| baoyu-image-gen | AI图片生成 | ✅ |
| baoyu-url-to-markdown | 网页抓取 | ✅ |
| seedance2 | Seedance 2.0提示词 | ✅ |
| humanizer | 去AI味 | ✅ |

---

## 📝 使用示例

### 场景1：发布公众号文章

**用户：** 内容总监，帮我写篇关于AI的文章，发布到公众号草稿箱

**内容总监会：**
1. 确认选题方向
2. 生成文章（去AI味处理）
3. 使用微信兼容模板生成HTML
4. API发布到公众号草稿箱
5. 返回管理链接

### 场景2：生成视频提示词

**用户：** 视频总监，帮我写个Seedance提示词，要教育科普风格

**视频总监会：**
1. 确认视频类型和风格
2. 生成符合Seedance 2.0规范的提示词
3. 包含镜头语言（@zoom in/out等）
4. 发送提示词和参考示例

---

## 🔐 安全提醒

- **永远不要**将 `.env` 文件或真实API keys提交到GitHub
- 本仓库中的 `openclaw.json` 已脱敏，所有密钥均为占位符
- 定期检查GitHub Token，及时撤销不再使用的Token

---

## 📚 参考资源

- [OpenClaw 官方文档](https://docs.openclaw.ai)
- [42章经播客：从Clawdbot到AI Coding](https://www.xiaoyuzhoufm.com/episode/698563a188663289fe80769a)
- [GitHub - awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills)

---

## 💬 交流反馈

如果你在使用过程中遇到问题，或有更好的配置建议，欢迎交流！

**首发公众号：**「老里的一人公司」

---

*未来已来，只是分布不均。开始搭建你的AI团队吧！* 🚀
