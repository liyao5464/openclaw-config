#!/usr/bin/env python3
"""
使用永久素材接口上传封面并发布
"""
import requests
import io

APPID = "wxbde0f982acfe271b"
SECRET = "a561d22a1227a810d66f13efa19bedb1"

# 获取 token
token_url = f"https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={APPID}&secret={SECRET}"
token = requests.get(token_url, timeout=30).json().get('access_token')
print(f"✅ Token 获取成功")

# 构造一个最小的有效的 1x1 棕色 JPEG
jpeg_data = bytes([
    0xFF, 0xD8, 0xFF, 0xE0, 0x00, 0x10, 0x4A, 0x46, 0x49, 0x46, 0x00, 0x01,
    0x01, 0x00, 0x00, 0x01, 0x00, 0x01, 0x00, 0x00, 0xFF, 0xDB, 0x00, 0x43,
    0x00, 0x08, 0x06, 0x06, 0x07, 0x06, 0x05, 0x08, 0x07, 0x07, 0x07, 0x09,
    0x09, 0x08, 0x0A, 0x0C, 0x14, 0x0D, 0x0C, 0x0B, 0x0B, 0x0C, 0x19, 0x12,
    0x13, 0x0F, 0x14, 0x1D, 0x1A, 0x1F, 0x1E, 0x1D, 0x1A, 0x1C, 0x1C, 0x20,
    0x24, 0x2E, 0x27, 0x20, 0x22, 0x2C, 0x23, 0x1C, 0x1C, 0x28, 0x37, 0x29,
    0x2C, 0x30, 0x31, 0x34, 0x34, 0x34, 0x1F, 0x27, 0x39, 0x3D, 0x38, 0x32,
    0x3C, 0x2E, 0x33, 0x34, 0x32, 0xFF, 0xC0, 0x00, 0x0B, 0x08, 0x00, 0x01,
    0x00, 0x01, 0x01, 0x01, 0x11, 0x00, 0xFF, 0xC4, 0x00, 0x1F, 0x00, 0x00,
    0x01, 0x05, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08,
    0x09, 0x0A, 0x0B, 0xFF, 0xDA, 0x00, 0x08, 0x01, 0x01, 0x00, 0x00, 0x3F,
    0x00, 0x7F, 0xFF, 0xD9
])

# 1. 上传永久素材（封面图）
print("📤 上传永久封面图...")
upload_url = f"https://api.weixin.qq.com/cgi-bin/material/add_material?access_token={token}&type=thumb"
files = {'media': ('cover.jpg', io.BytesIO(jpeg_data), 'image/jpeg')}
resp = requests.post(upload_url, files=files, timeout=30).json()
print(f"上传结果: {resp}")

if 'media_id' in resp:
    thumb_media_id = resp['media_id']
    print(f"✅ 永久封面图上传成功: {thumb_media_id}")
    
    # 2. 创建草稿
    print("\n📝 创建草稿...")
    draft_url = f"https://api.weixin.qq.com/cgi-bin/draft/add?access_token={token}"
    
    # 读取文章内容
    with open('/root/.openclaw/workspace/2026-chunwan-wechat-final.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 内容可能太长，微信限制，截断一下
    if len(content) > 20000:
        print(f"⚠️ 内容过长 ({len(content)} 字符)，需要截断")
        content = content[:20000]
    
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
    
    draft_resp = requests.post(draft_url, json=data, timeout=30).json()
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
