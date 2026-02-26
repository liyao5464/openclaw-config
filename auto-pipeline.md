# 一键内容自动化流水线

## 触发命令

```
写文章：[选题]
```

## 完整流程（9步）

```
Step 1: 写稿
  → style-agent.md 风格指令
  → 输出：articles/[slug].md

Step 2: QC检查
  → qc-agent.md 质检
  → FAIL → 打回重写（最多2次）
  → PASS → 继续

Step 3: Markdown格式化
  → baoyu-format-markdown
  → 输出：articles/[slug]-formatted.md

Step 4: 生成封面图
  → baoyu-cover-image articles/[slug].md --quick --aspect 16:9 --lang zh
  → 输出：articles/[slug]-cover.png

Step 5: 生成文章配图
  → baoyu-article-illustrator articles/[slug].md --quick
  → 输出：articles/[slug]-img-*.png

Step 6: 压缩图片
  → baoyu-compress-image articles/[slug]-*.png
  → 输出：WebP格式，减小体积

Step 7: Markdown转HTML
  → baoyu-markdown-to-html articles/[slug]-formatted.md
  → 主题：Grace（暖棕色系）
  → 输出：articles/[slug].html

Step 8: 发布微信公众号
  → baoyu-post-to-wechat articles/[slug].html
  → 封面：articles/[slug]-cover.png
  → 状态：草稿（不自动发布，等老里确认）

Step 9: 通知老里
  → Telegram 发送：文章标题 + 封面图 + 微信草稿链接
```

---

## 各步骤详细参数

### Step 4: 封面图
```
baoyu-cover-image [article.md] \
  --quick \
  --aspect 16:9 \
  --lang zh \
  --palette warm \
  --rendering flat-vector \
  --text title-subtitle
```

### Step 5: 文章配图
```
baoyu-article-illustrator [article.md] \
  --quick \
  --style warm \
  --count 2
```

### Step 7: HTML转换
```
baoyu-markdown-to-html [article.md] \
  --theme grace
```

### Step 8: 发布微信
```
baoyu-post-to-wechat [article.html] \
  --cover [cover.png] \
  --author 老里 \
  --draft
```

---

## 文件命名规范

| 文件 | 命名 |
|------|------|
| 原始草稿 | `articles/YYYY-MM-DD-[slug].md` |
| 格式化版 | `articles/YYYY-MM-DD-[slug]-formatted.md` |
| 封面图 | `articles/YYYY-MM-DD-[slug]-cover.webp` |
| 配图 | `articles/YYYY-MM-DD-[slug]-img-1.webp` |
| HTML | `articles/YYYY-MM-DD-[slug].html` |

---

## 异常处理

| 情况 | 处理 |
|------|------|
| QC连续2次FAIL | 通知老里人工介入 |
| 封面图生成超时 | 用 gen-image.sh 备用方案 |
| 微信发布失败 | 保存HTML，通知老里手动发 |
| 任意步骤报错 | 停止流水线，报告卡在哪一步 |
