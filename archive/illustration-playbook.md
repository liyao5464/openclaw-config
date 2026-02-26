# 配图流程（冷存储）

> 从 MEMORY.md 移出，触发词"配图"时读取

## 触发方式
写完文章后说"配图"，走完整流程。

## 流程
1. 用 `baoyu-article-illustrator` 技能分析文章
2. EXTEND.md 偏好：notion 风格、中文、输出到 `./illustrations`
3. 生成 outline（4张）让老里确认
4. 批量生图（用 `gen-image.sh` + awk 跳过 frontmatter）
5. 嵌入文章对应位置

## 关键命令
```bash
PROMPT=$(awk '/^---/{p++; next} p>=2{print}' prompts/illustration-0N.md | tr '\n' ' ' | xargs)
bash scripts/gen-image.sh "$PROMPT" "illustrations/slug/NN-type-name.png"
```

## 生图配置
- 服务：Labnana (Gemini图片生成代理)
- 端点：`https://api.labnana.com/openapi/v1/images/generation`
- 模型：`gemini-3-pro-image-preview`
- 脚本：`scripts/gen-image.sh`
- 支持宽高比：1:1 / 16:9 / 9:16 / 4:3 / 3:4
- 积分：1K=15分，2K=15分，4K=30分
- 同步返回base64，不用轮询
