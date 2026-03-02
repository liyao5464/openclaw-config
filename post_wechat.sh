#!/bin/bash

# 微信公众号 API 发布脚本
# 用法: bash post_wechat.sh "标题" "内容" "封面图片路径(可选)"

APPID="wxbde0f982acfe271b"
SECRET="a561d22a1227a810d66f13efa19bedb1"

# 获取 access_token
echo "正在获取 access_token..."
TOKEN_RESPONSE=$(curl -s "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=${APPID}&secret=${SECRET}")
ACCESS_TOKEN=$(echo $TOKEN_RESPONSE | grep -o '"access_token":"[^"]*"' | cut -d'"' -f4)

if [ -z "$ACCESS_TOKEN" ]; then
    echo "获取 token 失败: $TOKEN_RESPONSE"
    exit 1
fi

echo "✅ 获取 token 成功"

# 如果有封面图，先上传
MEDIA_ID=""
if [ -n "$3" ] && [ -f "$3" ]; then
    echo "正在上传封面图..."
    UPLOAD_RESPONSE=$(curl -s -F "media=@$3" "https://api.weixin.qq.com/cgi-bin/material/add_material?access_token=${ACCESS_TOKEN}&type=thumb")
    MEDIA_ID=$(echo $UPLOAD_RESPONSE | grep -o '"media_id":"[^"]*"' | cut -d'"' -f4)
    echo "✅ 封面上传成功: $MEDIA_ID"
fi

# 准备图文内容
TITLE="$1"
CONTENT="$2"

# 转义特殊字符
CONTENT_ESCAPED=$(echo "$CONTENT" | sed 's/\\/\\\\/g; s/"/\\"/g; s/\n/\\n/g')

# 构造请求体
JSON_BODY="{
    \"articles\": [{
        \"title\": \"${TITLE}\",
        \"thumb_media_id\": \"${MEDIA_ID}\",
        \"content\": \"${CONTENT_ESCAPED}\",
        \"content_source_url\": \"\",
        \"digest\": \"\",
        \"show_cover_pic\": 0
    }]
}"

echo "正在发布文章..."
# 新增永久素材（图文消息）
RESPONSE=$(curl -s -X POST \
    "https://api.weixin.qq.com/cgi-bin/material/add_news?access_token=${ACCESS_TOKEN}" \
    -H "Content-Type: application/json" \
    -d "$JSON_BODY")

echo "API 响应: $RESPONSE"

# 检查是否成功
if echo "$RESPONSE" | grep -q '"media_id"'; then
    echo "✅ 文章发布成功！"
    echo "media_id: $(echo $RESPONSE | grep -o '"media_id":"[^"]*"' | cut -d'"' -f4)"
else
    echo "❌ 发布失败"
    echo "错误: $(echo $RESPONSE | grep -o '"errmsg":"[^"]*"' | cut -d'"' -f4)"
fi