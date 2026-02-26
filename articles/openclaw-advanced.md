# OpenClaw 进阶指南：技能扩展、成本优化、自动化全攻略

*入门篇教你装好了 OpenClaw，这篇教你把它用到极致。*

---

用了一段时间 OpenClaw 之后，我开始觉得不够用了。

8 个分身跑起来了，记忆也配好了，但我想要更多：

- 能不能让 AI 帮我自动发推？
- 能不能每天早上自动给我发日程？
- 每个月 API 费用能不能少一点？

这篇文章，就是我折腾了几个月之后总结的进阶玩法。

---

## 第一章：技能市场 ClawHub——给 AI 装上超能力

OpenClaw 本身是个框架，真正的能力来自**技能（Skills）**。

ClawHub 是 OpenClaw 的官方技能市场，目前有超过 10,000 个技能。

官网：https://clawhub.com

### 怎么安装技能

```bash
# 先登录 ClawHub（不登录会限速）
clawhub login

# 安装技能
clawhub install 技能名称

# 卸载技能
clawhub uninstall 技能名称
```

### 我用过的好技能

**① X/Twitter 发帖：opentweet/x-poster**
```bash
clawhub install opentweet/x-poster
```
让 AI 帮你发推文、创建 thread、安排定时发布。

**② 浏览器自动化：playwright-mcp**
```bash
clawhub install playwright-mcp
```
让 AI 自动浏览网页、填表单、截图。功能强大，但要小心配置。

**③ Obsidian 知识库：obsidian-direct**
```bash
clawhub install obsidian-direct
```
把你的 Obsidian 笔记库变成 AI 的长期记忆。用 Obsidian 做笔记的朋友必装。

**④ GitHub 管理：github**
```bash
clawhub install github
```
管理代码仓库、审查 PR、自动 commit。开发者专属。

### ⚠️ 安全警告：不是所有技能都安全

2026 年 2 月发生过一次严重安全事件：

ClawHub 上排名第一的技能被发现是恶意软件，会**窃取 API 密钥和 SSH 凭证**。超过 1,184 个恶意技能被识别出来。

现在 ClawHub 已经和 VirusTotal 合作，会自动扫描。但你自己也要注意：

- ✅ 只装带 **Verified** 认证标志的技能
- ✅ 安装前看一眼代码，有没有可疑的 `curl | bash` 或 `sudo` 命令
- ✅ 一次只装一个，用几天确认没问题再装下一个
- ❌ 不要装来路不明的技能

调试技能出问题时：
```bash
openclaw logs --verbose
```

---

## 第二章：多模型路由——省钱 70% 的秘诀

很多人第一个月就烧了 $100+，因为所有任务都丢给最贵的模型。

其实没必要。

**核心原则：用对模型，不用最贵的。**

| 任务类型 | 推荐模型 | 原因 |
|---------|---------|------|
| 复杂推理、多步骤规划 | Claude Opus / GPT-4 | 需要强推理能力 |
| 日常对话、简单任务 | Claude Haiku / Kimi K2.5 | 够用，便宜 10 倍 |
| 文章写作、内容创作 | Claude Sonnet | 性价比之王 |
| 文件整理、格式转换 | MiniMax M2.5 | 快且便宜 |

### 怎么配置多模型路由

在 `~/.openclaw/openclaw.json` 里设置 primary + fallbacks：

```json
{
  "agents": {
    "defaults": {
      "model": {
        "primary": "minimax/MiniMax-M2.5",
        "fallbacks": [
          "anyrouter/claude-sonnet-4-6",
          "kimi-coding/k2p5"
        ]
      }
    }
  }
}
```

**我的策略：**
- 默认用 MiniMax（便宜）
- 需要高质量输出时手动切换到 Sonnet
- 复杂分析才用 Opus

一个月下来，API 费用比之前少了一大半。

---

## 第三章：CRON 自动化——让 AI 主动干活

OpenClaw 最强大的地方不是被动回答问题，而是**主动执行任务**。

CRON 就是让 AI 按时间表自动工作的机制。

### 常见自动化场景

**① 每天早上发日程**
```
每天 8:00 → 检查今日日程 → 发 Telegram 提醒
```

**② 每周五总结**
```
每周五 17:00 → 总结本周进展 → 发给我看
```

**③ 每晚压缩记忆**
```
每晚 23:00 → 运行 memory compact → 节省 token
```

### 怎么设置 CRON

在 OpenClaw Dashboard 里点几下就能设置，比手动 cron 更智能。

或者直接告诉 AI：

> "每天早上 8 点提醒我今天的待办事项"

AI 会自动帮你创建 CRON 任务。

### Heartbeat 频率

Heartbeat 是 AI 定期检查是否有事情要做的机制。

**建议设置 30-60 分钟。**

设成 5 分钟会让 API 费用飙升，大部分时候没必要那么频繁。

---

## 第四章：成本监控——防止 AI 偷偷烧钱

有人半夜被 Claude Opus 烧了几百刀，早上起来看账单差点哭出来。

这种事完全可以避免。

### 三道防线

**第一道：API 平台设置每日上限**

在 Anthropic / OpenAI 控制台设置每日消费上限。

建议：测试阶段 $5/天，稳定使用后再调高。

**第二道：安装 ClawWatcher**

```bash
clawhub install clawwatcher
```

实时监控每个模型花了多少钱，可设每日硬上限。

超过上限自动暂停，不会继续烧钱。

**第三道：定期 compact 记忆**

```bash
openclaw compact
```

每周运行一次，把长对话压缩成摘要。

对话越长，每次调用消耗的 token 越多。定期压缩能省 30-50% 的费用。

---

## 第五章：安全加固——别让 AI 变成漏洞

OpenClaw 能执行系统命令，配置不当会有安全风险。

### SOUL.md 必须有安全边界

```markdown
## 安全边界（重要！）

- 修改 .env 或 credentials/ 文件夹前必须经过我的二次确认
- 单笔超过 $50 的操作必须获得我的"Y"确认
- 永远不要在没有预览的情况下执行 rm 命令
- 不要在我睡觉时间（23:00-07:00）发送非紧急通知
```

**"永远不要做"清单非常重要。** 写清楚边界，AI 才不会越界。

### 不要暴露到公网

```bash
# ✅ 正确：只在本地运行
bind: "loopback"  # 127.0.0.1

# ❌ 错误：暴露到公网
bind: "0.0.0.0"
```

如果需要远程访问，用 **Tailscale**，不要直接开放端口。

### 定期更新

```bash
openclaw update
```

每周运行一次。OpenClaw 更新很快，经常修补安全漏洞，别用老版本。

---

## 第六章：进阶踩坑——我交过的学费（续）

### 坑一：Heartbeat 设太短，一个月烧 $200

Heartbeat 设成了 5 分钟，AI 每 5 分钟就调用一次模型检查有没有事情做。

一个月下来，光 Heartbeat 就烧了 $200。

**教训：Heartbeat 设 30-60 分钟，够用了。**

### 坑二：装了恶意技能，API Key 被盗

从 ClawHub 装了一个看起来很好用的技能，结果是恶意软件。

API Key 被盗，被人用来调用模型，账单飙升。

**教训：只装 Verified 技能，装之前看一眼代码。**

### 坑三：没有备份 workspace，服务器崩了全没了

服务器出问题，workspace 里的所有配置、记忆、对话历史全没了。

重新配置花了两天。

**教训：定期备份 `~/.openclaw/workspace/` 到云端。**

### 坑四：技能版本不兼容

OpenClaw 更新后，之前装的某个技能突然不工作了。

**教训：技能出问题先去它的 GitHub 页面看 issue，通常有人已经报告了。**

---

## 结尾

从入门到进阶，OpenClaw 的学习曲线确实有点陡。

但一旦配好了，它真的能帮你省很多时间。

我现在每天花在重复性工作上的时间，比以前少了一大半。

**学习路径建议：**

1. 先把入门篇的基础配好，跑稳了
2. 再装 1-2 个技能，感受一下扩展能力
3. 配置多模型路由，开始省钱
4. 设置几个 CRON 任务，让 AI 主动干活
5. 最后做安全加固，放心用

不要跳步，每个阶段扎实了再进入下一阶段。

---

*觉得有用，转发给你身边那个正在折腾 OpenClaw 的朋友。*

*入门篇在这里：《OpenClaw 保姆级教程：从安装到 8 个 AI 分身，一篇搞定》*

