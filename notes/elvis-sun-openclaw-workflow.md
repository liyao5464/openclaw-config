# Elvis Sun OpenClaw 工作流深度解析

**原文：** https://x.com/elvissun/article/2025920521871716562  
**作者：** Elvis Sun (@elvissun)  
**时间：** 2026年2月

---

## 🎯 核心成果

| 指标 | 数据 |
|------|------|
| 单日最高提交 | **94 commits** |
| 平均日提交 | **50 commits** |
| 30分钟完成 | **7 个 PR** |
| 月成本 | Claude $100 + Codex $90（可降至$20起步）|
| 成功率 | 中小任务**一次性完成**，无需干预 |

---

## 🏗️ 系统架构：双层架构

```
┌─────────────────────────────────────────────────────────┐
│  层1: Orchestrator (OpenClaw)                           │
│  - Zoe: 编排器，持有业务上下文                           │
│  - 职责：拆解任务、写Prompt、选模型、监控、通知          │
│  - Context: Obsidian Vault (客户数据、会议记录、历史决策) │
└─────────────────────────────────────────────────────────┘
                            ↓ 精确Prompt
┌─────────────────────────────────────────────────────────┐
│  层2: Coding Agents (Codex/Claude/Gemini)               │
│  - 职责：专注编码，不接触业务上下文                      │
│  - Context: 仅代码 + Orchestrator给的精简上下文          │
└─────────────────────────────────────────────────────────┘
```

**关键洞察：** Context Windows 是零和博弈
- 塞满代码 → 没有业务上下文空间
- 塞满客户历史 → 没有代码空间
- **解决方案：** 两层分离，各取所需

---

## 🔄 8步工作流

### Step 1: 需求拆解 (Scoping)
**与 Zoe 对话确定范围**

- 客户电话后，直接与 Zoe 讨论需求
- Zoe 自动读取 Obsidian 中的会议笔记
- 共同确定功能方案

**Zoe 自动执行3件事：**
1. **充值 credits** - 有 admin API 访问权限
2. **拉取客户配置** - 只读生产数据库访问（Coding Agent 永远没有这个权限）
3. **Spawn Codex Agent** - 生成详细 Prompt

---

### Step 2: Spawn Agent

**每个 Agent 的隔离环境：**
```bash
# 创建独立 worktree + 分支
git worktree add ../feat-custom-templates -b feat/custom-templates origin/main
cd ../feat-custom-templates && pnpm install

# 启动 tmux 会话
tmux new-session -d -s "codex-templates" \
  -c "/Users/elvis/Documents/GitHub/medialyst-worktrees/feat-custom-templates" \
  "$HOME/.codex-agent/run-agent.sh templates gpt-5.3-codex high"
```

**为什么选择 tmux 而不是 `codex exec`？**

**tmux 的超能力：中途重定向**
```bash
# Agent 方向错了？不用杀死，直接纠正
tmux send-keys -t codex-templates "Stop. Focus on the API layer first, not the UI." Enter

# 需要更多上下文？
tmux send-keys -t codex-templates "The schema is in src/types/template.ts. Use that." Enter
```

---

### Step 3: 任务追踪

**JSON 注册表：** `.clawdbot/active-tasks.json`

```json
{
  "id": "feat-custom-templates",
  "tmuxSession": "codex-templates",
  "agent": "codex",
  "description": "Custom email templates for agency customer",
  "repo": "medialyst",
  "worktree": "feat-custom-templates",
  "branch": "feat/custom-templates",
  "startedAt": 1740268800000,
  "status": "running",
  "notifyOnComplete": true
}
```

完成后更新：
```json
{
  "status": "done",
  "pr": 341,
  "completedAt": 1740275400000,
  "checks": {
    "prCreated": true,
    "ciPassed": true,
    "claudeReviewPassed": true,
    "geminiReviewPassed": true
  },
  "note": "All checks passed. Ready to merge."
}
```

---

### Step 4: 循环监控 (10分钟 Cron)

**脚本：** `.clawdbot/check-agents.sh`

**设计原则：** 100% 确定性，极度省 Token

**检查项：**
- tmux 会话是否存活
- 追踪分支是否有 open PR
- CI 状态 (via `gh cli`)
- 自动重试失败 Agent（最多3次）
- **只在需要人工干预时通知**

> "I'm not watching terminals. The system tells me when to look."

---

### Step 5: Agent 创建 PR

**Agent 执行：**
```bash
git commit -m "..."
git push
gh pr create --fill
```

**此时不通知人** —— PR 创建 ≠ 完成

---

### Step 6: 三AI代码审核

**每个 PR 必须经过3个 Reviewer：**

| Reviewer | 专长 | 评价 |
|----------|------|------|
| **Codex Reviewer** | 边界情况、逻辑错误、竞态条件 | "Exceptional at edge cases. False positive rate is very low." |
| **Gemini Code Assist** | 安全问题、扩展性问题 | "Free and incredibly useful. No brainer to install." |
| **Claude Code Reviewer** | 过度谨慎 | "Mostly useless. Lots of 'consider adding...' overengineering. Skip unless critical." |

---

### Step 7: 自动化测试

**CI Pipeline：**
- Lint + TypeScript
- Unit tests
- E2E tests
- Playwright tests（预览环境，与生产一致）

**新增规则：** UI 变更必须包含截图，否则 CI 失败

---

### Step 8: 人工审核 → Merge

**收到 Telegram 通知：**
> "PR #341 ready for review."

**此时状态：**
- ✅ CI 通过
- ✅ 三AI审核通过
- ✅ UI 截图已提供
- ✅ 边界情况已在 Review Comment 中记录

**人工审核时间：** 5-10分钟

> "Many PRs I merge without reading the code — the screenshot shows me everything I need."

---

## 🧠 关键方法论

### 1. Ralph Loop 升级版

**传统 Ralph Loop：**
```
记忆 → 生成 → 评估 → 保存
```
问题：Prompt 静态，只改进检索

**Elvis 升级版：**
```
失败 → Zoe 用业务上下文分析 → 改写 Prompt → 重试
```

**示例：**
- Context 用完？→ "Focus only on these three files."
- 方向错了？→ "Stop. The customer wanted X, not Y."
- 需要澄清？→ "Here's customer's email..."

### 2. 主动工作 (Proactive)

Zoe **不等人分配任务**，自动找活干：

| 时间 | 触发 | 动作 |
|------|------|------|
| 早上 | Scan Sentry | 发现4个新错误 → spawn 4 agents |
| 会后 | Scan 会议笔记 | 发现3个feature需求 → spawn 3 Codex agents |
| 晚上 | Scan git log | spawn Claude 更新 changelog |

> "I take a walk after a customer call. Come back to Telegram: '7 PRs ready for review.'"

### 3. 强化学习循环

**奖励信号：**
- ✅ CI passing
- ✅ 三代码审核通过
- ✅ 人工 merge

**失败触发学习：**
- 记录成功模式："This prompt structure works for billing features."
- 记录失败教训："Codex needs the type definitions upfront."
- 持续优化 Prompt

---

## 🤖 Agent 分工策略

| Agent | 最佳场景 | 占比 |
|-------|----------|------|
| **Codex** | 后端逻辑、复杂bug、多文件重构 | 90% |
| **Claude Code** | 前端工作、git操作 | 少量 |
| **Gemini** | UI设计（生成HTML/CSS spec） | 设计任务 |

**路由策略：**
- Billing bug → Codex
- Button style fix → Claude
- New dashboard design → Gemini → Claude

---

## 💰 成本与瓶颈

### 当前成本
- Claude: ~$100/month
- Codex: ~$90/month
- **可起步于 $20**

### 当前瓶颈：RAM

**问题：**
- 每个 agent 需要独立 worktree
- 每个 worktree 有自己的 `node_modules`
- 5个并行 agent = 5个 TypeScript 编译器 + 5个测试运行器

**现状：**
- Mac Mini 16GB → 最多 4-5 agents（会 swap）

**解决方案：**
- 购买 Mac Studio M4 Max 128GB ($3,500)
- 3月底到货

---

## 🔧 可复用的技术细节

### Git Worktree 隔离
```bash
git worktree add ../feat-branch -b feat/feature origin/main
```

### Tmux 会话管理
```bash
# 创建
tmux new-session -d -s "agent-name" -c "/path/to/worktree" "command"

# 发送指令（不杀死 agent）
tmux send-keys -t agent-name "your command" Enter
```

### Cron 监控脚本设计
- 100% 确定性
- 极低 Token 消耗
- 只在需要时通知

---

## 🚀 对老里的启示

### 立即可用

1. **双层架构** - OpenClaw 管业务，Agent 管执行
2. **Obsidian 作为 Context Hub** - 会议笔记、客户数据、历史决策
3. **tmux 而非 exec** - 可中途干预，不杀死 agent
4. **JSON 任务注册表** - 追踪状态，Cron 扫描
5. **三AI审核** - Codex(逻辑) + Gemini(安全) + Claude(保守验证)

### 需要权衡

- **成本：** $190/month 对老里可能偏高
- **复杂度：** 需要维护 worktree、tmux、cron
- **适用性：** Elvis 是工程场景，老里是内容创作

### 适配建议

**内容创作场景可借鉴：**
- **Orchestrator (小知了)** - 持有老里的风格记忆、历史文章
- **Research Agent** - 抓取素材、整理观点
- **Writer Agent** - 生成初稿
- **Reviewer Agent** - 检查风格、敏感词
- **tmux 模式** - 可中途纠正方向（"这段太学术，改口语"）

---

## 📌 金句摘录

> "Context windows are zero-sum. You have to choose what goes in."

> "I'm not watching terminals. The system tells me when to look."

> "The next generation of entrepreneurs won't hire a team of 10 to do what one person with the right system can do."

> "There's so much AI-generated slop right now. I'm trying to do the opposite: less hype, more documentation of building an actual business."

> "Real customers, real revenue, real commits that ship to production, and real loss too."

---

## 🔗 相关概念

- **Stripe Minions** - Stripe 的并行编码 agent 系统（背景编排层）
- **Ralph Loop** - 记忆→生成→评估→学习的循环
- **Agentic PR** - Elvis 正在做的产品：用 agents 帮初创公司做 PR

---

*整理时间：2026-02-24*  
*整理者：小知了*
