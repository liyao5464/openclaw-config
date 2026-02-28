#!/bin/bash
# md2html-simple.sh - 简单Markdown转HTML脚本（主号使用）
# 适用于老里主号公众号文章

if [ $# -lt 1 ]; then
    echo "Usage: $0 <markdown-file>"
    exit 1
fi

MD_FILE="$1"
FILENAME=$(basename "$MD_FILE" .md)
OUTPUT_DIR="$(dirname "$MD_FILE")"
HTML_FILE="${OUTPUT_DIR}/${FILENAME}.html"

# 读取markdown内容
CONTENT=$(cat "$MD_FILE")

# 转换为HTML（简单版本）
# 处理标题
CONTENT=$(echo "$CONTENT" | sed 's/^# \(.*\)$/<h1>\1<\/h1>/')
CONTENT=$(echo "$CONTENT" | sed 's/^## \(.*\)$/<h2>\1<\/h2>/')
CONTENT=$(echo "$CONTENT" | sed 's/^### \(.*\)$/<h3>\1<\/h3>/')

# 处理粗体和斜体
CONTENT=$(echo "$CONTENT" | sed 's/\*\*\(.*\)\*\*/<strong>\1<\/strong>/g')
CONTENT=$(echo "$CONTENT" | sed 's/\*\(.*\)\*/<em>\1<\/em>/g')

# 处理引用
CONTENT=$(echo "$CONTENT" | sed 's/^> \(.*\)$/<blockquote>\1<\/blockquote>/')

# 处理列表
CONTENT=$(echo "$CONTENT" | sed 's/^- \(.*\)$/<li>\1<\/li>/')
CONTENT=$(echo "$CONTENT" | sed 's/^[0-9]\. \(.*\)$/<li>\1<\/li>/')

# 处理段落（非空行且不以<开头）
CONTENT=$(echo "$CONTENT" | awk '
BEGIN { in_para = 0 }
{
    if ($0 ~ /^<|^$/ ) {
        if (in_para) { print "</p>"; in_para = 0 }
        print
    } else {
        if (!in_para) { printf "<p>"; in_para = 1 }
        printf "%s", $0
    }
}
END { if (in_para) print "</p>" }
')

# 添加HTML头尾
cat > "$HTML_FILE" << EOF
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${FILENAME}</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; line-height: 1.8; max-width: 680px; margin: 0 auto; padding: 20px; color: #333; }
        h1 { font-size: 24px; border-bottom: 2px solid #07c160; padding-bottom: 10px; }
        h2 { font-size: 20px; color: #07c160; margin-top: 30px; }
        h3 { font-size: 17px; color: #576b95; }
        blockquote { border-left: 4px solid #07c160; padding-left: 15px; color: #666; font-style: italic; margin: 20px 0; }
        li { margin: 8px 0; }
        p { margin: 15px 0; }
        strong { color: #07c160; }
    </style>
</head>
<body>
${CONTENT}
</body>
</html>
EOF

echo "✅ 已生成: $HTML_FILE"