#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信公众号发布 - 精简版
"""

import requests
import json
import os
import base64

APPID = "wxbde0f982acfe271b"
SECRET = "a561d22a1227a810d66f13efa19bedb1"

# 标题（中文算3字节，64字节≈21个中文字符）
TITLE = "Seedance 2.0 实测"

# 摘要（120字节以内）
DIGEST = "字节AI视频工具Seedance 2.0实测：音视频同步、多镜头叙事"

CONTENT = """<h2>先搞清楚这是啥</h2>
<p>上周刷视频的时候，看到一条 AI 生成的短片。画面里的人正在说话，口型和声音居然对上了，而且不是那种"大概能对上"的水平，是你真以为是实拍的那种同步。</p>

<h2>我实际测了什么</h2>
<p><strong>场景一：人物对话</strong> - prompt 写得很简单："一个女孩坐在咖啡厅里，对着镜头说话"。出来的效果让我愣了一下，女孩的嘴型真的在跟着"说话"的节奏动。</p>
<p><strong>场景二：多镜头切换</strong> - 三个镜头，人物长相、衣服、光线都能保持一致。</p>
<p><strong>场景三：口播视频</strong> - 口型同步率很高，表情自然，背景也不穿帮。</p>

<h2>竞品对比</h2>
<p>音视频同步：Seedance ✅ 原生 | Veo 3 ✅ | Sora ❌ | 可灵 ❌</p>
<p>生成速度：Seedance 41秒 | 可灵较快 | Sora几分钟 | Veo较慢</p>
<p>价格：可灵 0.99元/5s | Seedance 3.67元/5s | Sora $20/月 | Veo $250/月</p>

<h2>当然不完美</h2>
<p>1. 手还是不行 - AI 视频的通病</p>
<p>2. 太复杂的 prompt 会崩</p>
<p>3. 中文口型还有提升空间</p>

<h2>最后说两句</h2>
<p>AI 视频这个赛道，2024 年是"从无到有"，2025 年是"从有到好"。Seedance 2.0 这一步，标志着 AI 视频开始真正"可用"了——是商用级别的可用。</p>
"""

def get_token():
    url = f"https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={APPID}&secret={SECRET}"
    resp = requests.get(url).json()
    return resp.get("access_token")

def upload_thumb(token):
    """上传封面图"""
    url = f"https://api.weixin.qq.com/cgi-bin/material/add_material?access_token={token}&type=thumb"
    
    png_data = base64.b64decode("iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8/5+hHgAHggJ/PchI7wAAAABJRU5ErkJggg==")
    thumb_path = "/tmp/thumb.png"
    with open(thumb_path, "wb") as f:
        f.write(png_data)
    
    with open(thumb_path, "rb") as f:
        files = {"media": f}
        resp = requests.post(url, files=files)
    
    os.remove(thumb_path)
    return resp.json()

def add_draft(token, thumb_media_id):
    """添加草稿"""
    url = f"https://api.weixin.qq.com/cgi-bin/draft/add?access_token={token}"
    
    data = {
        "articles": [{
            "title": TITLE,
            "content": CONTENT,
            "digest": DIGEST,
            "content_source_url": "",
            "thumb_media_id": thumb_media_id,
            "show_cover_pic": 0,
            "need_open_comment": 1,
            "only_fans_can_comment": 0
        }]
    }
    
    resp = requests.post(url, json=data)
    return resp.json()

def main():
    print("🚀 获取 access_token...")
    token = get_token()
    if not token:
        print("❌ 获取 token 失败")
        return
    print(f"✅ Token 获取成功")
    
    print(f"\n🖼️ 上传封面图...")
    upload_result = upload_thumb(token)
    
    if not upload_result.get("media_id"):
        print(f"❌ 封面上传失败: {upload_result}")
        return
    
    thumb_id = upload_result["media_id"]
    print(f"✅ 封面上传成功")
    
    print(f"\n📝 创建草稿...")
    print(f"标题: {TITLE} ({len(TITLE.encode('utf-8'))} 字节)")
    print(f"摘要: {DIGEST} ({len(DIGEST.encode('utf-8'))} 字节)")
    
    result = add_draft(token, thumb_id)
    print(f"📤 响应: {json.dumps(result, ensure_ascii=False)}")
    
    if result.get("errcode") == 0:
        print(f"\n✅ 草稿创建成功！")
        print(f"media_id: {result.get('media_id')}")
        print(f"\n👉 请登录 https://mp.weixin.qq.com")
        print(f"路径：内容与互动 → 草稿箱")
    else:
        errcode = result.get("errcode")
        errmsg = result.get("errmsg", "")
        print(f"\n❌ 失败: {errmsg}")
        
        if errcode == 45003:
            print("提示: 标题/摘要/内容超出长度限制")

if __name__ == "__main__":
    main()
