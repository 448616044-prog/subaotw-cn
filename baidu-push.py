#!/usr/bin/env python3
"""百度主动推送脚本 — 双token每日20条配额"""
import urllib.request
import os

TOKENS = [
    "UAVg0xt7rxpTjzaL",
    "zjjGnbA2oufj2XmY",
]
BASE = "http://data.zz.baidu.com/urls?site=https://www.subaotw.cn&token="

def push_urls(url_list, token):
    """推送URL列表到百度，返回结果"""
    data = "\n".join(url_list).encode('utf-8')
    api = BASE + token
    req = urllib.request.Request(api, data=data, 
                                  headers={"Content-Type": "text/plain"})
    resp = urllib.request.urlopen(req, timeout=30)
    return resp.read().decode()

def collect_all_urls():
    """收集站点所有页面URL（不含index/404）"""
    urls = []
    for root, dirs, files in os.walk("."):
        dirs[:] = [d for d in dirs if d not in ('.git',)]
        for f in files:
            if f.endswith('.html') and f != '404.html':
                path = os.path.join(root, f).replace('./', '')
                if path.endswith('/index.html'):
                    # /equipment/index.html → /equipment/
                    path = path.replace('/index.html', '/')
                else:
                    path = path.replace('.html', '')
                urls.append(f"https://www.subaotw.cn/{path}")
    return sorted(urls)

if __name__ == "__main__":
    all_urls = collect_all_urls()
    print(f"Total: {len(all_urls)} URLs")
    
    # Dual token: each 10/day = 20 total
    for t, token in enumerate(TOKENS):
        batch = 10
        for i in range(0, min(batch, len(all_urls)), batch):
            chunk = all_urls[t*batch + i:t*batch + i + batch]
            try:
                result = push_urls(chunk, token)
                print(f"Token{t+1} Batch{t+1} ({len(chunk)} URLs): {result}")
            except Exception as e:
                print(f"Token{t+1} error: {e}")
