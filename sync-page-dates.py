#!/usr/bin/env python3
"""同步所有HTML页面的日期字段，使其与sitemap一致"""
import os, re, sys
from datetime import date, timedelta

BASE = os.path.dirname(os.path.abspath(__file__))
SITEMAP = os.path.join(BASE, 'sitemap.xml')

# ── 读取 sitemap，建立 URL→lastmod 映射 ──
url_to_lastmod = {}
with open(SITEMAP) as f:
    content = f.read()
    
entries = re.findall(r'<loc>(https://www\.subaotw\.cn[^<]+)</loc>\s*<lastmod>(\d{4}-\d{2}-\d{2})</lastmod>', content, re.DOTALL)
for url, lastmod in entries:
    url_to_lastmod[url] = lastmod

print(f'加载 {len(url_to_lastmod)} 条 sitemap 映射')

# ── 生成 URL → HTML文件路径映射 ──
# 规则: URL路径去掉域名 → 拼接本地路径
# https://www.subaotw.cn/about → about.html
# https://www.subaotw.cn/tw-to-cn/food-shipping → tw-to-cn/food-shipping.html
# https://www.subaotw.cn/ → index.html

def url_to_local_path(url):
    path = url.replace('https://www.subaotw.cn', '').lstrip('/')
    if not path:
        return os.path.join(BASE, 'index.html')
    # 目录路径 → index.html
    local = os.path.join(BASE, path + '.html')
    if os.path.exists(local):
        return local
    # 也可能是目录下的index.html
    local2 = os.path.join(BASE, path, 'index.html')
    if os.path.exists(local2):
        return local2
    return None

# ── 更新每个HTML文件 ──
updated = 0
skipped = 0
for url, lastmod in url_to_lastmod.items():
    local = url_to_local_path(url)
    if not local:
        skipped += 1
        continue
    
    with open(local, 'r') as f:
        html = f.read()
    
    original = html
    
    # 1. 更新 <meta name="lastmod">
    html = re.sub(
        r'<meta name="lastmod" content="[^"]*"',
        f'<meta name="lastmod" content="{lastmod}"',
        html
    )
    
    # 2. 更新 JSON-LD datePublished → 用lastmod（因为这是实际存在的第一版）
    # 只更新 Article/WebPage Schema 的 datePublished
    html = re.sub(
        r'"datePublished":\s*"[^"]*"',
        f'"datePublished": "{lastmod}"',
        html
    )
    html = re.sub(
        r'"dateModified":\s*"[^"]*"',
        f'"dateModified": "{lastmod}"',
        html
    )
    
    # 3. 更新 upDate (自定义字段)
    html = re.sub(
        r'"upDate":\s*"[^"]*"',
        f'"upDate": "{lastmod}T00:00:00"',
        html
    )
    
    if html != original:
        with open(local, 'w') as f:
            f.write(html)
        updated += 1

print(f'\n✅ 已更新: {updated} 页')
print(f'⏭️ 跳过(无映射): {skipped} 页')

# ── 验证 ──
print(f'\n📋 抽查验证:')
for check_url in [
    'https://www.subaotw.cn/',
    'https://www.subaotw.cn/about',
    'https://www.subaotw.cn/tw-to-cn/food-shipping',
    'https://www.subaotw.cn/blog/taiwan-moving-to-mainland-2026',
]:
    local = url_to_local_path(check_url)
    if local and os.path.exists(local):
        with open(local) as f:
            content = f.read()
        lastmod_match = re.search(r'<meta name="lastmod" content="([^"]*)"', content)
        published = re.search(r'"datePublished":\s*"([^"]*)"', content)
        print(f'  {check_url.split("/")[-1] or "index"}: lastmod={lastmod_match.group(1) if lastmod_match else "N/A"}, published={published.group(1) if published else "N/A"}')
