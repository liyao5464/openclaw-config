#!/usr/bin/env python3
"""
微信公众号草稿创建（简化版）
先测试基础功能
"""

import json
import requests

# 配置
APPID = "wxbde0f982acfe271b"
SECRET = "a561d22a1227a810d66f13efa19bedb1"

def get_token():
    url = f"https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={APPID}&secret={SECRET}"
    resp = requests.get(url, timeout=30).json()
    return resp.get('access_token')

def create_draft_simple(token):
    """创建简单草稿（测试）"""
    url = f"https://api.weixin.qq.com/cgi-bin/draft/add?access_token={token}"
    
    # 简化内容 - 微信要求的格式
    html_content = """
    <h1>看完春晚，我发现自己被时代甩了一截</h1>
    <p>说实话，昨晚看春晚的时候，我一直在走神。</p>
    <p>不是因为节目不好看，而是我脑子里一直在想一件事：这玩意儿（指AI）进步得太快了。</p>
    <p>原文较长，请查看完整内容...</p>
    """
    
    data = {
        "articles": [{
            "title": "看完春晚，我发现自己被时代甩了一截",
            "content": html_content,
            "author": "老里",
            "digest": "昨晚看完春晚，最大的感受是AI含量爆表！有几个节目美得令人瞠目..."
        }]
    }
    
    resp = requests.post(url, json=data, timeout=30).json()
    return resp

if __name__ == "__main__":
    print("获取 token...")
    token = get_token()
    print(f"Token: {token[:20]}...")
    
    print("\n创建草稿...")
    result = create_draft_simple(token)
    print(json.dumps(result, indent=2, ensure_ascii=False))
