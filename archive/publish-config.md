# 微信公众号发布配置（详细版）

> 从 MEMORY.md 移出的冷存储

## 发布要点

1. **必须 export 环境变量** - 不能只定义，要 export
2. **封面图要求** - 900×383px, jpg/png, <2MB
3. **HTML格式** - 使用微信兼容模板（内联样式）
4. **账号类型** - 订阅号+未认证，API模式可用

## 常用路径

| 文件/目录 | 路径 |
|----------|------|
| 发布脚本 | `skills/baoyu-skills/skills/baoyu-post-to-wechat/scripts/wechat-api.ts` |
| 技能配置 | `~/.baoyu-skills/.env` |
| Token缓存 | `~/.baoyu-skills/access_token.json` |
| 文章存放 | `articles/` |

## 常见问题

**Q: access_token expired?**
```bash
rm ~/.baoyu-skills/access_token.json
```

**Q: 封面图上传失败?**
- 检查尺寸 900×383、格式 jpg/png、大小 <2MB

## 历史发布记录

- 2026-02-17: 春晚AI文章
- 2026-02-18: Matt Shumer深度分析
- 2026-02-25: ePro-Memory文章
- 2026-02-26: NotebookLM教程、ePro-Memory（含配图版）
