#!/usr/bin/env python3
"""
先上传图片获取 media_id，再创建草稿
"""
import requests

APPID = "wxbde0f982acfe271b"
SECRET = "a561d22a1227a810d66f13efa19bedb1"

# 获取 token
token_url = f"https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={APPID}&secret={SECRET}"
token = requests.get(token_url).json().get('access_token')
print(f"Token: {token[:30]}...")

# 1. 先上传临时素材（封面图）
# 使用占位图 URL 下载图片
img_url = "https://via.placeholder.com/900x383/d4a574/ffffff?text=2026%E6%98%A5%E6%99%9AAI%E7%9C%8B%E7%82%B9"
img_data = requests.get(img_url).content

# 上传图片素材
upload_url = f"https://api.weixin.qq.com/cgi-bin/media/upload?access_token={token}&type=thumb"
files = {'media': ('cover.jpg', img_data, 'image/jpeg')}
resp = requests.post(upload_url, files=files).json()
print(f"\n上传图片结果: {resp}")

if 'thumb_media_id' in resp:
    thumb_media_id = resp['thumb_media_id']
    print(f"✅ 封面图上传成功: {thumb_media_id}")
    
    # 2. 创建草稿
    draft_url = f"https://api.weixin.qq.com/cgi-bin/draft/add?access_token={token}"
    data = {
        "articles": [{
            "title": "看完春晚，我发现自己被时代甩了一截",
            "content": "<p>文章内容...</p>",
            "thumb_media_id": thumb_media_id
        }]
    }
    
    draft_resp = requests.post(draft_url, json=data).json()
    print(f"\n创建草稿结果: {json.dumps(draft_resp, indent=2, ensure_ascii=False)}")
else:
    print("❌ 封面上传失败")
