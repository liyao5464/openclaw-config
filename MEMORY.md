# MEMORY.md - 长期记忆（硬限100行）

## 核心规则（每次都看）

- 发文章前必问：发主号还是实验室？不确定就问
- 排版前删掉"备用标题"，不能进正文
- HTML统一用 `scripts/md2html-pro.js ... wechat`
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
