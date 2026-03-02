#!/usr/bin/env python3
import requests
import json

APPID = "wxbde0f982acfe271b"
SECRET = "a561d22a1227a810d66f13efa19bedb1"

# 获取 token
token_url = f"https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={APPID}&secret={SECRET}"
token = requests.get(token_url).json().get('access_token')
print(f"Token: {token}")

# 最简测试 - 只传 title 和 content
url = f"https://api.weixin.qq.com/cgi-bin/draft/add?access_token={token}"
data = {
    "articles": [{
        "title": "测试文章",
        "content": "<p>这是一篇测试文章</p>"
    }]
}

resp = requests.post(url, json=data).json()
print(json.dumps(resp, indent=2, ensure_ascii=False))
