#!/usr/bin/env python3
"""
微信公众号文章发布脚本
无需 npm/bun 依赖，直接使用 Python + 微信 API
"""

import json
import requests
import sys
import os

# 微信配置
WECHAT_APPID = "wxbde0f982acfe271b"
WECHAT_SECRET = "a561d22a1227a810d66f13efa19bedb1"

def get_access_token():
    """获取微信 access_token"""
    url = f"https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={WECHAT_APPID}&secret={WECHAT_SECRET}"
    try:
        response = requests.get(url, timeout=30)
        data = response.json()
        if 'access_token' in data:
            print(f"✅ Access token 获取成功")
            return data['access_token']
        else:
            print(f"❌ 获取 token 失败: {data}")
            return None
    except Exception as e:
        print(f"❌ 请求失败: {e}")
        return None

def upload_image(access_token, image_path):
    """上传图片到微信素材库"""
    url = f"https://api.weixin.qq.com/cgi-bin/media/uploadimg?access_token={access_token}"
    try:
        with open(image_path, 'rb') as f:
            files = {'media': f}
            response = requests.post(url, files=files, timeout=30)
            data = response.json()
            if 'url' in data:
                print(f"✅ 图片上传成功: {data['url']}")
                return data['url']
            else:
                print(f"❌ 图片上传失败: {data}")
                return None
    except Exception as e:
        print(f"❌ 图片上传失败: {e}")
        return None

def create_draft(access_token, title, content, thumb_media_id=None):
    """创建草稿"""
    url = f"https://api.weixin.qq.com/cgi-bin/draft/add?access_token={access_token}"
    
    # 构造图文消息
    articles = [{
        "title": title,
        "content": content,
        "author": "老里",
        "digest": "昨晚看完春晚，最大的感受是AI含量爆表！有几个节目美得令人瞠目……",
        "content_source_url": "",
        "need_open_comment": 1,
        "only_fans_can_comment": 0
    }]
    
    # 如果有封面图 media_id，才添加
    if thumb_media_id:
        articles[0]["thumb_media_id"] = thumb_media_id
    
    data = {"articles": articles}
    
    try:
        response = requests.post(url, json=data, timeout=30)
        result = response.json()
        if 'media_id' in result:
            print(f"✅ 草稿创建成功!")
            print(f"📄 Media ID: {result['media_id']}")
            return result['media_id']
        else:
            print(f"❌ 创建草稿失败: {result}")
            return None
    except Exception as e:
        print(f"❌ 请求失败: {e}")
        return None

def main():
    print("🚀 开始发布到微信公众号...")
    print(f"AppID: {WECHAT_APPID[:10]}...")
    
    # 1. 获取 access_token
    token = get_access_token()
    if not token:
        print("❌ 无法获取 access_token，请检查 AppID 和 Secret")
        return
    
    # 2. 读取文章内容
    html_file = "/root/.openclaw/workspace/2026-chunwan-wechat-final.html"
    if not os.path.exists(html_file):
        print(f"❌ 文件不存在: {html_file}")
        return
    
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print(f"✅ 已读取文章 ({len(content)} 字符)")
    
    # 3. 创建草稿
    media_id = create_draft(
        access_token=token,
        title="看完春晚，我发现自己被时代甩了一截",
        content=content
    )
    
    if media_id:
        print(f"\n🎉 发布成功!")
        print(f"📱 请登录公众号后台查看草稿")
    else:
        print(f"\n❌ 发布失败")

if __name__ == "__main__":
    main()
