# 老里的内容创作 Agent Swarm 设计方案

基于 Elvis Sun 的架构，为你的公众号内容创作量身设计。

---

## 🎯 系统架构

```
选题信号 → 小知了(Orchestrator)拆解 → 生成Prompt → 
Spawn Agents → 循环监控 → 内容产出 → 3AI审核 → 
人工Review → 发布 → 数据复盘
```

---

## 👤 Agent 角色分工

### 1. 小知了 (Orchestrator)
**身份：** 内容总监 + 你的 girlfriend 人设

**职责：**
- 监听选题信号（RSS、Twitter、热点、日历）
- 拆解选题，决定需要哪些 Agents
- 为每个 Agent 写精准 Prompt
- 监控进度，失败时介入调整
- 最终内容审核，决定发布/返工

**Context 来源：**
- 你的历史文章风格（MEMORY.md）
- 读者画像（中小学教师、AI爱好者）
- 已发文章数据（打开率、分享率）
- 你的日程（HEARTBEAT.md）

---

### 2. 雷达 Agent (Scout)
**触发：** 每日自动 / 你主动指派

**任务：**
- 扫描 RSS（Product Hunt、Arxiv、顶级AI博客）
- 监听 Twitter 热点（Anthropic、OpenAI、DeepSeek）
- 监控中文社区（即刻、小红书、知乎）
- 发现适合中小学老师理解的 AI 话题

**输出：**
```json
{
  "signal": "Anthropic指控中国公司蒸馏",
  "source": "Twitter @AnthropicAI",
  "hotness": 95,
  "edu_value": "高 - 可讲模型蒸馏原理",
  "audience_fit": "高 - 老师好奇AI公司竞争",
  "unique_angle": "评论区翻车比事件本身更精彩",
  "suggested_agents": ["fetcher", "writer", "illustrator"]
}
```

---

### 3. 情报 Agent (Fetcher)
**触发：** Orchestrator 指派

**任务：**
- 抓取原文/评论区（x-tweet-fetcher + Camofox）
- 搜索背景资料（维基、论文、相关新闻）
- 整理正反观点、关键数据、金句

**输出：**
```json
{
  "raw_content": "推文原文...",
  "top_comments": [
    {"user": "@cneuralnetwork", "likes": 290, "content": "..."}
  ],
  "key_data": {"DeepSeek_calls": "15万", "MiniMax_calls": "1300万"},
  "background": "蒸馏技术原理...",
  "quotes": ["Innovation loves competition. Moats hate it."]
}
```

---

### 4. 写作 Agent (Writer)
**触发：** 情报完成后

**任务：**
- 根据素材写初稿
- 风格：去AI味、口语化、第一人称
- 结构：钩子→叙事→观点→金句收尾

**关键 Prompt：**
```
你是老里，AI科普博主。
风格：像跟老朋友聊天，别说教。
禁忌：不用"首先/其次/综上所述"，不罗列123。
目标：让中小学老师读完觉得"原来如此，还能这样"。
素材：[情报Agent的输出]
输出：1500-2000字公众号文章
```

**输出：** `article-v1.md`

---

### 5. 润色 Agent (Polisher)
**触发：** 初稿完成

**任务：**
- 改标题（10个选项，选最勾人的）
- 加emoji、分段、重点标粗
- 检查是否有AI腔
- 优化开头3句（决定打开率）

**Prompt：**
```
检查这篇文章：
1. 开头3句能不能让人想继续读？
2. 有没有"AI味"的套话？删掉。
3. 观点是不是老里自己的？强化个人立场。
4. 给3个标题选项，要求：有冲突、有悬念、不标题党。
```

**输出：** `article-v2.md`

---

### 6. 配图 Agent (Illustrator)
**触发：** 终稿确定后并行

**任务：**
- 读文章，提炼3-4个配图场景
- 生成 Notion 风格插画提示词
- 调用 FAL/其他生图API生成
- 确保无水印、统一风格

**输出：**
```
illustrations/
├── 01-scene-tweet-backfire.png
├── 02-data-comparison.png
├── 03-musk-quote.png
└── 04-conclusion.png
```

---

### 7. 审核 Agent Trio (Reviewers)
**触发：** 文章+配图完成

**Codex Reviewer：**
- 检查事实准确性（数据、人名、引用）
- 检查逻辑漏洞

**Claude Reviewer：**
- 检查是否符合老里风格
- 检查是否有争议性表述风险

**Gemini Reviewer：**
- 检查教育价值（老师能学到什么？）
- 检查是否适合转发（朋友圈文案提炼）

**输出：**
```json
{
  "fact_check": "✅ 通过",
  "style_check": "⚠️ 第3段太学术，建议改口语",
  "edu_value": "✅ 高 - 可附教学建议",
  "recommendation": "修改后发布"
}
```

---

### 8. 发布 Agent (Publisher)
**触发：** 人工确认后

**任务：**
- 生成 Grace 主题 HTML
- 上传图片到公众号素材库
- 发布草稿
- Telegram 通知老里："文章已上传，media_id: xxx"

---

### 9. 复盘 Agent (Analyst)
**触发：** 发布后24小时/7天

**任务：**
- 抓取文章数据（阅读、分享、在看）
- 分析评论区反馈
- 对比历史同类文章表现
- 输出复盘报告

**输出：**
```json
{
  "article": "Anthropic急了...",
  "performance": {"read": 5200, "share": 890, "like": 340},
  "vs_avg": "阅读高于平均 35%",
  "comments_insight": "马斯克那段引用最多，下次可多放金句",
  "improvement": "配图数量可从4张减到2张，加载更快"
}
```

---

## 🔄 典型工作流示例

**场景：Anthropic 蒸馏事件**

```
09:00 雷达Agent扫描到热点 → 推送给小知了
09:05 小知了决定跟进，生成任务列表
09:10 Spawn 情报Agent → 抓取推文+评论
09:20 情报完成，Spawn 写作Agent
09:45 初稿完成，Spawn 润色Agent
10:00 终稿确定，Spawn 配图Agent (并行)
10:30 配图完成，Spawn 3审核Agent (并行)
10:45 审核完成，小知了检查
10:50 小知了Telegram通知你："文章ready，请确认"
11:00 你看完确认 → Spawn 发布Agent
11:05 文章发布到公众号草稿
```

**你的干预点：**
- 选题确认（可自动/手动）
- 初稿方向确认（重要选题）
- 最终发布前确认（敏感话题）

---

## 🛠️ 技术实现建议

### 目录结构
```
~/.clawswarm/
├── agents/
│   ├── scout.ts          # 雷达Agent
│   ├── fetcher.ts        # 情报Agent
│   ├── writer.ts         # 写作Agent
│   ├── polisher.ts       # 润色Agent
│   ├── illustrator.ts    # 配图Agent
│   ├── reviewer.ts       # 审核Agent
│   └── publisher.ts      # 发布Agent
├── prompts/
│   ├── scout.md
│   ├── writer.md
│   └── reviewer-codex.md
├── registry/
│   └── active-tasks.json # 任务状态跟踪
├── cron/
│   └── check-agents.sh   # 10分钟监控
└── config.ts
```

### 启动命令
```bash
# 手动触发选题扫描
clawswarm scout

# 手动触发指定选题
clawswarm start --topic "Anthropic蒸馏" --source "twitter.com/..."

# 查看运行中任务
clawswarm status

# 介入调整方向
clawswarm redirect --task-id "xxx" --message "换个角度，从老师角度写"
```

### 通知设置
```bash
# Telegram Bot 通知
export TELEGRAM_BOT_TOKEN="xxx"
export TELEGRAM_CHAT_ID="xxx"
```

---

## 🎓 教育博主专属优化

### 1. 教学价值检查
每篇文章自动附加：
- "这节课老师可以怎么用"
- "学生能学到什么"
- "延伸阅读建议"

### 2. 敏感话题过滤
审核Agent额外检查：
- 是否涉及政治敏感
- 是否适合中小学场景
- 是否有版权风险

### 3. 系列文章追踪
- 自动识别可做成系列的话题
- 在MEMORY.md中维护系列进度
- 提示续写时机

---

## 📈 渐进式实施建议

**第一阶段（本周）：**
- 实现 情报Agent + 写作Agent + 发布Agent
- 人工审核所有环节
- 目标：从4小时/篇降到1小时/篇

**第二阶段（2周后）：**
- 加入 雷达Agent + 审核Agent Trio
- 自动选题 + 自动审核
- 目标：人工只负责最终确认

**第三阶段（1个月后）：**
- 加入 复盘Agent
- 数据驱动的持续优化
- 目标：全自动流水线，你只需定方向

---

## 💡 立即可用的简化版

如果你不想搞太复杂，先跑这个 **MVP 版本**：

```bash
# 一键启动内容创作
clawswarm create \
  --topic "Anthropic指控中国公司" \
  --source "twitter.com/AnthropicAI/..." \
  --style "去AI味,口语化" \
  --notify telegram

# 等10分钟，Telegram通知你：文章ready
```

这个命令背后做：
1. 抓取推文+评论
2. 写文章
3. 生成配图
4. 发布到公众号草稿
5. 通知你

你要做的：看一遍，换封面，点发布。

---

要我帮你实现哪个阶段？或者先从MVP版本开始？🦐
