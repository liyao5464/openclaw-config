# MEMORY.md - 长期记忆

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

## 其他重要记忆

（待补充...）
