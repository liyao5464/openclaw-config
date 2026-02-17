#!/usr/bin/env python3
"""
生成微信合规的封面图 (900x383)
"""
import requests
import io

FAL_KEY = "c52e3c23-5e14-47c6-9059-c5e7aa62ff4c:04d3a9e98479295656e228845fbe8394"

url = "https://fal.run/fal-ai/flux/schnell"
headers = {
    "Authorization": f"Key {FAL_KEY}",
    "Content-Type": "application/json"
}
data = {
    "prompt": "Minimalist book cover design with question mark, dark blue background, subtle AI neural network pattern, thought-provoking atmosphere, professional editorial style, clean typography space",
    "aspect_ratio": "16:9",
    "image_size": "landscape_16_9"
}

print("生成封面图中...")
resp = requests.post(url, headers=headers, json=data, timeout=120)
result = resp.json()

print(f"结果: {result}")

if 'images' in result and len(result['images']) > 0:
    image_url = result['images'][0]['url']
    print(f"\n✅ 封面图生成成功!")
    print(f"URL: {image_url}")
    
    # 下载图片
    img_data = requests.get(image_url).content
    with open('/root/.openclaw/workspace/cover-article.jpg', 'wb') as f:
        f.write(img_data)
    print(f"✅ 已保存到: /root/.openclaw/workspace/cover-article.jpg")
else:
    print("❌ 生成失败")
