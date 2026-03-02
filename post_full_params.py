#!/usr/bin/env python3
"""
完整参数格式重试
"""
import requests
import json

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

# 尝试不设置任何media_id，看看是否还有其他必填字段
print("\n📝 尝试创建草稿（无封面，完整参数）...")
draft_url = f"https://api.weixin.qq.com/cgi-bin/draft/add?access_token={token}"

data = {
    "articles": [{
        "title": "看完春晚，我发现自己被时代甩了一截",
        "content": content,
        "author": "老里",
        "digest": "昨晚看完春晚，最大的感受是AI含量爆表！有几个节目美得令人瞠目...",
        "content_source_url": "",
        "show_cover_pic": 0,
        "need_open_comment": 1,
        "only_fans_can_comment": 0
    }]
}

print(f"请求数据: {json.dumps(data, ensure_ascii=False)[:500]}...")

draft_resp = requests.post(draft_url, json=data, timeout=30).json()
print(f"\n结果: {json.dumps(draft_resp, indent=2, ensure_ascii=False)}")

if 'media_id' in draft_resp:
    print(f"\n🎉 发布成功！Media ID: {draft_resp['media_id']}")
else:
    print(f"\n❌ 创建失败")
