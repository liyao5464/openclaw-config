# 配图流程（冷存储）

> 从 MEMORY.md 移出，触发词"配图"时读取

## 触发方式
写完文章后说"配图"，走完整流程。

## 流程
1. 用 `baoyu-article-illustrator` 技能分析文章
2. 风格偏好：**简笔插画式知识图**（见下方风格说明），中文，输出到 `./illustrations`
3. 生成 outline（4张）让老里确认
4. 批量生图（用 `gen-image.sh` + awk 跳过 frontmatter）
5. 嵌入文章对应位置

## 插图风格说明（简笔插画式知识图）

**核心特征：**
- 白底黑线，手绘感线条
- 简单小人/图标代替复杂写实图片
- 箭头连接概念，逻辑一眼看懂
- 局部点缀淡色（不超过3色），不花哨
- 中文标注清晰可读，扁平设计

**Prompt 模板：**
```
简笔插画风格知识图，手绘感，白底，黑色线条，[具体内容描述]，包含简单小人图标、箭头连接、中文标注，清晰可读的中文文字，扁平设计，教育信息图风格
```

**宽高比建议：**
- 文章配图：16:9
- 封面：16:9（900×383px）
- 正文插图：4:3 或 1:1

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
