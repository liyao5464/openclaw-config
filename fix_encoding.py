#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信公众号发布 - 修复编码问题
"""

import requests
import json
import os

APPID = "wxbde0f982acfe271b"
SECRET = "a561d22a1227a810d66f13efa19bedb1"

TITLE = "Seedance 2.0 实测"
DIGEST = "字节AI视频工具实测"

# 使用简单 HTML，避免复杂编码
CONTENT = """<h2>先搞清楚这是啥</h2>
<p>上周刷视频的时候，看到一条 AI 生成的短片。画面里的人正在说话，口型和声音居然对上了，而且不是那种"大概能对上"的水平，是你真以为是实拍的那种同步。</p>
<p>我盯着看了三遍，然后发现这是字节跳动的 <strong>Seedance 2.0</strong> 生成的。</p>

<h2>我实际测了什么</h2>
<p><strong>场景一：人物对话</strong> - prompt 写得很简单："一个女孩坐在咖啡厅里，对着镜头说话"。出来的效果让我愣了一下，女孩的嘴型真的在跟着"说话"的节奏动。</p>
<p><strong>场景二：多镜头切换</strong> - 三个镜头，人物长相、衣服、光线都能保持一致。</p>
<p><strong>场景三：口播视频</strong> - 口型同步率很高，表情自然，背景也不穿帮。</p>

<h2>竞品对比</h2>
<p>音视频同步：Seedance 原生支持 | Veo 3 支持 | Sora 不支持 | 可灵 不支持</p>
<p>生成速度：Seedance 41秒 | 可灵较快 | Sora几分钟 | Veo较慢</p>
<p>价格：可灵 0.99元/5s | Seedance 3.67元/5s | Sora $20/月 | Veo $250/月</p>

<h2>当然不完美</h2>
<p>1. 手还是不行 - AI 视频的通病</p>
<p>2. 太复杂的 prompt 会崩</p>
<p>3. 中文口型还有提升空间</p>

<h2>最后说两句</h2>
<p>AI 视频这个赛道，2024 年是"从无到有"，2025 年是"从有到好"。Seedance 2.0 这一步，标志着 AI 视频开始真正"可用"了——是商用级别的可用。</p>"""

def get_token():
    url = f"https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={APPID}&secret={SECRET}"
    resp = requests.get(url)
    return resp.json().get("access_token")

def upload_image(token):
    """上传封面图"""
    url = f"https://api.weixin.qq.com/cgi-bin/material/add_material?access_token={token}&type=thumb"
    
    # 下载示例图片
    os.system("curl -sL 'https://picsum.photos/400/300' -o /tmp/cover.jpg")
    
    with open("/tmp/cover.jpg", "rb") as f:
        files = {"media": f}
        resp = requests.post(url, files=files)
    
    os.remove("/tmp/cover.jpg")
    return resp.json()

def publish(token, thumb_id):
    """发布草稿"""
    url = f"https://api.weixin.qq.com/cgi-bin/draft/add?access_token={token}"
    
    article = {
        "title": TITLE,
        "content": CONTENT,
        "digest": DIGEST,
        "thumb_media_id": thumb_id,
        "show_cover_pic": 0,
        "need_open_comment": 1,
        "only_fans_can_comment": 0
    }
    
    data = {"articles": [article]}
    
    headers = {"Content-Type": "application/json; charset=utf-8"}
    resp = requests.post(url, json=data, headers=headers)
    return resp.json()

def main():
    print("获取 token...")
    token = get_token()
    if not token:
        print("获取失败")
        return
    print("✅ Token OK")
    
    print("\n上传封面...")
    upload_res = upload_image(token)
    thumb_id = upload_res.get("media_id")
    if not thumb_id:
        print(f"上传失败: {upload_res}")
        return
    print(f"✅ 封面 OK: {thumb_id[:20]}...")
    
    print("\n创建草稿...")
    result = publish(token, thumb_id)
    print(f"响应: {json.dumps(result, ensure_ascii=False)}")
    
    if result.get("media_id"):
        print(f"\n✅ 成功!")
        print(f"media_id: {result['media_id']}")
        print(f"\n请登录 https://mp.weixin.qq.com 查看草稿")
    else:
        print(f"\n❌ 失败: {result.get('errmsg')}")

if __name__ == "__main__":
    main()
