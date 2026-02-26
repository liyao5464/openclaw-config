# 发布操作手册（冷存储）

> 从 MEMORY.md 移出，需要时 `read archive/publish-playbook.md`

## 标准发布流程

```bash
# 1. 转HTML（统一用 Wechat 主流风）
node scripts/md2html-pro.js articles/[文章].md wechat

# 2. 生封面图
bash scripts/gen-cover-smart.sh "文章标题" articles/[文章]-cover.png
# 或：bash scripts/gen-image.sh "简洁提示词" articles/[文章]-cover.png

# 3. 推微信草稿（主号）
export WECHAT_APP_ID="wxbde0f982acfe271b"
export WECHAT_APP_SECRET="a561d22a1227a810d66f13efa19bedb1"
npx -y bun /root/.openclaw/workspace/skills/baoyu-skills/skills/baoyu-post-to-wechat/scripts/wechat-api.ts \
  articles/[文章]-wechat.html \
  --cover /root/.openclaw/workspace/articles/[文章]-cover.png \
  --title "标题" --author "老里"

# 3b. 推微信草稿（小号）
export WECHAT_APP_ID="wx22983d127a8ee206"
export WECHAT_APP_SECRET="ea1ea206e7f690a3b87f153dabc56770"
# 其余命令同上
```

**注意：** md2html-pro.js 生成的文件后缀是 `-wechat.html`
