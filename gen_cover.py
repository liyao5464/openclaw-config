#!/usr/bin/env python3
"""
用 FAL API 生成封面图
"""
import requests
import json

FAL_KEY = "c52e3c23-5e14-47c6-9059-c5e7aa62ff4c:04d3a9e98479295656e228845fbe8394"

url = "https://fal.run/fal-ai/flux/schnell"
headers = {
    "Authorization": f"Key {FAL_KEY}",
    "Content-Type": "application/json"
}
data = {
    "prompt": "2026 Spring Festival Gala AI theme poster, robot performing martial arts on stage, red lanterns, golden decorations, tech light effects, data streams, horse silhouette, warm brown red gold color scheme, cinematic poster quality",
    "aspect_ratio": "16:9",
    "image_size": "landscape_16_9"
}

print("生成封面图中...")
resp = requests.post(url, headers=headers, json=data, timeout=120)
result = resp.json()

print(f"结果: {json.dumps(result, indent=2)[:500]}")

if 'images' in result and len(result['images']) > 0:
    image_url = result['images'][0]['url']
    print(f"\n✅ 封面图生成成功!")
    print(f"URL: {image_url}")
    
    # 下载图片
    img_data = requests.get(image_url).content
    with open('/root/.openclaw/workspace/cover-chunwan.png', 'wb') as f:
        f.write(img_data)
    print(f"✅ 已保存到: /root/.openclaw/workspace/cover-chunwan.png")
else:
    print("❌ 生成失败")
