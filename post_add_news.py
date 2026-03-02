#!/usr/bin/env python3
"""
使用 add_news 接口（旧版图文消息接口）
"""
import requests

APPID = "wxbde0f982acfe271b"
SECRET = "a561d22a1227a810d66f13efa19bedb1"

# 获取 token
token_url = f"https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={APPID}&secret={SECRET}"
token = requests.get(token_url, timeout=30).json().get('access_token')
print(f"✅ Token: {token[:30]}...")

# 读取文章内容
with open('/root/.openclaw/workspace/2026-chunwan-wechat-final.html', 'r', encoding='utf-8') as f:
    content = f.read()

print(f"📄 文章长度: {len(content)} 字符")

# 使用 add_news 接口（永久图文素材）
print("\n📝 使用 add_news 接口...")
url = f"https://api.weixin.qq.com/cgi-bin/material/add_news?access_token={token}"

data = {
    "articles": [{
        "title": "看完春晚，我发现自己被时代甩了一截",
        "content": content,
        "author": "老里",
        "digest": "昨晚看完春晚，最大的感受是AI含量爆表！有几个节目美得令人瞠目...",
        "show_cover_pic": 0,
        "need_open_comment": 1,
        "only_fans_can_comment": 0
    }]
}

resp = requests.post(url, json=data, timeout=30).json()
print(f"\n结果: {resp}")

if 'media_id' in resp:
    print(f"\n🎉 成功！Media ID: {resp['media_id']}")
else:
    print(f"\n❌ 失败: {resp}")
