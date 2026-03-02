#!/usr/bin/env python3
"""
发布到微信公众号 - 使用临时图片作为封面
"""
import requests
import io

APPID = "wxbde0f982acfe271b"
SECRET = "a561d22a1227a810d66f13efa19bedb1"

# 获取 token
token_url = f"https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={APPID}&secret={SECRET}"
token = requests.get(token_url, timeout=30).json().get('access_token')
print(f"✅ Token 获取成功")

# 读取文章内容
with open('/root/.openclaw/workspace/matt-shumer-wechat.html', 'r', encoding='utf-8') as f:
    content = f.read()

print(f"📄 文章长度: {len(content)} 字符")

# 上传临时图片作为封面
print("📤 上传封面图...")
upload_url = f"https://api.weixin.qq.com/cgi-bin/media/upload?access_token={token}&type=thumb"

# 使用新生成的封面图
with open('/root/.openclaw/workspace/cover-article.jpg', 'rb') as f:
    files = {'media': ('cover.jpg', f, 'image/jpeg')}
    upload_resp = requests.post(upload_url, files=files, timeout=30).json()

print(f"上传结果: {upload_resp}")

if 'thumb_media_id' in upload_resp:
    thumb_media_id = upload_resp['thumb_media_id']
    print(f"✅ 封面上传成功: {thumb_media_id}")
    
    # 创建草稿
    print("\n📝 创建草稿...")
    draft_url = f"https://api.weixin.qq.com/cgi-bin/draft/add?access_token={token}"
    
    data = {
        "articles": [{
            "title": "那篇7000万阅读的爆文，到底在害怕什么？",
            "content": content,
            "author": "老里",
            "digest": "我读了三遍Matt Shumer的文章，发现大多数人没get到真正的恐怖点。递归自我改进、认知断层、权力转移...这篇文章把底层逻辑挖透了。",
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
