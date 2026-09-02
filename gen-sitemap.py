#!/usr/bin/env python3
"""Generate sitemap.xml for subaotw.cn"""
import glob, os
from datetime import date

BASE = os.path.dirname(os.path.abspath(__file__))

urls = []
for f in sorted(glob.glob(f'{BASE}/**/*.html', recursive=True)):
    if '404' in f or 'google' in f:
        continue
    path = f.replace(BASE, '').replace('/index.html', '/').replace('.html', '')
    if path == '/index':
        path = '/'
    urls.append(f'https://www.subaotw.cn{path}')

today = date.today().isoformat()
xml = ['<?xml version="1.0" encoding="UTF-8"?>',
       '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for u in urls:
    xml.append(f'  <url><loc>{u}</loc><lastmod>{today}</lastmod><changefreq>weekly</changefreq><priority>0.8</priority></url>')
xml.append('</urlset>')

spath = os.path.join(BASE, 'sitemap.xml')
with open(spath, 'w') as f:
    f.write('\n'.join(xml))
print(f'subaotw.cn sitemap: {len(urls)} URLs')
