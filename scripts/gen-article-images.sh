#!/bin/bash
# gen-article-images.sh - 分析文章内容，自动生成配图并嵌入 Markdown
# 用法: bash scripts/gen-article-images.sh articles/my-article.md
# 可选: bash scripts/gen-article-images.sh articles/my-article.md --count 3 --no-embed

set -e

ARTICLE="$1"
COUNT=2        # 默认生成 2 张配图
EMBED=true     # 默认嵌入到 Markdown
DASHSCOPE_API_KEY="sk-a0a58e7d5a1f46a08d1884c84c1bfc96"
ANYROUTER_API_KEY="sk-Ajvm8RLYw8P4dn0o9yTC9I5AG5QGMSD1awBVchVlUBxL6M5I"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

# 解析参数
shift
while [[ $# -gt 0 ]]; do
  case "$1" in
    --count) COUNT="$2"; shift 2 ;;
    --no-embed) EMBED=false; shift ;;
    *) shift ;;
  esac
done

# 检查文章文件
if [ -z "$ARTICLE" ] || [ ! -f "$ARTICLE" ]; then
  echo "用法: $0 <文章路径.md> [--count 2] [--no-embed]"
  exit 1
fi

ARTICLE_DIR="$(dirname "$ARTICLE")"
ARTICLE_NAME="$(basename "$ARTICLE" .md)"
IMAGES_DIR="$ARTICLE_DIR/images"
mkdir -p "$IMAGES_DIR"

echo "📖 分析文章: $ARTICLE"
echo "🎨 计划生成: $COUNT 张配图"
echo ""

# 读取文章内容（截取前 3000 字）
CONTENT=$(head -c 3000 "$ARTICLE")

# 调用 AI 分析文章，生成配图提示词
echo "🤖 AI 分析文章结构，生成配图提示词..."

PROMPTS_JSON=$(python3 -c "
import json, urllib.request, sys

content = open('$ARTICLE').read()[:3000]
count = $COUNT
api_key = '$ANYROUTER_API_KEY'

payload = {
    'model': 'claude-sonnet-4-6',
    'max_tokens': 1024,
    'messages': [{
        'role': 'user',
        'content': f'你是专业的文章配图设计师。分析以下文章，生成 {count} 个配图提示词。\n\n要求：\n1. 提示词用英文\n2. 风格：真实感、生活化、适合微信公众号\n3. 避免：文字、人脸特写、版权元素\n4. 返回 JSON：{{\"images\": [{{\"position\": \"段落描述\", \"prompt\": \"英文提示词\", \"alt\": \"中文说明\"}}]}}\n\n文章：\n{content}'
    }]
}

req = urllib.request.Request(
    'https://api.autocode.space/v1/messages',
    data=json.dumps(payload).encode(),
    headers={
        'x-api-key': api_key,
        'anthropic-version': '2023-06-01',
        'content-type': 'application/json'
    }
)
resp = urllib.request.urlopen(req, timeout=30)
print(resp.read().decode())
" 2>/dev/null)

# 解析提示词
IMAGES_DATA=$(echo "$PROMPTS_JSON" | python3 -c "
import sys, json, re
data = json.load(sys.stdin)
text = data.get('content', [{}])[0].get('text', '')
# 提取 JSON
match = re.search(r'\{.*\}', text, re.DOTALL)
if match:
    print(match.group())
else:
    print('{\"images\": []}')
" 2>/dev/null)

if [ -z "$IMAGES_DATA" ] || [ "$IMAGES_DATA" = '{"images": []}' ]; then
  echo "❌ AI 分析失败，使用默认提示词"
  IMAGES_DATA="{\"images\": [{\"position\": \"封面\", \"prompt\": \"modern technology concept, clean minimal design, soft lighting, professional photography\", \"alt\": \"文章配图\"}]}"
fi

echo "✅ 提示词生成完成"
echo ""

# 批量生成图片
echo "$IMAGES_DATA" | python3 -c "
import sys, json, subprocess, os

data = json.load(sys.stdin)
images = data.get('images', [])
script_dir = '$SCRIPT_DIR'
images_dir = '$IMAGES_DIR'
article_name = '$ARTICLE_NAME'
embed = '$EMBED' == 'true'
article_path = '$ARTICLE'

results = []

for i, img in enumerate(images):
    prompt = img.get('prompt', '')
    alt = img.get('alt', f'配图{i+1}')
    position = img.get('position', f'段落{i+1}')
    filename = f'{article_name}-img{i+1}.png'
    output_path = os.path.join(images_dir, filename)

    print(f'🎨 生成第 {i+1} 张: {alt}')
    print(f'   提示词: {prompt[:60]}...' if len(prompt) > 60 else f'   提示词: {prompt}')

    result = subprocess.run(
        ['bash', os.path.join(script_dir, 'gen-image.sh'), prompt, output_path],
        capture_output=True, text=True
    )

    if os.path.exists(output_path):
        print(f'   ✅ 已保存: images/{filename}')
        results.append({'alt': alt, 'path': f'images/{filename}', 'position': position})
    else:
        print(f'   ❌ 生成失败')

print('')

# 嵌入到 Markdown
if embed and results:
    print('📝 嵌入图片到文章...')
    with open(article_path, 'r') as f:
        content = f.read()

    # 在文章末尾追加图片（简单策略）
    img_section = '\n\n---\n\n'
    for r in results:
        img_section += f'![{r[\"alt\"]}]({r[\"path\"]})\n\n'

    with open(article_path, 'a') as f:
        f.write(img_section)

    print(f'✅ 已嵌入 {len(results)} 张图片到文章末尾')
    print('')
    print('💡 提示：图片已追加到文章末尾，你可以手动移动到合适位置')
"

echo ""
echo "🎉 完成！图片保存在: $IMAGES_DIR"
