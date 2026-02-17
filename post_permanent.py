#!/usr/bin/env python3
"""
尝试使用 material/upload 上传永久图片，再用 draft/add
"""
import requests
import io

APPID = "wxbde0f982acfe271b"
SECRET = "a561d22a1227a810d66f13efa19bedb1"

# 获取 token
token_url = f"https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={APPID}&secret={SECRET}"
token = requests.get(token_url, timeout=30).json().get('access_token')
print(f"✅ Token: {token[:30]}...")

# 创建一个稍微大一点的 JPEG 图片数据（2x2 像素棕色）
# 这是一个更完整的 JPEG 文件
jpeg_data = bytes.fromhex(
    'FFD8FFE000104A46494600010100000100010000FFDB0043000806060706050807'
    '07070909080A0C14100C0B0B0C1912130F141D1A1F1E1D1A1C1C20242E2720222C'
    '231C1C2837292C30313434341F27393D38323C2E333432FFC0000B080002000201'
    '011110FFC4011F0000010501010101010100000000000000010203040506070809'
    '0A0BFFC400B5100002010303020403050504040000017D01020300041105122131'
    '410613516107227114328191A1082342B1C11552D1F02433627282090A16171819'
    '1A25262728292A3435363738393A434445464748494A535455565758595A636465'
    '666768696A737475767778797A838485868788898A92939495969798999AA2A3A4'
    'A5A6A7A8A9AAB2B3B4B5B6B7B8B9BAC2C3C4C5C6C7C8C9CAD2D3D4D5D6D7D8D9'
    'DAE1E2E3E4E5E6E7E8E9EAF1F2F3F4F5F6F7F8F9FAFFC4001F0100030101010101'
    '010101010000000000000102030405060708090A0BFFC400B5110002010204040304'
    '0705040400010277000102031104052131061241510761711322328108144291A1B1'
    'C109233352F0156272D10A162434E125F11718191A262728292A35363738393A4344'
    '45464748494A535455565758595A636465666768696A737475767778797A82838485'
    '868788898A92939495969798999AA2A3A4A5A6A7A8A9AAB2B3B4B5B6B7B8B9BAC2'
    'C3C4C5C6C7C8C9CAD2D3D4D5D6D7D8D9DAE2E3E4E5E6E7E8E9EAF2F3F4F5F6F7'
    'F8F9FAFFDA0008010100013F00FFD9'
)

print(f"📤 上传永久图片（{len(jpeg_data)} 字节）...")
upload_url = f"https://api.weixin.qq.com/cgi-bin/material/add_material?access_token={token}&type=thumb"
files = {'media': ('cover.jpg', io.BytesIO(jpeg_data), 'image/jpeg')}
resp = requests.post(upload_url, files=files, timeout=30).json()
print(f"上传结果: {resp}")

if 'media_id' in resp:
    media_id = resp['media_id']
    print(f"✅ 永久图片上传成功: {media_id}")
    
    # 创建草稿
    print("\n📝 创建草稿...")
    draft_url = f"https://api.weixin.qq.com/cgi-bin/draft/add?access_token={token}"
    
    # 读取文章内容
    with open('/root/.openclaw/workspace/2026-chunwan-wechat-final.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    data = {
        "articles": [{
            "title": "看完春晚，我发现自己被时代甩了一截",
            "content": content,
            "author": "老里",
            "digest": "昨晚看完春晚，最大的感受是AI含量爆表！有几个节目美得令人瞠目...",
            "thumb_media_id": media_id,
            "need_open_comment": 1,
            "only_fans_can_comment": 0
        }]
    }
    
    draft_resp = requests.post(draft_url, json=data, timeout=30).json()
    print(f"\n草稿结果: {draft_resp}")
    
    if 'media_id' in draft_resp:
        print(f"\n🎉 发布成功！Media ID: {draft_resp['media_id']}")
    else:
        print(f"\n❌ 创建失败: {draft_resp}")
else:
    print("❌ 永久图片上传失败")
