#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信公众号 API 发布脚本 - 草稿箱接口
"""

import requests
import json
import sys

# 配置
APPID = "wxbde0f982acfe271b"
SECRET = "a561d22a1227a810d66f13efa19bedb1"

# 文章内容
TITLE = "Seedance 2.0 实测：字节跳动的 AI 视频要变天了"

CONTENT_HTML = """<p>上周刷视频的时候，看到一条 AI 生成的短片。画面里的人正在说话，口型和声音居然对上了，而且不是那种"大概能对上"的水平，是你真以为是实拍的那种同步。</p>

<p>我盯着看了三遍，然后发现这是字节跳动的 <strong>Seedance 2.0</strong> 生成的。</p>

<p>作为用过 Sora、可灵、Runway 的老玩家，我当时就一个感觉：这不对啊，怎么突然这么强了？</p>

<h2>先搞清楚这是啥</h2>

<p>Seedance 不是新东西，字节在 2025 年 6 月就发布了 1.0 版本。那时候主打的是"多镜头叙事"和"超快生成"——5 秒视频只要 41 秒，比竞品快 10 倍。</p>

<p>但说实话，1.0 版本我用过几次，质量可以，但还没到让我想付费的程度。</p>

<p><strong>Seedance 2.0 不一样。</strong>最大的升级就两个字：音视频同步。不是后期配个音那种，是画面和声音一起生成，嘴型、表情、气息全都对得上。</p>

<h2>我实际测了什么</h2>

<p><strong>场景一：人物对话</strong></p>

<p>prompt 写得很简单："一个女孩坐在咖啡厅里，对着镜头说话，介绍她今天的心情。"</p>

<p>出来的效果让我愣了一下。女孩的嘴型真的在跟着"说话"的节奏动，不是那种机械的开合，是有轻重缓急的。表情也会随着语气变化——说到开心的时候眼睛弯起来，说到烦恼的时候眉头微皱。</p>

<p>这跟我之前用的 AI 视频完全是两回事。以前的模型，人物动起来要么像机器人，要么像皮影戏。Seedance 2.0 这个，能看出"表演"的感觉。</p>

<p><strong>场景二：多镜头切换</strong></p>

<p>这个是从 1.0 继承的能力，但 2.0 更稳了。我试了"从远景切换到特写，再转到侧面角度"这种指令。出来的三个镜头，人物长相、衣服、光线都能保持一致。不会出现"切个镜头换个人"的尴尬。</p>

<p><strong>场景三：口播视频</strong></p>

<p>这个是我最惊讶的。Seedance 2.0 生成的结果，直接能用。口型同步率很高，表情自然，背景也不穿帮。当然，仔细看还是能看出不是真人，但放在抖音、视频号里，普通用户根本分辨不出来。</p>

<h2>它到底比别家强在哪</h2>

<p><strong>竞品对比：</strong>Seedance 2.0 vs Sora vs 可灵 2.0 vs Veo 3</p>

<p>• 音视频同步：Seedance ✅ 原生 | Veo 3 ✅ | Sora ❌ | 可灵 ❌</p>

<p>• 生成速度：Seedance 41秒（5秒视频）| 可灵较快 | Sora几分钟 | Veo较慢</p>

<p>• 价格：可灵 0.99元/5s（最便宜）| Seedance 3.67元/5s | Sora $20/月 | Veo $250/月</p>

<p>Seedance 2.0 的定价在中间，但音视频同步这个功能，目前独一份（除了超贵的 Veo 3）。</p>

<h2>当然不完美</h2>

<p><strong>第一，手还是不行。</strong>AI 视频的通病，手部动作复杂的时候，偶尔还是会出现"手指粘连"或者"多一根手指"的情况。</p>

<p><strong>第二，太复杂的 prompt 会崩。</strong>三个人在房间里吵架，人物位置关系是乱的。</p>

<p><strong>第三，中文口型还有提升空间。</strong>英文同步很好，中文某些发音（比如"ü"）还差一点点。</p>

<h2>谁会需要这个</h2>

<p><strong>短视频创作者：</strong>做口播、剧情号的人，以后可能不需要真人出镜了。</p>

<p><strong>电商卖家：</strong>产品介绍视频，以前要拍要剪，现在几分钟出片。</p>

<p><strong>广告代理：</strong>给客户看 concept，以前做 storyboard，现在直接出动态 demo。</p>

<p><strong>独立 filmmaker：</strong>可以用 AI 生成空镜或概念片段，减少实拍成本。</p>

<h2>最后说两句</h2>

<p>AI 视频这个赛道，2024 年是"从无到有"，2025 年是"从有到好"。Seedance 2.0 这一步，标志着 AI 视频开始真正"可用"了——是商用级别的可用。</p>

<p>当然，说"取代真人拍摄"还太早。光线、质感、情绪的细腻程度，AI 还差得远。但作为一个工具，它已经可以帮创作者省掉 80% 的重复劳动了。</p>

<p>接下来几个月，抖音、视频号上肯定会出现大量 AI 生成的内容。普通人能不能分辨出来？我估计很难。技术迭代太快了。上个月还觉得"这明显是 AI 做的"，这个月就已经"真假难辨"了。</p>

<p><br/></p>

<p>CHANGELOG<br/>2025.06：Seedance 1.0 发布<br/>2025.12：Seedance 1.5 Pro 发布<br/>2026.02：Seedance 2.0 发布</p>"""

def get_access_token():
    """获取 access_token"""
    url = f"https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={APPID}&secret={SECRET}"
    response = requests.get(url)
    data = response.json()
    
    if "access_token" in data:
        print(f"✅ 获取 token 成功")
        return data["access_token"]
    else:
        print(f"❌ 获取 token 失败: {data}")
        return None

def add_draft(access_token, title, content):
    """新增草稿（draft/add 接口）"""
    url = f"https://api.weixin.qq.com/cgi-bin/draft/add?access_token={access_token}"
    
    # 构造图文消息 - 不包含 thumb_media_id
    data = {
        "articles": [
            {
                "title": title,
                "content": content,
                "digest": "字节跳动 Seedance 2.0 实测：音视频同步、多镜头叙事、商用级 AI 视频生成工具评测",
                "content_source_url": "",
                "show_cover_pic": 0,
                "need_open_comment": 1,
                "only_fans_can_comment": 0
            }
        ]
    }
    
    response = requests.post(url, json=data)
    result = response.json()
    
    return result

def main():
    print("🚀 开始发布到微信公众号草稿箱...\n")
    
    # 1. 获取 token
    access_token = get_access_token()
    if not access_token:
        sys.exit(1)
    
    print(f"\n文章标题: {TITLE}")
    print(f"内容长度: {len(CONTENT_HTML)} 字符\n")
    
    # 2. 添加到草稿
    result = add_draft(access_token, TITLE, CONTENT_HTML)
    print(f"API 返回: {json.dumps(result, ensure_ascii=False)}")
    
    if result.get("errcode") == 0 and "media_id" in result:
        media_id = result["media_id"]
        print(f"\n✅ 草稿创建成功！")
        print(f"media_id: {media_id}")
        print(f"\n请前往公众号后台查看：")
        print(f"https://mp.weixin.qq.com")
        print(f"\n路径：内容与互动 → 草稿箱")
    else:
        errcode = result.get("errcode")
        errmsg = result.get("errmsg", "未知错误")
        print(f"\n❌ 创建草稿失败")
        print(f"错误码: {errcode}")
        print(f"错误信息: {errmsg}")

if __name__ == "__main__":
    main()
