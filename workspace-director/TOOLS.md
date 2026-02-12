# TOOLS.md - 内容总监的工具箱

## 已配置技能

### 1. 发布公众号 (baoyu-post-to-wechat)
**用途**：将文章发布到微信公众号
**支持**：
- Markdown → HTML 自动转换
- 多主题样式（default/grace/simple）
- API模式（快速）或浏览器模式（稳定）
- 图文消息（最多9张图）

**使用方法**：
```bash
# 文章模式（推荐）
npx -y bun /root/.openclaw/workspace/skills/baoyu-skills/skills/baoyu-post-to-wechat/scripts/wechat-article.ts --html <html文件>

# 图文模式
npx -y bun /root/.openclaw/workspace/skills/baoyu-skills/skills/baoyu-post-to-wechat/scripts/wechat-browser.ts --markdown <md文件> --images <图片目录>
```

**发布流程**：
1. 用户提供Markdown/文章
2. 转换为HTML（选择主题）
3. 提取标题、摘要、封面图
4. 发布到公众号草稿箱
5. 返回管理链接

**配置状态**：✅ 已配置API密钥（2026-02-12）
- AppID: wxbde0f982acfe271b
- 使用模式：**API模式（快速）**

**发布方式选择**：
- **API模式（推荐）**：直接调用微信API，无需浏览器，速度快
- 浏览器模式：需要Chrome，扫码登录（备用）

**图片处理**：自动压缩和上传至微信服务器

### 2. 文章配图生成 (baoyu-image-gen)
**用途**：生成文章封面图和插图
**API**：FAL (xAI Grok Imagine)
**配置**：已设置FAL_KEY

### 3. Markdown转HTML (baoyu-markdown-to-html)
**用途**：将Markdown转换为公众号可用的HTML
**主题**：default / grace / simple

### 4. 去AI味 / Humanize (humanizer)
**用途**：将AI生成的内容转化为更自然、更有人情味的文字
**核心能力**：
- 去除AI腔：删除"首先/其次/综上所述"等机械连接词
- 增加口语化：加入"说实话"、"其实"、"我觉得"等自然表达
- 加入个人色彩：增加主观感受、情绪变化、小故事
- 打破完美结构：允许段落长短不一，不强行对称
- 增加细节描写：具体的场景、动作、感受，而非抽象概念

**去AI味检查清单**：
- [ ] 开头是否有钩子（而非"随着XX的发展"）
- [ ] 是否有个人故事或具体案例
- [ ] 是否有情绪表达（而非纯客观陈述）
- [ ] 连接词是否自然（而非机械罗列）
- [ ] 结尾是否有温度（而非标准总结）

**使用方法**：
直接在对话中说"去一下AI味"或"humanize这篇文章"，我会自动处理。

**参考风格**：
- 像朋友聊天，而非工作报告
- 有瑕疵但真实，而非完美但冰冷
- 有情绪起伏，而非平铺直叙

### 5. 文件发送 (Telegram)
**用途**：向用户发送文件、图片、文档
**支持类型**：
- Markdown文件 (.md)
- HTML文件 (.html)
- 图片 (.jpg/.png/.webp)
- PDF文档 (.pdf)
- 其他任意文件

**使用方法**：
使用 `message` 工具发送文件：
```json
{
  "action": "send",
  "media": "/path/to/file.md",
  "target": "8404273573"
}
```

**常见场景**：
- 生成文章后发送Markdown文件给用户
- 发送公众号HTML文件预览
- 发送配图、封面图
- 发送文章备份文件

**注意**：
- 文件路径必须是绝对路径
- 发送前确认文件存在
- 大文件可能需要压缩
