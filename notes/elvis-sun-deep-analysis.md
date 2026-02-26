# Elvis Sun 工作流 - 深度解析 v2

> 原文：https://x.com/elvissun/article/2025920521871716562

---

## 🧠 第一层：表面看到的

8步流水线、tmux、JSON注册表、三AI审核...

这些是**工具**，不是核心。

---

## 🔥 第二层：真正的洞察

### 洞察1：Context Window 是零和博弈

> "Context windows are zero-sum. You have to choose what goes in."

这句话是整篇文章的灵魂。

**传统做法：**
```
一个 AI → 塞入所有信息（代码 + 业务 + 历史）
结果：什么都知道一点，什么都做不好
```

**Elvis 的做法：**
```
Orchestrator → 只装业务上下文（Obsidian）
Coding Agent → 只装代码上下文
每个 AI 只做它最擅长的事
```

**关键词：** "Specialization through context, not through different models."

不是因为模型不同才分工，是因为**给的信息不同**才分工。

---

### 洞察2：完成的定义（Definition of Done）

这是整个系统能跑起来的关键，但文章里只用了一段话带过。

```
PR created
+ Branch synced to main（无冲突）
+ CI passing（lint/types/unit/E2E）
+ Codex review passed
+ Claude review passed
+ Gemini review passed
+ Screenshots included（UI变更时）
= DONE
```

**为什么重要？**

Agent 不知道"完成"是什么意思，除非你告诉它。

大多数人让 Agent 写完代码就算完，Elvis 的 Agent 要过完所有关卡才算完。这就是为什么他可以"不读代码直接 merge"。

---

### 洞察3：tmux 的真正价值不是并行，是**可干预**

大多数人用 tmux 是为了并行跑多个 Agent。

Elvis 用 tmux 是为了**中途纠正方向而不杀死 Agent**：

```bash
# Agent 走错方向了？不用重来
tmux send-keys -t codex-templates "Stop. Focus on API first." Enter

# 需要补充信息？
tmux send-keys -t codex-templates "Schema is in src/types/template.ts" Enter
```

**类比：** 这就像你雇了个员工，发现他做错了，你可以拍拍他肩膀说"换个方向"，而不是开除他重新招人。

---

### 洞察4：Zoe 的权限设计（安全边界）

| 角色 | 权限 |
|------|------|
| Zoe (Orchestrator) | Admin API + 只读生产数据库 |
| Coding Agents | **什么都没有** |

Coding Agent 永远不会接触生产数据库。

这不只是安全考虑，更是**职责分离**：
- Zoe 负责"知道什么"
- Agent 负责"做什么"

---

### 洞察5：监控脚本的设计哲学

> "The script is 100% deterministic and extremely token-efficient."

Cron 每10分钟跑一次，但**不直接问 AI**，而是：
1. 读 JSON 注册表（纯文件操作）
2. 检查 tmux 是否存活（shell 命令）
3. 查 CI 状态（gh cli）
4. **只在需要人工时才通知**

**为什么重要？** 大多数人的监控方案是"每隔一段时间问 AI 进展如何"，这既贵又慢。Elvis 的方案是确定性脚本 + 只在异常时触发 AI。

---

### 洞察6：Zoe 的主动性（Proactive Work Finding）

这是 94 commits/天 的真正来源：

| 时间 | 触发源 | 动作 |
|------|--------|------|
| 早上 | Sentry 错误日志 | 自动 spawn 修复 Agent |
| 会后 | Obsidian 会议笔记 | 自动识别 feature 需求 → spawn Agent |
| 晚上 | git log | 自动更新 changelog |

Elvis 去散步，回来就有 7 个 PR 等着 review。

**关键：** Zoe 不等人分配任务，她**主动找活干**。

---

### 洞察7：强化学习循环（真正的自我改进）

**传统 Ralph Loop：**
```
记忆 → 生成 → 评估 → 保存学习
问题：Prompt 是静态的，只改进了检索
```

**Elvis 的升级：**
```
失败 → Zoe 用业务上下文分析失败原因
     → 改写 Prompt（不是重复同一个 Prompt）
     → 重试
成功 → 记录成功模式
     → 下次同类任务用更好的 Prompt
```

**奖励信号：** CI passing + 3 reviews passing + 人工 merge

**失败信号：** CI 失败 / review 不通过 / Agent 卡住

这是真正的强化学习，不是噱头。

---

## 🎯 第三层：对老里的直接启示

### 你的场景 vs Elvis 的场景

| 维度 | Elvis | 老里 |
|------|-------|------|
| 核心产出 | 代码/PR | 文章/内容 |
| 质量标准 | CI + 3 AI review | 风格 + 受众匹配 + 传播力 |
| 上下文来源 | Obsidian（客户/会议） | 历史文章 + 受众画像 + 选题库 |
| 主要 Agent | Codex/Claude/Gemini | Research/Writer/Reviewer |

### 可以直接复用的设计

**1. 双层架构**
```
小知了 (Orchestrator)
  → 持有：老里的写作风格、历史文章、受众画像
  → 职责：拆解选题、写 Prompt、选模型、监控质量

Writer Agent
  → 持有：当前选题的素材 + 精简风格指南
  → 职责：专注写作，不管其他
```

**2. 完成的定义（内容版）**
```
初稿生成
+ 字数达标（1200-2000字）
+ 去AI味检查通过
+ 敏感词检查通过
+ 标题吸引力评分 > 7/10
+ 配图提示词生成
= DONE（可发布）
```

**3. 可干预的写作流程**

不要一次性生成，要用"tmux 思维"：
- 生成开头 → 确认方向 → 继续
- 发现跑偏 → 直接纠正 → 不重来

**4. 主动找选题**

小知了可以主动：
- 早上扫 HN/Twitter 热点
- 发现好选题 → 通知老里确认
- 确认后自动开始写作流程

**5. 记录成功模式**

哪类文章传播好？哪种开头钩子有效？记录下来，下次用更好的 Prompt。

---

## 💡 最值得记住的3句话

> **"Context windows are zero-sum."**
> 信息是有限的，要精准分配，不要什么都塞。

> **"I'm not watching terminals. The system tells me when to look."**
> 好系统是异常驱动的，不是轮询驱动的。

> **"Specialization through context, not through different models."**
> 分工的本质是信息隔离，不是模型差异。

---

## 🚀 下一步行动建议

如果老里想复刻这套系统（内容版）：

1. **建立 Context Hub** - 把历史文章、受众画像、写作风格整理成结构化文件
2. **定义完成标准** - 什么样的文章算"可发布"，写清楚
3. **设计可干预节点** - 每个关键步骤后有确认点，不要全自动
4. **主动扫描热点** - 让小知了每天早上推送3个选题候选

---

*深度解析时间：2026-02-24*
