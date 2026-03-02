#!/usr/bin/env python3
"""
微信公众号文章抓取脚本
用法: python3 fetch_mp.py <url>
"""

import sys
import re
import subprocess
import json

def fetch_mp(url: str) -> dict:
    # 用 iPhone UA 请求，微信对手机端限制少
    result = subprocess.run([
        'curl', '-s', '-L', url,
        '-H', 'User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15',
        '-H', 'Accept: text/html,application/xhtml+xml',
        '--max-time', '15'
    ], capture_output=True, text=True)

    html = result.stdout
    if not html:
        return {'error': '请求失败，无响应'}

    # 提取标题
    title = ''
    t = re.search(r'<h1[^>]*class="[^"]*rich_media_title[^"]*"[^>]*>(.*?)</h1>', html, re.DOTALL)
    if t:
        title = re.sub(r'<[^>]+>', '', t.group(1)).strip()
    if not title:
        t = re.search(r'<title>(.*?)</title>', html)
        if t:
            title = t.group(1).strip()

    # 提取作者/公众号名
    author = ''
    a = re.search(r'var\s+nickname\s*=\s*"([^"]+)"', html)
    if a:
        author = a.group(1)

    # 提取正文（js_content div）
    body = ''
    m = re.search(r'id=["\']js_content["\'][^>]*>(.*?)</div>', html, re.DOTALL)
    if m:
        raw = m.group(1)
        # 去掉所有标签，保留换行
        body = re.sub(r'<br\s*/?>', '\n', raw)
        body = re.sub(r'</p>', '\n', body)
        body = re.sub(r'<[^>]+>', '', body)
        body = re.sub(r'\n{3,}', '\n\n', body)
        body = body.strip()

    if not body:
        return {'error': '未找到正文，可能需要登录或文章已删除', 'title': title}

    return {
        'title': title,
        'author': author,
        'url': url,
        'content': body,
        'length': len(body)
    }


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("用法: python3 fetch_mp.py <微信文章URL>")
        sys.exit(1)

    url = sys.argv[1]
    result = fetch_mp(url)

    if 'error' in result:
        print(f"❌ {result['error']}")
        sys.exit(1)

    print(f"标题: {result['title']}")
    print(f"作者: {result['author']}")
    print(f"字数: {result['length']}")
    print("=" * 50)
    print(result['content'])
