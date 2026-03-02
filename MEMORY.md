# MEMORY.md - 长期记忆（硬限100行）

## 核心规则（每次都看）

- 发文章前必问：发主号还是实验室？不确定就问
- 排版前删掉"备用标题"，不能进正文
- HTML转换：使用 baoyu-post-to-wechat 技能自动处理
- 封面提示词要简洁，太复杂会超时
- 写文章前必读 `writing-guide.md` + `style-agent.md`

## 双账号

| 账号 | AppID | AppSecret |
|------|-------|-----------|
| 主号 | wxbde0f982acfe271b | a561d22a1227a810d66f13efa19bedb1 |
| 小号 | wx22983d127a8ee206 | ea1ea206e7f690a3b87f153dabc56770 |

主号=AI科普深度分析 / 小号=工作流工具类

## 写作风格索引

- 风格文件：`style-agent.md` + `writing-guide.md`
- 核心：接地气技术布道者，朋友聊天语气
- 开头："大家好，我是老里"，50-100字切入
- 结尾：固定"感恩三连"模板
- 禁止：书面腔、被动句、AI味、说教

## 知识库索引（按需加载）

> 详细内容见 `memory/INDEX.md`，启动时扫描导航，按需读子文件。

| 类型 | 路径 | 说明 |
|------|------|------|
| 人物画像 | `memory/people/laoli-profile.md` | 老里基本信息 |
| 用户偏好 | `memory/preferences/laoli-preferences.md` | 写作风格+禁止项 |
| 发布经验 | `memory/lessons/wechat-publishing.md` | 流程+踩坑 |
| 写作方法论 | `memory/lessons/writing-methodology.md` | 结构+标题公式 |
| 记忆架构 | `memory/lessons/openclaw-memory-arch.md` | Token优化 |
| 双账号决策 | `memory/decisions/2026-02-14-dual-accounts.md` | 账号配置 |

## 冷存储索引（用到再读）

| 内容 | 路径 |
|------|------|
| 发布完整命令 | `archive/publish-playbook.md` |
| 发布配置详情 | `archive/publish-config.md` |
| 配图流程 | `archive/illustration-playbook.md` |
| ePro方法论 | `archive/epro-memory-guide.md` |
| 心跳/群聊规则 | `archive/heartbeat-groupchat-rules.md` |

## 踩坑记录（防重犯）

- ❌ 发错号（主号发成实验室）
- ❌ 封面提示词太复杂→超时
- ❌ 忘删备用标题→发布失败
- ❌ 上下文压缩导致指令丢失

## 操作铁律（强制执行，不可违反）

### 1. openclaw.json 修改三步铁律
- 改前备份（带时间戳）：`cp openclaw.json openclaw.json.bak.$(date +%Y%m%d%H%M%S)`
- 改前查文档确认字段合法值
- 改后双验证：JSON解析 + `openclaw doctor`，通过后才能重启

### 2. 禁止危险重启
- ❌ 禁止先 kill 前台 gateway 再 systemd start
- ❌ 禁止 stop+start 快速连击
- ✅ 优先用 `openclaw gateway restart`，校验通过后执行

### 3. 禁止猜命令/猜配置
- 不熟悉的命令先查文档或 `--help`
- 配置字段不靠猜，必须按 schema

### 4. 给选项后必须等确认
- 不可擅自拍板执行未经老里确认的方案

### 5. 密钥安全铁律
- ❌ 不在输出里暴露任何密钥
- 所有密钥通过 1Password `op` 读取
- 示例只用占位符，不写真值

### 6. 1Password SSH 调用铁律
- 所有 op 相关操作必须在 tmux 里跑
- 私钥只进 ssh-agent，不落盘
- 连接服务器统一走 1P op 取密钥

### 7. 代码/生产变更流程
- 本地改 → 测试 → commit → 老里确认 → 再推送/部署
- ❌ 不直接在线服务器改核心代码
