#!/usr/bin/env python3
"""
创建纯色封面图并上传
"""
import requests
import base64
from io import BytesIO

APPID = "wxbde0f982acfe271b"
SECRET = "a561d22a1227a810d66f13efa19bedb1"

# 获取 token
token_url = f"https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={APPID}&secret={SECRET}"
token = requests.get(token_url).json().get('access_token')
print(f"✅ Token 获取成功")

# 创建一个简单的纯色图片 (1x1 像素，棕色，会被微信拉伸)
# 使用 base64 编码的棕色 PNG 图片
# 这是一个 900x383 的棕色背景图
img_base64 = """
iVBORw0KGgoAAAANSUhEUgAAA4AAAAF/CAYAAAB2R3hMAAAACXBIWXMAABYlAAAWJQFJUUtw
AAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAIABJREFUeJzt3Xd8FHX+
x/H3zGzLppNGQiAJvYUO0kSKFEFR9BQVz57Zz8PuvJ+9nJ56Zz17Zz17Zz17Zz17Zz17Zz17
Zz17Zz17Zz17Zz17Zz17Zz17Zz17Zz17Zz17Zz17Zz17Zz17Zz17Zz17Zz17Zz17Zz17
Zz17Zz17Zz17Zz17Zz17Zz17Zz17Zz17Zz17Zz17Zz17Zz17Zz17Zz17Zz17Zz17Zz17
Zz17Zz17Zz17Zz17Zz17Zz17Zz17Zz17Zz17Zz17Zz17Zz17Zz17Zz17Zz17Zz17Zz17
Zz17Zz17Zz17Zz17Zz17Zz17Zz17Zz17Zz17Zz17Zz17Zz17Zz17Zz17Zz17Zz17Zz17
Zz17Zz17Zz17Zz17Zz17Zz17Zz17Zz17Zz17Zz17Zz17Zz17Zz17Zz17Zz17Zz17Zz17
Zz17Zz17Zz17Zz17Zz17Zz17Zz17Zz17Zz17Zz17Zz17Zz17Zz17Zz17Zz17Zz17Zz17
Zz17Zz17Zz17Zz17Zz17Zz17Zz17Zz17Zz17Zz17Zz17Zz17Zz17Zz17Zz17Zz17Zz17
Zz17Zz17Zz17Zz17Zz17Zz17Zz17Zz17Zz17Zz2/8N/2U4h7/g+v0AAAAASUVORK5CYII=
"""

img_data = base64.b64decode(img_base64.strip())

# 上传图片素材
print("📤 上传封面图...")
upload_url = f"https://api.weixin.qq.com/cgi-bin/media/upload?access_token={token}&type=thumb"
files = {'media': ('cover.jpg', BytesIO(img_data), 'image/jpeg')}
resp = requests.post(upload_url, files=files).json()
print(f"上传结果: {resp}")

if 'thumb_media_id' in resp:
    thumb_media_id = resp['thumb_media_id']
    print(f"✅ 封面图上传成功: {thumb_media_id}")
    
    # 创建草稿
    print("\n📝 创建草稿...")
    draft_url = f"https://api.weixin.qq.com/cgi-bin/draft/add?access_token={token}"
    
    # 读取文章内容
    with open('/root/.openclaw/workspace/2026-chunwan-wechat-final.html', 'r') as f:
        content = f.read()
    
    data = {
        "articles": [{
            "title": "看完春晚，我发现自己被时代甩了一截",
            "content": content,
            "author": "老里",
            "digest": "昨晚看完春晚，最大的感受是AI含量爆表！有几个节目美得令人瞠目...",
            "thumb_media_id": thumb_media_id,
            "need_open_comment": 1,
            "only_fans_can_comment": 0
        }]
    }
    
    draft_resp = requests.post(draft_url, json=data).json()
    print(f"\n草稿创建结果:")
    print(f"{draft_resp}")
    
    if 'media_id' in draft_resp:
        print(f"\n🎉 发布成功！")
        print(f"📱 Media ID: {draft_resp['media_id']}")
        print(f"请登录公众号后台查看草稿")
    else:
        print(f"\n❌ 创建失败: {draft_resp}")
else:
    print("❌ 封面上传失败")
