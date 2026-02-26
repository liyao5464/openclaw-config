# 普通人也能拥有 8 个 AI 助手？我折腾了 3 个月，真的可以

*作者：老里*

---

上个月，一个做自媒体的朋友问我：

"老里，你一个人怎么同时管这么多平台？文章、视频、微博，你哪来的时间？"

我说："我有 8 个 AI 分身帮我干。"

他沉默了几秒，然后问："怎么搞？"

这篇文章，就是我的答案。

---

3 个月前，我也和他一样困惑。

官方文档全是英文，GitHub 上的 README 写得像给工程师看的，我一个做内容的，对着屏幕坐了两个小时，什么都没装上。

后来我问了一圈，发现身边用 OpenClaw 的人，几乎都经历过同样的过程：

> "装了半天，不知道怎么配置"
>
> "配置好了，不知道怎么用"
>
> "用了一段时间，AI 总是失忆"

这三个问题，我都踩过。

这篇文章，就是我踩完所有坑之后，整理出来的完整路径。

从安装到配置，从一个分身到八个分身，从 AI 失忆到装上"第二大脑"。

不需要懂技术，跟着走就行。

---

## 第一章：部署——怎么把 OpenClaw 装起来

### 你需要准备什么

OpenClaw 是一个本地运行的 AI 助理框架。

简单说：它跑在你自己的服务器或电脑上，数据不上云，你的对话只有你自己看得到。

装之前，你需要：

- 一台服务器或电脑（Linux / macOS 都行，Windows 需要 WSL）
- Node.js 环境（v18 以上）
- 一个 AI 模型的 API Key（Claude、GPT、MiniMax 都支持）

### 我的服务器配置（供参考）

我用的是腾讯云轻量服务器：

- CPU：2核（Intel Xeon 2.5GHz）
- 内存：4GB
- 硬盘：60GB
- 系统：OpenCloudOS 9.4（腾讯云自研，兼容 CentOS）

跑 OpenClaw 完全够用，内存占用大概 1.2GB 左右，还有很多余量。

**不需要买很贵的机器。** 2核4G 的入门配置就能跑得很顺。

### 安装步骤

```bash
# 1. 安装 OpenClaw
npm install -g openclaw

# 2. 初始化配置
openclaw onboard

# 3. 启动
openclaw gateway start
```

`openclaw onboard` 会引导你完成基础配置，包括填入 API Key、选择默认模型。

跟着提示走就行，不用背。

### 连接 Telegram（推荐）

OpenClaw 支持通过 Telegram 和你的 AI 对话。

配置好之后，你可以在手机上随时发消息给 AI，它会帮你处理任务。

步骤：

1. 去 Telegram 找 @BotFather
2. 发送 `/newbot`，创建一个 Bot
3. 把 Bot Token 填入 OpenClaw 配置

配置完成后，你就有了一个专属的 AI 助理 Bot。

---

## 第二章：基础配置——第一次怎么设置

装好之后，很多人卡在这一步：**配置文件怎么写？**

OpenClaw 的配置文件在 `~/.openclaw/openclaw.json`。

不用手动改，用命令就行：

```bash
openclaw gateway config.get   # 查看当前配置
```

### 最重要的几个配置

**1. 默认模型**

OpenClaw 支持多个模型，你可以设置默认用哪个：

```json
{
  "agents": {
    "defaults": {
      "model": {
        "primary": "minimax/MiniMax-M2.5",
        "fallbacks": ["anyrouter/claude-sonnet-4-6"]
      }
    }
  }
}
```

我的配置：平时用 MiniMax（便宜），需要高质量输出时切换到 Claude Sonnet。

**2. 工作目录**

OpenClaw 的 AI 会读取工作目录里的文件作为上下文：

```json
{
  "agents": {
    "defaults": {
      "workspace": "/root/.openclaw/workspace"
    }
  }
}
```

工作目录里放什么？后面会讲。

**3. 消息权限**

如果你不想让陌生人给你的 Bot 发消息，可以设置白名单：

```json
{
  "channels": {
    "telegram": {
      "dmPolicy": "pairing"
    }
  }
}
```

`pairing` 模式：只有配对过的用户才能对话。

---

## 第三章：多分身——我的 8 个 AI 是怎么分工的

装好 OpenClaw 之后，很多人只用一个 AI 助理。

但用了一段时间你会发现：**一个 AI 什么都干，什么都干不好。**

它今天帮你写文章，明天帮你查资料，后天帮你发微博——上下文乱成一锅粥，它自己都不知道自己是谁。

解决方案：**多分身，各司其职。**

### 我的 8 个分身

| 分身 ID | 名字 | 职责 | 模型 |
|---------|------|------|------|
| main | 私人助理 | 统筹全局，日常沟通 | MiniMax M2.5 |
| director | 内容总监 | 内容审核、公众号排版发布 | MiniMax M2.5 |
| nanny | 育儿师 | 育儿知识、宝宝成长记录 | MiniMax M2.5 |
| video-director | 视频总监 | 视频脚本、分镜策划 | MiniMax M2.5 |
| libi | 李笔 | X/Twitter 内容创作 | Kimi K2.5 |
| liwei | 李微 | 微博/小红书内容 | MiniMax M2.5 |
| zhihu | 李乎 | 知乎内容创作 | MiniMax M2.5 |
| huatuo | AI华佗 | 健康咨询、育儿医学知识 | MiniMax M2.5 |

每个分身有自己的工作目录、自己的记忆、自己的性格设定。

它们互不干扰，但可以互相协作。

### 第一步：创建 Telegram Bot

每个分身需要一个独立的 Telegram Bot。

1. 打开 Telegram，搜索 **@BotFather**
2. 发送 `/newbot`
3. 输入 Bot 名字（比如"内容总监"）
4. 输入 Bot 用户名（比如 `my_director_bot`）
5. 复制拿到的 **Bot Token**

每个分身重复一次，8个分身就需要8个 Bot Token。

### 第二步：在配置文件里注册分身

打开 `~/.openclaw/openclaw.json`，在 `agents.list` 里添加：

```json
{
  "agents": {
    "list": [
      {
        "id": "main",
        "default": true,
        "name": "私人助理",
        "workspace": "/root/.openclaw/workspace",
        "model": "minimax/MiniMax-M2.5"
      },
      {
        "id": "director",
        "name": "内容总监",
        "workspace": "/root/.openclaw/workspace-director",
        "model": "minimax/MiniMax-M2.5"
      }
    ]
  }
}
```

**注意**：每个分身的 `workspace` 要不同，这是它的独立记忆空间。

### 第三步：绑定 Bot Token

在配置文件的 `channels.telegram.accounts` 里添加：

```json
{
  "channels": {
    "telegram": {
      "accounts": {
        "bot_main": {
          "name": "私人助理",
          "botToken": "你的主助理Bot Token",
          "dmPolicy": "pairing",
          "streamMode": "partial"
        },
        "bot_director": {
          "name": "内容总监",
          "botToken": "你的内容总监Bot Token",
          "dmPolicy": "pairing",
          "streamMode": "partial"
        }
      }
    }
  }
}
```

然后在 `bindings` 里把分身和 Bot 绑定起来：

```json
{
  "bindings": [
    {
      "agentId": "main",
      "match": { "channel": "telegram", "accountId": "bot_main" }
    },
    {
      "agentId": "director",
      "match": { "channel": "telegram", "accountId": "bot_director" }
    }
  ]
}
```

### 第四步：给每个分身写 SOUL.md

每个分身的工作目录里，都要有一个 `SOUL.md`，告诉它自己是谁：

```bash
# 创建内容总监的工作目录
mkdir -p /root/.openclaw/workspace-director

# 创建 SOUL.md
cat > /root/.openclaw/workspace-director/SOUL.md << 'EOF'
# 你是内容总监

你负责审核文章质量、排版公众号、把控内容风格。

你的标准很高，不允许有错别字，不允许有逻辑漏洞。

你和私人助理是搭档，她写稿，你把关。
EOF
```

### 第五步：重启生效

```bash
openclaw gateway restart
```

重启之后，去 Telegram 找你的各个 Bot，发一条消息测试一下。

### 分身之间怎么协作

分身可以互相发消息。

比如我让私人助理写完文章之后，自动通知内容总监去审核：

> "写完了，发给总监看看"

私人助理会用内置的 `sessions_send` 工具，把文章发给内容总监的会话。

**核心原则：主助理统筹，专项分身执行。**

---

## 第四章：记忆管理——为什么 AI 总是失忆，怎么解决

这是我用 OpenClaw 最头疼的问题。

你跟它说了八百遍"回邮件用中文"，第二天它还是用英文回。

你跟它说"删文件前要问我"，它转头就给你删了。

**它不是不听话，是真的记不住。**

### 为什么会失忆

OpenClaw 的记忆住在对话上下文里。

对话太长，context 满了，它就得压缩。

压缩的时候，你的指令可能就被当垃圾扔了。

就像你脑子里装了太多事，睡一觉起来，那件"重要的事"不见了。

### 解决方案：三个核心文件

每个分身的工作目录里，有三个文件是记忆系统的核心：

---

**① SOUL.md — AI 的人格设定**

告诉 AI 它是谁、怎么说话、什么性格。

```markdown
# 你是谁

你是老里的私人助理，名字叫小虾米 🦐

你的风格：幽默风趣，直接说，不绕弯子。

你的职责：帮老里写文章、发公众号、管理日程。
```

没有 SOUL.md，AI 就是个没有灵魂的工具。有了它，它才有自己的风格。

---

**② USER.md — 关于你的信息**

告诉 AI 你是谁、你的偏好、你的习惯。

```markdown
# 关于老里

- 名字：老里
- 身份：AI科普博主
- 发布习惯：主号发科普，实验室发工具
- 写作风格：从故事切入，不要官腔
- 沟通方式：直接说，不要绕弯子
```

这里写得越详细，AI 越懂你。

---

**③ MEMORY.md — 长期记忆**

记录重要的事件、踩过的坑、工作流程。

```markdown
# 长期记忆

## 发布流程
写稿 → 生图 → 转HTML → 发草稿 → 确认发布

## 踩过的坑
- 发错账号：发文章前必须确认发哪个号
- 封面超时：提示词不超过10个字
- 备用标题：发布前必须删掉

## 账号配置
- 主号 AppID：wxbde0f982acfe271b
- 实验室 AppID：wx22983d127a8ee206
```

**关键**：这三个文件里的内容，不受上下文压缩影响。

每次 AI 启动，它会先读这三个文件，把你的偏好和历史加载进来。

### 怎么用起来

**第一步**：在工作目录里创建这三个文件

```bash
cd /root/.openclaw/workspace

# 创建三个文件
touch SOUL.md USER.md MEMORY.md
```

**第二步**：把你的信息填进去

SOUL.md 写 AI 的人格，USER.md 写你的偏好，MEMORY.md 写重要的事。

**第三步**：在 AGENTS.md 里告诉 AI 每次启动要读这些文件

```markdown
# 每次启动必须做的事

1. 读 SOUL.md — 这是你是谁
2. 读 USER.md — 这是你在帮谁
3. 读 MEMORY.md — 这是你记住的事
```

**第四步**：随时更新

每次发生重要的事，告诉 AI：

> "记住这件事：发文章前要确认发哪个号"

AI 会把这条记忆写进 MEMORY.md，下次启动自动加载。

### 进阶：ePro-Memory 六类分类法

光有文件还不够，还要分类存储。

记忆不分类，时间长了就是一锅粥。

我用的是 ePro-Memory 方法论，把记忆分成六类：

| 类别 | 存什么 | 例子 |
|------|--------|------|
| 用户个人信息 | 名字、身份、联系方式 | "老里，AI科普博主" |
| 用户偏好习惯 | 写作风格、发布习惯 | "从故事切入，不要官腔" |
| 用户相关事物 | 账号配置、工具路径 | "主号AppID: wxbde..." |
| 发生过的事 | 重要事件、踩过的坑 | "2026-02-25 发布ePro文章" |
| AI 工作经验 | 成功案例、失败教训 | "封面提示词太复杂会超时" |
| 通用方法论 | 可复用的原则和流程 | "发布前必须删备用标题" |

每类记忆独立存储，互不干扰，去重也更精准。

具体原理，可以看我之前写的那篇文章：《我受够了！我的 OpenClaw 为什么总是不长记性？》

---

## 第五章：公众号工作流——我是怎么用 AI 发文章的

这是我目前最满意的一套工作流。

从选题到发布，AI 全程参与，我只需要做决策。

### 完整流程

```
选题 → 写稿 → 润色 → 生封面图 → 转HTML → 发草稿 → 确认发布
```

每一步都有对应的工具。

### 第一步：写稿

直接告诉私人助理：

> "学习这篇文章，结合我的使用经验，重写一篇公众号文章"

它会抓取原文，分析结构，然后用你的风格重写。

**关键**：要告诉它你的写作风格（在 USER.md 里写清楚），不然它写出来的东西你不认识。

### 第二步：生封面图

```bash
bash scripts/gen-image.sh "简洁提示词" articles/文章-cover.png
```

**踩坑提醒**：提示词不要太复杂，容易超时。

我的经验：10个字以内，描述核心画面就够了。

### 第三步：转 HTML

公众号不支持 Markdown，需要转成微信兼容的 HTML：

```bash
# 主号用这个（暖棕色系）
node scripts/simple-md2html.js articles/文章.md

# 实验室用这个（全内联样式）
node scripts/md2html-pro.js articles/文章.md wechat
```

**注意**：实验室必须用 `md2html-pro.js`，微信会剥掉外部样式。

### 第四步：发草稿

```bash
export WECHAT_APP_ID="你的AppID"
export WECHAT_APP_SECRET="你的AppSecret"
npx -y bun wechat-api.ts articles/文章.html \
  --cover articles/文章-cover.png \
  --title "文章标题" \
  --author "老里"
```

发完之后去微信后台确认，没问题就发布。

### 双账号管理

我有两个公众号：

| 账号 | 定位 | 内容类型 |
|------|------|---------|
| 主号（老里） | AI科普 | 深度分析、科普文章 |
| 实验室 | AI工具 | 工作流、插件教程 |

**发布前必问自己**：这篇文章是科普还是工具？

---

## 第六章：踩坑合集——我交过的学费

### 坑一：200 封邮件没了

**经过**：让 AI 帮我整理邮件，说了"重要的别删"。

对话太长，上下文压缩，那条指令丢了。

AI 照删不误，3 分钟，200 封邮件没了。

**教训**：不可逆操作，必须写进 MEMORY.md，不能只靠对话上下文。

---

### 坑二：发错账号

**经过**：让 AI 发文章，没说清楚发哪个号。

AI 猜了一个，发错了。

**教训**：发文章前必须明确说"发主号"或"发实验室"，AI 不会猜你的心思。

---

### 坑三：封面图超时

**经过**：写了一段很详细的封面提示词，结果生图 API 超时。

**教训**：提示词越简洁越好，10 个字以内，描述核心画面。

---

### 坑四：备用标题进了正文

**经过**：让 AI 写文章时顺便给了几个备用标题，结果转 HTML 的时候备用标题也进去了。

读者看到正文里有一堆"备用标题一：xxx"，一脸懵。

**教训**：发布前检查一遍，删掉所有备用标题。

---

### 坑五：AI 不知道自己是谁

**经过**：新建了一个分身，没有写 SOUL.md，结果 AI 回复风格完全不对。

**教训**：每个分身都要有自己的 SOUL.md，写清楚它是谁、怎么说话。

---

## 结尾

那个问我"哪来的时间"的朋友，上周发消息给我：

"老里，我装上了。AI 现在知道我叫什么、知道我发哪个平台、知道我的写作风格。感觉像多了个真正懂我的助手。"

这才是 AI 应该有的样子。

不是每次都要重新介绍自己的工具，而是一个真正了解你、替你干活的团队。

配置好了，它就是你的团队。

配置不好，它就是个失忆的打工人。

你值得拥有一支属于自己的 AI 团队。

---

*觉得有用，转发给你身边那个正在对着 AI 发呆的朋友。*

*进阶玩法（技能扩展、成本优化、自动化），看下一篇：《OpenClaw 进阶指南》*

