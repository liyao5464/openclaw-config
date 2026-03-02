#!/usr/bin/env python3
"""
用最简化的内容测试
"""
import requests

APPID = "wxbde0f982acfe271b"
SECRET = "a561d22a1227a810d66f13efa19bedb1"

# 获取 token
token_url = f"https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={APPID}&secret={SECRET}"
token = requests.get(token_url, timeout=30).json().get('access_token')
print(f"✅ Token: {token[:30]}...")

# 最简单的内容
test_content = "<p>看完春晚，我发现自己被时代甩了一截</p><p>说实话，昨晚看春晚的时候，我一直在走神。不是因为节目不好看，而是我脑子里一直在想一件事：这玩意儿（指AI）进步得太快了。</p>"

print(f"📄 内容长度: {len(test_content)} 字符")

# 创建草稿
print("\n📝 创建测试草稿...")
draft_url = f"https://api.weixin.qq.com/cgi-bin/draft/add?access_token={token}"

data = {
    "articles": [{
        "title": "测试文章",
        "content": test_content
    }]
}

draft_resp = requests.post(draft_url, json=data, timeout=30).json()
print(f"\n结果: {draft_resp}")

if 'media_id' in draft_resp:
    print(f"\n🎉 成功！Media ID: {draft_resp['media_id']}")
else:
    print(f"\n❌ 失败")
