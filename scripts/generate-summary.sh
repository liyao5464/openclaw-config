#!/bin/bash
# generate-summary.sh - 自动生成文章摘要
# 用法: ./generate-summary.sh <文章路径>

if [ $# -lt 1 ]; then
    echo "Usage: $0 <article-path>"
    echo "Example: $0 articles/my-post.md"
    exit 1
fi

ARTICLE="$1"
BASENAME=$(basename "$ARTICLE" .md)
DIR=$(dirname "$ARTICLE")

# 检查文件是否存在
if [ ! -f "$ARTICLE" ]; then
    echo "❌ 错误: 文件不存在 $ARTICLE"
    exit 1
fi

# 提取标题
TITLE=$(grep -m1 "^# " "$ARTICLE" | sed 's/^# //')

# 提取正文内容（去掉标题和空行）
CONTENT=$(grep -v "^#" "$ARTICLE" | grep -v "^$" | head -20)

# 统计字数
WORD_COUNT=$(wc -m < "$ARTICLE")

# 生成摘要文件
SUMMARY_FILE="${DIR}/${BASENAME}-summary.md"

cat > "$SUMMARY_FILE" << EOF
# 文章摘要: ${TITLE}

**原文**: ${ARTICLE}
**字数**: ${WORD_COUNT} 字
**生成时间**: $(date '+%Y-%m-%d %H:%M')

---

## 一句话总结

$(echo "$CONTENT" | head -3 | tr '\n' ' ' | cut -c1-100)...

## 关键要点

EOF

# 提取小节标题作为关键要点
grep "^## " "$ARTICLE" | sed 's/^## /- /' >> "$SUMMARY_FILE"

cat >> "$SUMMARY_FILE" << EOF

## 适合读者

- AI爱好者
- 内容创作者
- 教育工作者

## 建议标签

#AI工具 #科技趋势 #效率工具

---
*由 generate-summary.sh 自动生成*
EOF

echo "✅ 摘要已生成: $SUMMARY_FILE"
cat "$SUMMARY_FILE"