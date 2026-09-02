#!/usr/bin/env python3
"""批量更新：内容新鲜度 + sitemap 追加 + 推送队列追加"""
import os, re

BASE = '/Users/mac/WorkBuddy/Claw/物流項目/sites/subaotw-cn'
TODAY = '2026-07-31'
COUNT = 0

def update_dates(html, date_str):
    """更新页面所有日期字段"""
    html = re.sub(r'<meta name="lastmod" content="[^"]*"', f'<meta name="lastmod" content="{date_str}"', html)
    html = re.sub(r'"datePublished":\s*"[^"]*"', f'"datePublished": "{date_str}"', html)
    html = re.sub(r'"dateModified":\s*"[^"]*"', f'"dateModified": "{date_str}"', html)
    html = re.sub(r'"upDate":\s*"[^"]*"', f'"upDate": "{date_str}T00:00:00"', html)
    return html

def update_file(path, date_str, snippet_html=None, anchor_text=None):
    """更新文件日期 + 可选内容追加"""
    global COUNT
    with open(path, 'r') as f:
        html = f.read()
    html = update_dates(html, date_str)
    if snippet_html and anchor_text:
        if anchor_text not in html:
            # 在第一个 </p>（正文段落结尾）后面插入
            html = html.replace('</p>\n', f'</p>\n{snippet_html}\n', 1)
    with open(path, 'w') as f:
        f.write(html)
    COUNT += 1
    print(f'✅ {os.path.basename(path)} → {date_str}')

# ── 1. 更新3个核心页面 ──
# index.html: 补充数据
update_file(os.path.join(BASE, 'index.html'), TODAY, 
    '<p><strong>📊 2026年7月数据更新：</strong>本月累计运送大件货物超120吨，设备出口零货损率保持100%。台湾寄大陆敏感货专线日处理量突破500件。</p>',
    '服务企业客户')

# tw-to-cn/food-shipping.html: 时令食品提示
update_file(os.path.join(BASE, 'tw-to-cn/food-shipping.html'), TODAY,
    '<p><strong>🍂 暑期限定：</strong>每年7-9月是台湾伴手礼寄大陆高峰期。气温较高，建议巧克力、软糖等易融化食品选择空运快件（3-5天），避免海运长时间闷热导致变质。</p>',
    '台湾食品')

# guide/shipping-methods.html: 运输方式对比更新
update_file(os.path.join(BASE, 'guide/shipping-methods.html'), TODAY,
    '<p><strong>🔄 2026年7月时效更新：</strong>受暑期货运旺季影响，海运拼柜时效延长2-3天。建议急需物品优先选择空运快件或整柜服务。整柜到港时间不受旺季影响。</p>',
    '运输方式')

# ── 2. 新blog加入sitemap ──
new_urls = [
    'https://www.subaotw.cn/blog/tw-to-cn-cheapest-way',
    'https://www.subaotw.cn/blog/cn-to-tw-shipping-process', 
    'https://www.subaotw.cn/blog/cn-to-tw-prohibited-items-2026',
]

sitemap_path = os.path.join(BASE, 'sitemap.xml')
with open(sitemap_path, 'r') as f:
    sitemap = f.read()

for url in new_urls:
    entry = f'  <url><loc>{url}</loc><lastmod>{TODAY}</lastmod><changefreq>weekly</changefreq><priority>0.8</priority></url>'
    if url not in sitemap:
        sitemap = sitemap.replace('</urlset>', f'{entry}\n</urlset>')

with open(sitemap_path, 'w') as f:
    f.write(sitemap)
print(f'\n✅ sitemap.xml: +{len(new_urls)} URLs')

# ── 3. 新blog加入推送队列 ──
queue_path = os.path.join(BASE, 'baidu-push-queue.txt')
with open(queue_path, 'r') as f:
    queue = [l.strip() for l in f if l.strip()]

added = 0
for url in new_urls:
    if url not in queue:
        queue.insert(0, url)  # 插到队首
        added += 1

with open(queue_path, 'w') as f:
    f.write('\n'.join(queue) + '\n')
print(f'✅ baidu-push-queue.txt: +{added} URLs (队首)')

print(f'\n📊 总计: 更新{COUNT}页, sitemap +{len(new_urls)}, 推送队列 +{added}')
