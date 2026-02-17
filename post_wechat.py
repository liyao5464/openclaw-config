#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信公众号 API 发布脚本
"""

import requests
import json
import sys

# 配置
APPID = "wxbde0f982acfe271b"
SECRET = "a561d22a1227a810d66f13efa19bedb1"

# 文章内容
TITLE = "Seedance 2.0 实测：字节跳动的 AI 视频要变天了"

CONTENT_HTML = """
<p style="font-size:16px;line-height:1.8;color:#333;margin:0 0 16px 0;">上周刷视频的时候，看到一条 AI 生成的短片。画面里的人正在说话，口型和声音居然对上了，而且不是那种"大概能对上"的水平，是你真以为是实拍的那种同步。</p>

<p style="font-size:16px;line-height:1.8;color:#333;margin:0 0 16px 0;">我盯着看了三遍，然后发现这是字节跳动的 <strong>Seedance 2.0</strong> 生成的。</p>

<p style="font-size:16px;line-height:1.8;color:#333;margin:0 0 24px 0;">作为用过 Sora、可灵、Runway 的老玩家，我当时就一个感觉：这不对啊，怎么突然这么强了？</p>

<h2 style="font-size:18px;color:#1976d2;margin:24px 0 12px 0;font-weight:bold;">先搞清楚这是啥</h2>

<p style="font-size:16px;line-height:1.8;color:#333;margin:0 0 16px 0;">Seedance 不是新东西，字节在 2025 年 6 月就发布了 1.0 版本。那时候主打的是"多镜头叙事"和"超快生成"——5 秒视频只要 41 秒，比竞品快 10 倍。</p>

<p style="font-size:16px;line-height:1.8;color:#333;margin:0 0 16px 0;">但说实话，1.0 版本我用过几次，质量可以，但还没到让我想付费的程度。</p>

<p style="font-size:16px;line-height:1.8;color:#333;margin:0 0 16px 0;"><strong>Seedance 2.0 不一样。</strong>最大的升级就两个字：<span style="color:#d32f2f;font-weight:bold;">音视频同步</span>。不是后期配个音那种，是画面和声音一起生成，嘴型、表情、气息全都对得上。</p>

<h2 style="font-size:18px;color:#1976d2;margin:24px 0 12px 0;font-weight:bold;">我实际测了什么</h2>

<p style="font-size:16px;line-height:1.8;color:#333;margin:0 0 12px 0;"><strong>场景一：人物对话</strong></p>

<p style="font-size:16px;line-height:1.8;color:#333;margin:0 0 16px 0;background:#f5f5f5;padding:10px;border-radius:4px;">prompt 写得很简单："一个女孩坐在咖啡厅里，对着镜头说话，介绍她今天的心情。"</p>

<p style="font-size:16px;line-height:1.8;color:#333;margin:0 0 16px 0;">出来的效果让我愣了一下。女孩的嘴型真的在跟着"说话"的节奏动，不是那种机械的开合，是有轻重缓急的。表情也会随着语气变化——说到开心的时候眼睛弯起来，说到烦恼的时候眉头微皱。</p>

<p style="font-size:16px;line-height:1.8;color:#333;margin:0 0 16px 0;">这跟我之前用的 AI 视频完全是两回事。以前的模型，人物动起来要么像机器人，要么像皮影戏。Seedance 2.0 这个，能看出"表演"的感觉。</p>

<p style="font-size:16px;line-height:1.8;color:#333;margin:0 0 12px 0;"><strong>场景二：多镜头切换</strong></p>

<p style="font-size:16px;line-height:1.8;color:#333;margin:0 0 16px 0;">这个是从 1.0 继承的能力，但 2.0 更稳了。我试了"从远景切换到特写，再转到侧面角度"这种指令。出来的三个镜头，人物长相、衣服、光线都能保持一致。不会出现"切个镜头换个人"的尴尬。</p>

<p style="font-size:16px;line-height:1.8;color:#333;margin:0 0 12px 0;"><strong>场景三：口播视频</strong></p>

<p style="font-size:16px;line-height:1.8;color:#333;margin:0 0 16px 0;">这个是我最惊讶的。Seedance 2.0 生成的结果，直接能用。口型同步率很高，表情自然，背景也不穿帮。当然，仔细看还是能看出不是真人，但放在抖音、视频号里，普通用户根本分辨不出来。</p>

<h2 style="font-size:18px;color:#1976d2;margin:24px 0 12px 0;font-weight:bold;">竞品对比</h2>

<p style="font-size:16px;line-height:1.8;color:#333;margin:0 0 8px 0;"><strong>Seedance 2.0</strong> vs <strong>Sora</strong> vs <strong>可灵 2.0</strong> vs <strong>Veo 3</strong></p>

<p style="font-size:16px;line-height:1.8;color:#333;margin:0 0 8px 0;">• 音视频同步：Seedance ✅ 原生支持 | Veo 3 ✅ | Sora ❌ | 可灵 ❌</p>

<p style="font-size:16px;line-height:1.8;color:#333;margin:0 0 8px 0;">• 生成速度：Seedance 41秒（5秒视频）| 可灵较快 | Sora几分钟 | Veo较慢</p>

<p style="font-size:16px;line-height:1.8;color:#333;margin:0 0 8px 0;">• 价格：可灵 0.99元/5s（最便宜）| Seedance 3.67元/5s | Sora $20/月 | Veo $250/月</p>

<p style="font-size:16px;line-height:1.8;color:#333;margin:0 0 16px 0;">Seedance 2.0 的定价在中间，但音视频同步这个功能，目前独一份（除了超贵的 Veo 3）。</p>

<h2 style="font-size:18px;color:#1976d2;margin:24px 0 12px 0;font-weight:bold;">当然不完美</h2>

<p style="font-size:16px;line-height:1.8;color:#333;margin:0 0 8px 0;"><strong>第一，手还是不行。</strong>AI 视频的通病，手部动作复杂的时候，偶尔还是会出现"手指粘连"或者"多一根手指"的情况。</p>

<p style="font-size:16px;line-height:1.8;color:#333;margin:0 0 8px 0;"><strong>第二，太复杂的 prompt 会崩。</strong>三个人在房间里吵架，人物位置关系是乱的。</p>

<p style="font-size:16px;line-height:1.8;color:#333;margin:0 0 16px 0;"><strong>第三，中文口型还有提升空间。</strong>英文同步很好，中文某些发音（比如"ü"）还差一点点。</p>

<h2 style="font-size:18px;color:#1976d2;margin:24px 0 12px 0;font-weight:bold;">谁会需要这个</h2>

<p style="font-size:16px;line-height:1.8;color:#333;margin:0 0 8px 0;"><strong>短视频创作者</strong>：做口播、剧情号的人，以后可能不需要真人出镜了。</p>

<p style="font-size:16px;line-height:1.8;color:#333;margin:0 0 8px 0;"><strong>电商卖家</strong>：产品介绍视频，以前要拍要剪，现在几分钟出片。</p>

<p style="font-size:16px;line-height:1.8;color:#333;margin:0 0 8px 0;"><strong>广告代理</strong>：给客户看 concept，以前做 storyboard，现在直接出动态 demo。</p>

<p style="font-size:16px;line-height:1.8;color:#333;margin:0 0 16px 0;"><strong>独立 filmmaker</strong>：可以用 AI 生成空镜或概念片段，减少实拍成本。</p>

<div style="background:#fff3e0;border-left:4px solid #ff9800;padding:12px 16px;margin:20px 0;">
<p style="font-size:16px;line-height:1.8;color:#e65100;margin:0;font-weight:bold;">最后说两句</p>
<p style="font-size:16px;line-height:1.8;color:#333;margin:8px 0 0 0;">AI 视频这个赛道，2024 年是"从无到有"，2025 年是"从有到好"。Seedance 2.0 这一步，标志着 AI 视频开始真正"可用"了——是商用级别的可用。</p>
</div>

<p style="font-size:16px;line-height:1.8;color:#333;margin:16px 0;">当然，说"取代真人拍摄"还太早。光线、质感、情绪的细腻程度，AI 还差得远。但作为一个工具，它已经可以帮创作者省掉 80% 的重复劳动了。</p>

<p style="font-size:16px;line-height:1.8;color:#333;margin:16px 0;">接下来几个月，抖音、视频号上肯定会出现大量 AI 生成的内容。普通人能不能分辨出来？我估计很难。技术迭代太快了。上个月还觉得"这明显是 AI 做的"，这个月就已经"真假难辨"了。</p>

<p style="font-size:14px;line-height:1.6;color:#666;margin:20px 0 0 0;padding-top:16px;border-top:1px solid #e0e0e0;">
CHANGELOG<br/>
2025.06：Seedance 1.0 发布<br/>
2025.12：Seedance 1.5 Pro 发布<br/>
2026.02：Seedance 2.0 发布
</p>
"""

def get_access_token():
    """获取 access_token"""
    url = f"https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={APPID}&secret={SECRET}"
    response = requests.get(url)
    data = response.json()
    
    if "access_token" in data:
        print(f"✅ 获取 token 成功，有效期 {data.get('expires_in', 7200)} 秒")
        return data["access_token"]
    else:
        print(f"❌ 获取 token 失败: {data}")
        return None

def add_news(access_token, title, content):
    """新增图文素材（保存为草稿）"""
    url = f"https://api.weixin.qq.com/cgi-bin/material/add_news?access_token={access_token}"
    
    # 构造图文消息
    data = {
        "articles": [
            {
                "title": title,
                "thumb_media_id": "",  # 封面图 media_id，可选
                "author": "AI前沿观察",
                "digest": "字节跳动 Seedance 2.0 实测：音视频同步、多镜头叙事、商用级 AI 视频生成工具评测",  # 摘要
                "content": content,
                "content_source_url": "",
                "show_cover_pic": 0
            }
        ]
    }
    
    response = requests.post(url, json=data)
    result = response.json()
    
    if "media_id" in result:
        print(f"✅ 文章发布成功！")
        print(f"media_id: {result['media_id']}")
        return result["media_id"]
    else:
        print(f"❌ 发布失败: {result}")
        return None

def main():
    print("🚀 开始发布到微信公众号...\n")
    
    # 1. 获取 token
    access_token = get_access_token()
    if not access_token:
        sys.exit(1)
    
    print(f"\n文章标题: {TITLE}")
    print(f"内容长度: {len(CONTENT_HTML)} 字符\n")
    
    # 2. 发布文章
    media_id = add_news(access_token, TITLE, CONTENT_HTML)
    
    if media_id:
        print(f"\n✅ 完成！文章已保存为永久素材")
        print(f"可以在公众号后台的『素材管理』中找到这篇文章")
    else:
        print("\n❌ 发布失败，请检查错误信息")

if __name__ == "__main__":
    main()
