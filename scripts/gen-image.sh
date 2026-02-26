#!/bin/bash
# gen-image.sh - 调用 wan2.6-t2i 生成文章配图
# 用法: ./gen-image.sh "提示词" 输出文件名.png

PROMPT="$1"
OUTPUT="${2:-output.png}"
API_KEY="sk-a0a58e7d5a1f46a08d1884c84c1bfc96"
ENDPOINT="https://dashscope.aliyuncs.com/api/v1/services/aigc/multimodal-generation/generation"

if [ -z "$PROMPT" ]; then
  echo "用法: $0 \"提示词\" [输出文件名.png]"
  exit 1
fi

echo "🎨 生成中: $PROMPT"

RESPONSE=$(curl -s -X POST "$ENDPOINT" \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d "{
    \"model\": \"wan2.6-t2i\",
    \"input\": {
      \"messages\": [{
        \"role\": \"user\",
        \"content\": [{\"type\": \"text\", \"text\": \"$PROMPT\"}]
      }]
    },
    \"parameters\": {\"size\": \"1024*1024\", \"n\": 1}
  }")

IMAGE_URL=$(echo "$RESPONSE" | python3 -c "
import sys, json
data = json.load(sys.stdin)
choices = data.get('output', {}).get('choices', [])
if choices:
    content = choices[0]['message']['content']
    for item in content:
        if item.get('type') == 'image':
            print(item['image'])
            break
" 2>/dev/null)

if [ -z "$IMAGE_URL" ]; then
  echo "❌ 生成失败: $RESPONSE"
  exit 1
fi

curl -s -o "$OUTPUT" "$IMAGE_URL"
echo "✅ 已保存: $OUTPUT"
echo "$IMAGE_URL"
