# MEMORY.md - 长期记忆

## 发布规则（重要）

- **排版发布前必须删除"备用标题"部分**，不能让备用标题进入正文
- 文章结构要有老里自己的视角和经历，不能照搬原文结构，避免抄袭感
- **HTML转换统一用 `scripts/md2html-pro.js`（Wechat主流风，红棕色标题下划线，全内联样式）**
- 封面图用 `scripts/gen-image.sh`，提示词要简洁（太复杂会超时）
- **双账号统一排版：主号和小号都用 Wechat 主流风（2026-02-25更新）**

## 标准发布流程（每次都这样）

```bash
# 1. 转HTML（统一用 Wechat 主流风）
node scripts/md2html-pro.js articles/[文章].md wechat

# 2. 生封面图（智能文件夹风格 - 推荐）
bash scripts/gen-cover-smart.sh "文章标题" articles/[文章]-cover.png
# 或者传统方式：
# bash scripts/gen-image.sh "简洁提示词" articles/[文章]-cover.png

# 3. 推微信草稿
export WECHAT_APP_ID="wxbde0f982acfe271b"
export WECHAT_APP_SECRET="a561d22a1227a810d66f13efa19bedb1"
npx -y bun [wechat-api.ts路径] articles/[文章]-wechat.html \
  --cover /root/.openclaw/workspace/articles/[文章]-cover.png \
  --title "标题" --author "老里"
```

wechat-api.ts路径：`/root/.openclaw/workspace/skills/baoyu-skills/skills/baoyu-post-to-wechat/scripts/wechat-api.ts`

**注意：** md2html-pro.js 生成的 HTML 文件后缀是 `-wechat.html`，推送时注意路径

## 双账号配置

| 账号 | 定位 | AppID | AppSecret |
|------|------|-------|-----------|
| 主号（老里） | AI科普、深度分析 | wxbde0f982acfe271b | a561d22a1227a810d66f13efa19bedb1 |
| 小号（老里的AI实验室） | AI工作流、内容创作工具 | wx22983d127a8ee206 | ea1ea206e7f690a3b87f153dabc56770 |

**发布时区分规则：**
- 用户说"发主号" / 文章是深度科普类 → 用主号配置
- 用户说"发实验室" / 文章是工作流/工具类 → 用小号配置
- 不确定时主动问清楚再发

---

## 微信公众号发布配置（已验证成功）

**最后更新：** 2026-02-18
**验证状态：** ✅ 已成功发布文章

### 发布方法

使用 baoyu-post-to-wechat 技能的 wechat-api.ts 脚本：

```bash
cd /root/.openclaw/workspace
export WECHAT_APP_ID="wxbde0f982acfe271b"
export WECHAT_APP_SECRET="a561d22a1227a810d66f13efa19bedb1"
npx -y bun /root/.openclaw/workspace/skills/baoyu-skills/skills/baoyu-post-to-wechat/scripts/wechat-api.ts \
  article.html \
  --cover cover.jpg \
  --title "文章标题" \
  --author "老里"
```

### 关键要点

1. **必须 export 环境变量** - 不能只定义，要 export
2. **封面图要求** - 900×383px, jpg/png, <2MB
3. **HTML格式** - 使用微信兼容模板（内联样式）
4. **账号类型** - 当前是订阅号+未认证，但API模式可用（可能是历史遗留权限）

### 成功发布的文章

- 2026-02-17: 春晚AI文章
- 2026-02-18: Matt Shumer深度分析文章
  - Media ID: cnuaTfbBU2-yDTsbxIRQFA11Lr4Ll9RKwHVkioJHHToLr_dLTUS5hS4bA3he-8p0

### 常用路径

| 文件/目录 | 路径 |
|----------|------|
| 发布脚本 | `/root/.openclaw/workspace/skills/baoyu-skills/skills/baoyu-post-to-wechat/scripts/wechat-api.ts` |
| 技能配置 | `~/.baoyu-skills/.env` |
| Token缓存 | `~/.baoyu-skills/access_token.json` |
| 文章存放 | `/root/.openclaw/workspace/` |

### 常见问题

**Q: 提示 access_token expired?**
```bash
rm ~/.baoyu-skills/access_token.json
```

**Q: 封面图上传失败?**
- 检查尺寸 900×383
- 检查格式 jpg/png
- 检查大小 <2MB

---

## 文章配图流程（已验证）

**配置时间：** 2026-02-26
**状态：** ✅ 已验证可用

### 触发方式
写完文章后说"配图"，我来走完整流程。

### 流程
1. 用 `baoyu-article-illustrator` 技能分析文章
2. EXTEND.md 偏好：notion 风格、中文、输出到 `./illustrations`
3. 生成 outline（4张：总览 + 章节对比 + 决策流程）让老里确认
4. 批量生图（用 `gen-image.sh` + awk 跳过 frontmatter）
5. 嵌入文章对应位置

### 关键命令
```bash
# 生图（跳过 frontmatter）
PROMPT=$(awk '/^---/{p++; next} p>=2{print}' prompts/illustration-0N.md | tr '\n' ' ' | xargs)
bash scripts/gen-image.sh "$PROMPT" "illustrations/slug/NN-type-name.png"
```

### 输出目录
`illustrations/{topic-slug}/` — outline.md + prompts/ + 图片文件

**配置时间：** 2026-02-24
**状态：** ✅ 已验证可用

- 端点：`https://dashscope.aliyuncs.com/api/v1/services/aigc/multimodal-generation/generation`
- 模型：`wan2.6-t2i`
- API Key：`sk-a0a58e7d5a1f46a08d1884c84c1bfc96`
- 生图脚本：`/root/.openclaw/workspace/scripts/gen-image.sh`
- 用法：`bash scripts/gen-image.sh "提示词" 输出文件.png`
- 注意：提示词不要太复杂，容易超时；同步调用，不用异步

## 内容生产流水线

**配置时间：** 2026-02-24
**文件：** `workspace/content-pipeline.md`

流程：写稿 → QC → 生图 → 通知老里

关键文件：
- `style-agent.md` — 风格守护者
- `qc-agent.md` — 质检员
- `scripts/gen-image.sh` — 生图脚本
- `articles/` — 文章存放目录

触发方式：发给小知了"写文章：[选题]"
