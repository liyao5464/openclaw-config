#!/bin/bash
# 公众号文章一键发布脚本
# 使用: ./publish-post.sh <文章md文件> <账号类型>
# 账号类型: main (主号) | lab (实验室)

set -e

# 检查参数
if [ $# -lt 2 ]; then
    echo "用法: ./publish-post.sh <文章md文件> <账号类型:main|lab>"
    exit 1
fi

MD_FILE=$1
ACCOUNT_TYPE=$2

# 检查文件存在
if [ ! -f "$MD_FILE" ]; then
    echo "❌ 错误: 文件不存在 $MD_FILE"
    exit 1
fi

# 获取文件名（不含扩展名）
FILENAME=$(basename "$MD_FILE" .md)
HTML_FILE="/tmp/${FILENAME}.html"

echo "📝 正在处理: $MD_FILE"

# 根据账号选择转换脚本
if [ "$ACCOUNT_TYPE" == "main" ]; then
    echo "🎯 发布到: 主号"
    CONVERTER="/root/.openclaw/workspace/scripts/simple-md2html.js"
    APPID="wxbde0f982acfe271b"
    APPSECRET="a561d22a1227a810d66f13efa19bedb1"
elif [ "$ACCOUNT_TYPE" == "lab" ]; then
    echo "🧪 发布到: 实验室"
    CONVERTER="/root/.openclaw/workspace/scripts/md2html-pro.js"
    APPID="wx22983d127a8ee206"
    APPSECRET="ea1ea206e7f690a3b87f153dabc56770"
else
    echo "❌ 错误: 账号类型必须是 main 或 lab"
    exit 1
fi

# 转换为HTML
echo "🔄 转换为HTML..."
if [ -f "$CONVERTER" ]; then
    node "$CONVERTER" "$MD_FILE" > "$HTML_FILE"
else
    echo "⚠️ 转换脚本不存在，使用默认转换"
    echo "<html><body>$(cat "$MD_FILE")</body></html>" > "$HTML_FILE"
fi

echo "✅ HTML已生成: $HTML_FILE"

# 发布到微信（如果发布脚本存在）
PUBLISH_SCRIPT="/root/.openclaw/workspace/skills/baoyu-skills/skills/baoyu-post-to-wechat/scripts/wechat-api.ts"

if [ -f "$PUBLISH_SCRIPT" ]; then
    echo "📤 正在发布..."
    # 注意: 实际发布需要标题、封面图等参数
    echo "⚠️ 发布功能需要额外参数（标题、封面图、作者等）"
    echo "   请使用完整命令发布，或手动上传到公众号后台"
else
    echo "⚠️ 发布脚本不存在，请手动上传HTML"
fi

echo ""
echo "📋 发布检查清单:"
echo "   [ ] 检查标题是否合适"
echo "   [ ] 删除备用标题"
echo "   [ ] 确认封面图已上传"
echo "   [ ] 确认账号正确 ($ACCOUNT_TYPE)"
echo "   [ ] 预览检查格式"
echo ""
echo "✨ HTML文件: $HTML_FILE"
