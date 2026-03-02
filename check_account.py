#!/usr/bin/env python3
"""
检查账号信息
"""
import requests

APPID = "wxbde0f982acfe271b"
SECRET = "a561d22a1227a810d66f13efa19bedb1"

# 获取 token
token_url = f"https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={APPID}&secret={SECRET}"
token_resp = requests.get(token_url, timeout=30).json()
print(f"Token 响应: {token_resp}")

if 'access_token' in token_resp:
    token = token_resp['access_token']
    
    # 获取账号信息
    info_url = f"https://api.weixin.qq.com/cgi-bin/account/getaccountbasicinfo?access_token={token}"
    info = requests.get(info_url, timeout=30).json()
    print(f"\n账号信息: {info}")
    
    # 检查草稿箱权限
    draft_count_url = f"https://api.weixin.qq.com/cgi-bin/draft/count?access_token={token}"
    count = requests.get(draft_count_url, timeout=30).json()
    print(f"\n草稿数量: {count}")
else:
    print("获取 token 失败")
