#!/usr/bin/env python3
"""
直接创建草稿（无封面图）
"""
import requests

APPID = "wxbde0f982acfe271b"
SECRET = "a561d22a1227a810d66f13efa19bedb1"

# 获取 token
token_url = f"https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={APPID}&secret={SECRET}"
token = requests.get(token_url, timeout=30).json().get('access_token')
print(f"✅ Token 获取成功")

# 读取文章内容
with open('/root/.openclaw/workspace/2026-chunwan-wechat-final.html', 'r', encoding='utf-8') as f:
    content = f.read()

print(f"📄 文章长度: {len(content)} 字符")

# 内容截断（微信限制）
if len(content) > 20000:
    print(f"⚠️ 内容过长，截断至 20000 字符")
    content = content[:20000]

# 创建草稿（无封面图）
print("\n📝 创建草稿...")
draft_url = f"https://api.weixin.qq.com/cgi-bin/draft/add?access_token={token}"

data = {
    "articles": [{
        "title": "看完春晚，我发现自己被时代甩了一截",
        "content": content,
        "author": "老里",
        "digest": "昨晚看完春晚，最大的感受是AI含量爆表！有几个节目美得令人瞠目...",
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
    print(f"💡 提示：请在公众号后台手动添加封面图")
    print(f"请登录 mp.weixin.qq.com 查看草稿")
else:
    print(f"\n❌ 创建失败: {draft_resp}")
