#!/bin/bash
# gen-image.sh - 调用 Labnana (Gemini) 生成文章配图
# 用法: ./gen-image.sh "提示词" [输出文件名.png] [宽高比]
# 宽高比: 1:1(默认) 16:9 9:16 4:3 3:4

PROMPT="$1"
OUTPUT="${2:-output.png}"
RATIO="${3:-1:1}"
API_KEY="lh_sk_692c146e2540cf229de27797_2a51341d61fdd05cae5afe63d404fddbf477dad21c562953"
ENDPOINT="https://api.labnana.com/openapi/v1/images/generation"

if [ -z "$PROMPT" ]; then
  echo "用法: $0 \"提示词\" [输出文件.png] [宽高比]"
  echo "宽高比: 1:1 16:9 9:16 4:3 3:4"
  exit 1
fi

echo "🎨 生成中: $PROMPT"

RESPONSE=$(curl -s -X POST "$ENDPOINT" \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d "{
    \"provider\": \"google\",
    \"prompt\": \"$PROMPT\",
    \"imageConfig\": {
      \"imageSize\": \"1K\",
      \"aspectRatio\": \"$RATIO\"
    }
  }")

# 从 Gemini 格式响应中提取 base64 图片
echo "$RESPONSE" | python3 -c "
import sys, json, base64
data = json.load(sys.stdin)
candidates = data.get('candidates', [])
if candidates:
    parts = candidates[0].get('content', {}).get('parts', [])
    for part in parts:
        inline = part.get('inlineData', {})
        if inline.get('data'):
            img = base64.b64decode(inline['data'])
            with open('$OUTPUT', 'wb') as f:
                f.write(img)
            print('OK')
            sys.exit(0)
# 失败
err = data.get('message', data.get('error', str(data)[:200]))
print(f'FAIL:{err}')
sys.exit(1)
" 2>/dev/null

if [ $? -eq 0 ]; then
  echo "✅ 已保存: $OUTPUT"
else
  echo "❌ 生成失败: $(echo "$RESPONSE" | head -c 300)"
  exit 1
fi
