# OpenClaw 2026.2.17 发布：百万上下文、子代理命令、iOS分享扩展重磅上线

*Google 的 AI 助手平台又进化了，这次更新全是干货*

---

今天凌晨，OpenClaw 发布了 **2026.2.17** 版本。

作为一个几乎天天用 OpenClaw 的人，我第一时间翻了更新日志。不得不说，这次更新**全是硬货**——从百万 token 上下文支持，到全新的子代理命令系统，再到 iOS 分享扩展，每一个功能都打在痛点上。

让我带你快速过一遍这次更新的重点。

---

## 🧠 百万上下文支持：Claude Opus/Sonnet 正式支持 1M Token

**最重磅的更新：** Anthropic 的 Claude Opus 和 Sonnet 模型现在支持 **100万 token 的上下文窗口**了。

**这意味着什么？**

以前处理长文档，比如一本 300 页的技术手册，你得切成好几块分批处理。现在？直接整本扔进去，AI 能一次性读完、理解、回答。

**使用方式很简单：**
```json
{
  "model": "anthropic/claude-opus-4",
  "params": {
    "context1m": true
  }
}
```

设置 `context1m: true`，就会自动启用百万上下文能力。

**适用场景：**
- 代码库分析（整个项目的代码一次性理解）
- 法律文档审查（几百页的合同一次性处理）
- 学术研究（整篇论文+参考文献一起分析）
- 企业知识库（大量文档的统一查询）

---

## 🤖 全新子代理命令：/subagents spawn

**第二大亮点：** 现在可以用命令行直接 spawning 子代理了。

**以前 spawning 子代理：**
- 需要在对话里让 AI 调用工具
- 或者写配置文件

**现在：**
```bash
/subagents spawn --task "分析这个代码库的架构" --agentId "code-reviewer"
```

直接从聊天界面 spawning，**确定性更强**，不需要等 AI "决定"要不要 spawning。

**有什么用？**

比如你在做一个复杂项目，需要：
1. 一个子代理专门写前端代码
2. 一个子代理专门写后端 API
3. 一个子代理专门写测试

现在可以直接 spawning，**并行处理**，效率翻倍。

---

## 📱 iOS 分享扩展：从任何 App 直接分享到 OpenClaw

**iOS 用户的福音来了。**

这次更新加入了 **iOS Share Extension**，你可以：
- 在 Safari 看到一篇文章 → 点击分享 → 选择 OpenClaw → 直接发送给 AI 分析
- 在 Photos 看到一张图 → 点击分享 → 选择 OpenClaw → 让 AI 描述/分析
- 在 Files 看到一个 PDF → 点击分享 → 选择 OpenClaw → 直接让 AI 总结

**使用场景：**
- 看到好文章，直接分享给 OpenClaw 做笔记和总结
- 收到重要文档，直接分享给 OpenClaw 提取关键信息
- 浏览图片时，直接问 AI "这张图有什么问题？"

**不用再复制粘贴了，一键直达。**

---

## 💬 Slack 原生流式消息：终于支持打字机效果了

**Slack 用户等这个功能等太久了。**

以前 OpenClaw 在 Slack 里的回复是一次性弹出来的，体验有点割裂。

**现在：**
- 支持 **chat.startStream/appendStream/stopStream**
- AI 回复会像打字一样逐字出现
- 保留了回复线程对齐（replyToMode）

**体验提升巨大**，特别是在长回复场景，用户能看到 AI 正在 "思考"，而不是干等。

---

## 🔘 Telegram 内联按钮样式支持

**Telegram Bot 现在可以发更好看的按钮了。**

支持三种样式：
- `primary` - 主按钮（蓝色强调）
- `success` - 成功按钮（绿色）
- `danger` - 危险按钮（红色）

**使用示例：**
```json
{
  "buttons": [
    {"text": "确认", "callback_data": "confirm", "style": "success"},
    {"text": "取消", "callback_data": "cancel", "style": "danger"}
  ]
}
```

**用户体验大幅提升**，重要的操作可以用醒目的颜色区分。

---

## 🎮 Discord 功能大升级

Discord 支持这次也有很多改进：

### 1. 原生 /exec 命令选项
- 支持 `host`、`security`、`ask`、`node` 等参数的自动补全
- 不用记命令格式了，直接选就行

### 2. 可复用交互组件
- 设置 `components.reusable: true`
- 按钮、选择器、表单可以多次使用才过期

### 3. 按钮白名单
- 可以设置 `allowedUsers`，限制只有特定用户能点击按钮
- 适合需要权限控制的场景

---

## 🔧 大量细节优化和 Bug 修复

除了上面的大功能，这次更新还有 **100+ 项优化和修复**，挑几个实用的说：

### Cron 定时任务增强
- **Webhook 分离**：cron 任务可以通过 webhook 单独推送，不占用主会话
- **错峰执行**：支持设置 `staggerMs`，避免所有任务在同一秒触发
- **用量统计**：可以查看每个 cron 任务的 token 消耗

### 浏览器自动化
- 支持 `extraArgs` 配置 Chrome 启动参数
- 更灵活地控制浏览器行为

### 语音通话优化
- 预缓存问候语 TTS，首屏播放更快
- 修复媒体流断开时通话卡死的问题

### 安全修复
- 修复环境变量注入漏洞（OC-09）
- 加强配置文件的 `$include` 路径校验，防止目录遍历攻击

---

## 📊 版本更新数据

| 指标 | 数据 |
|-----|------|
| **新增功能** | 30+ 项 |
| **Bug 修复** | 100+ 项 |
| **社区贡献者** | 50+ 位 |
| **提交代码** | 4134875 |

---

## 🚀 如何升级

**一键升级：**
```bash
openclaw update
```

**或重新安装：**
```bash
npm install -g openclaw
```

**Docker 用户：**
```bash
docker pull openclaw/openclaw:latest
```

---

## 💡 我的使用建议

作为一个重度用户，我觉得这次更新有几个点特别值得关注：

1. **百万上下文**：如果你经常处理长文档，一定要试试 Claude Opus/Sonnet 的 1M 模式

2. **子代理命令**：复杂项目可以尝试 spawning 多个子代理并行工作，效率提升明显

3. **iOS 分享**：如果你是 iPhone 用户，这个分享扩展会改变你的工作流

4. **Slack 流式消息**：如果你用 Slack，更新后体验会好很多

---

## 写在最后

OpenClaw 这次更新让我看到了 Google 在这款产品上的投入——不是小修小补，而是**真正的生产力工具进化**。

百万上下文、子代理系统、跨平台分享，这些功能都在指向同一个方向：**让 AI 助手真正融入工作流，而不是一个独立的聊天窗口**。

如果你还没用过 OpenClaw，现在是个好时机。

如果你已经在用，赶紧升级体验新功能吧！

---

*原文发布时间：2026年2月18日*
*OpenClaw 版本：2026.2.17*
*GitHub Release：https://github.com/openclaw/openclaw/releases/tag/v2026.2.17*
