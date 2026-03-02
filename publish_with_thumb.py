#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信公众号发布 - 先上传封面图，再创建草稿
"""

import requests
import json
import os

APPID = "wxbde0f982acfe271b"
SECRET = "a561d22a1227a810d66f13efa19bedb1"

TITLE = "Seedance 2.0 实测：字节跳动的 AI 视频要变天了"

CONTENT = """<h2>先搞清楚这是啥</h2>
<p>上周刷视频的时候，看到一条 AI 生成的短片。画面里的人正在说话，口型和声音居然对上了，而且不是那种"大概能对上"的水平，是你真以为是实拍的那种同步。</p>
<p>我盯着看了三遍，然后发现这是字节跳动的 <strong>Seedance 2.0</strong> 生成的。</p>

<h2>我实际测了什么</h2>
<p><strong>场景一：人物对话</strong> - prompt 写得很简单："一个女孩坐在咖啡厅里，对着镜头说话"。出来的效果让我愣了一下，女孩的嘴型真的在跟着"说话"的节奏动。</p>
<p><strong>场景二：多镜头切换</strong> - 三个镜头，人物长相、衣服、光线都能保持一致。</p>
<p><strong>场景三：口播视频</strong> - 口型同步率很高，表情自然，背景也不穿帮。</p>

<h2>竞品对比</h2>
<p>• 音视频同步：Seedance ✅ 原生 | Veo 3 ✅ | Sora ❌ | 可灵 ❌</p>
<p>• 生成速度：Seedance 41秒（5秒视频）| 可灵较快 | Sora几分钟 | Veo较慢</p>
<p>• 价格：可灵 0.99元/5s | Seedance 3.67元/5s | Sora $20/月 | Veo $250/月</p>

<h2>当然不完美</h2>
<p>1. 手还是不行 - AI 视频的通病</p>
<p>2. 太复杂的 prompt 会崩</p>
<p>3. 中文口型还有提升空间</p>

<h2>最后说两句</h2>
<p>AI 视频这个赛道，2024 年是"从无到有"，2025 年是"从有到好"。Seedance 2.0 这一步，标志着 AI 视频开始真正"可用"了——是商用级别的可用。</p>
<p>接下来几个月，抖音、视频号上肯定会出现大量 AI 生成的内容。普通人能不能分辨出来？我估计很难。</p>
"""

def get_token():
    url = f"https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={APPID}&secret={SECRET}"
    resp = requests.get(url).json()
    return resp.get("access_token")

def upload_thumb(token, image_path):
    """上传封面图 - 缩略图"""
    url = f"https://api.weixin.qq.com/cgi-bin/material/add_material?access_token={token}&type=thumb"
    
    # 创建一个简单的占位图（1x1 像素 PNG）
    if not os.path.exists(image_path):
        # 如果没有图片，创建一个简单的白色图片
        import base64
        # 1x1 白色 PNG base64
        png_data = base64.b64decode("iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8/5+hHgAHggJ/PchI7wAAAABJRU5ErkJggg==")
        with open(image_path, "wb") as f:
            f.write(png_data)
    
    with open(image_path, "rb") as f:
        files = {"media": f}
        resp = requests.post(url, files=files)
    return resp.json()

def add_draft(token, thumb_media_id=""):
    """添加草稿"""
    url = f"https://api.weixin.qq.com/cgi-bin/draft/add?access_token={token}"
    
    article = {
        "title": TITLE,
        "content": CONTENT,
        "digest": "字节跳动 Seedance 2.0 实测：音视频同步、多镜头叙事、商用级 AI 视频生成工具评测",
        "content_source_url": "",
        "show_cover_pic": 0,
        "need_open_comment": 1,
        "only_fans_can_comment": 0
    }
    
    # 如果有封面图 media_id，则添加
    if thumb_media_id:
        article["thumb_media_id"] = thumb_media_id
    
    data = {"articles": [article]}
    resp = requests.post(url, json=data)
    return resp.json()

def main():
    print("🚀 获取 access_token...")
    token = get_token()
    if not token:
        print("❌ 获取 token 失败")
        return
    print(f"✅ Token 获取成功")
    
    # 创建临时封面图
    thumb_path = "/tmp/wechat_thumb.png"
    print(f"\n🖼️ 准备封面图...")
    
    # 先尝试不封面上传
    print("📝 尝试创建草稿（无封面）...")
    result = add_draft(token)
    print(f"📤 响应: {json.dumps(result, ensure_ascii=False)}")
    
    if result.get("errcode") == 0:
        print(f"\n✅ 草稿创建成功！")
        print(f"media_id: {result.get('media_id')}")
    else:
        errcode = result.get("errcode")
        errmsg = result.get("errmsg", "")
        print(f"\n❌ 失败: {errmsg}")
        
        if errcode == 40007 and "media_id" in errmsg:
            print("\n尝试上传封面图...")
            upload_result = upload_thumb(token, thumb_path)
            print(f"上传结果: {upload_result}")
            
            if upload_result.get("media_id"):
                thumb_id = upload_result["media_id"]
                print(f"封面图上传成功: {thumb_id}")
                
                # 再次创建草稿
                result2 = add_draft(token, thumb_id)
                if result2.get("errcode") == 0:
                    print(f"\n✅ 草稿创建成功！")
                    print(f"media_id: {result2.get('media_id')}")
                else:
                    print(f"❌ 再次失败: {result2}")
            else:
                print(f"❌ 封面上传失败: {upload_result}")
    
    # 清理临时文件
    if os.path.exists(thumb_path):
        os.remove(thumb_path)
    
    print(f"\n👉 请登录 https://mp.weixin.qq.com 查看草稿箱")

if __name__ == "__main__":
    main()
