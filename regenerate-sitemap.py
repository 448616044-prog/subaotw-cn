#!/usr/bin/env python3
"""重新生成 sitemap.xml，分散 lastmod 日期模拟自然建站节奏"""
import os, re, sys
from datetime import date, timedelta
from collections import OrderedDict

BASE = os.path.dirname(os.path.abspath(__file__))

# ── 日期分配策略 ──
# 按页面优先级分配不同 "年龄"，模拟自然建站过程
PRIORITY_DAYS = OrderedDict([
    # (路径关键词, 距今天数范围)
    ('/index.html', (55, 60)),                      # 首页 - 最老
    ('/about', (48, 55)),                           # 关于页
    ('/contact', (45, 52)),
    ('/faq', (42, 50)),
    ('/pricing', (42, 50)),
    ('/shipping-price', (42, 50)),
    ('/cn-to-taiwan-landing', (40, 48)),
    ('/moving', (35, 45)),                          # 搬家相关
    ('/furniture', (35, 45)),                       # 家具
    ('/building-materials', (35, 45)),              # 建材
    ('/oversized', (35, 45)),
    ('/heavy', (35, 45)),
    ('/commercial', (35, 45)),
    ('/fcl-container', (35, 45)),
    ('/bulk-cargo', (35, 45)),
    ('/appliance', (30, 40)),
    ('/luggage', (30, 40)),
    ('/equipment/', (30, 40)),                      # equipment 目录
    ('/cases/', (28, 38)),
    ('/city/', (25, 35)),                           # 城市页面
    ('/guide/', (20, 32)),                          # guide 目录
    ('/tw-to-cn/', (18, 30)),                       # 台湾寄大陆核心目录
    ('/blog/city-', (12, 22)),                      # blog 城市页面
    ('/blog/cn-to-tw-', (8, 18)),                   # 大陆到台湾blog
    ('/blog/', (3, 15)),                            # 其他blog - 最新
],)

today = date.today()

def assign_days_ago(url):
    """根据URL匹配优先级分配年龄"""
    for keyword, (min_days, max_days) in PRIORITY_DAYS.items():
        if keyword in url:
            # 在同范围内做轻微随机偏移
            return min_days, max_days
    # 默认：较新
    return 3, 15

# ── 解析现有 sitemap ──
sitemap_path = os.path.join(BASE, 'sitemap.xml')
with open(sitemap_path) as f:
    content = f.read()

# 提取所有 URL 块
urls = re.findall(r'<loc>(https://www\.subaotw\.cn[^<]+)</loc>', content)
print(f'Found {len(urls)} URLs in sitemap')

# ── 为每个 URL 生成自然分散的日期 ──
# 确保同类页面日期不是完全相同的
import hashlib
assigned = {}
for url in urls:
    min_days, max_days = assign_days_ago(url)
    # 用URL hash做确定性偏移，避免每次都不同
    h = int(hashlib.md5(url.encode()).hexdigest(), 16)
    offset = h % (max_days - min_days + 1) if max_days > min_days else 0
    days_ago = min_days + offset
    assigned[url] = days_ago

# ── 生成新 sitemap ──
url_entries = []
for url in urls:
    days = assigned.get(url, 10)
    d = today - timedelta(days=days)
    lastmod = d.isoformat()
    url_entries.append(f'  <url><loc>{url}</loc><lastmod>{lastmod}</lastmod><changefreq>weekly</changefreq><priority>0.8</priority></url>')

sitemap_new = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
sitemap_new += '\n'.join(url_entries)
sitemap_new += '\n</urlset>\n'

# 写入
with open(sitemap_path, 'w') as f:
    f.write(sitemap_new)

# ── 统计 ──
from collections import Counter
date_buckets = Counter()
for url, days in assigned.items():
    bucket = f'{days//5*5}-{(days//5+1)*5-1}天前'
    date_buckets[bucket] += 1

print('\n📊 lastmod 分布统���:')
for bucket in sorted(date_buckets.keys(), key=lambda x: int(x.split('-')[0])):
    print(f'  {bucket}: {date_buckets[bucket]}页')

print(f'\n✅ sitemap.xml 已更新 ({len(urls)} 个URL, 日期范围 {min(assigned.values())}-{max(assigned.values())}天前)')
print(f'   最早: {today - timedelta(days=max(assigned.values()))}')
print(f'   最新: {today - timedelta(days=min(assigned.values()))}')

# ── 同时更新 baidu-push-queue.txt 中的 sitemap 路径（如果存在） ──
queue_path = os.path.join(BASE, 'baidu-push-queue.txt')
if os.path.exists(queue_path):
    push_sitemap = f'https://www.subaotw.cn/sitemap.xml'
    with open(queue_path) as f:
        queue_lines = [l.strip() for l in f if l.strip()]
    if push_sitemap not in queue_lines:
        queue_lines.insert(0, push_sitemap)
        with open(queue_path, 'w') as f:
            f.write('\n'.join(queue_lines) + '\n')
        print(f'✅ sitemap.xml URL 已加入推送队列首位')
