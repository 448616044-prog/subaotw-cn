#!/usr/bin/env python3
"""subaotw.cn 百度每日推送 — 从队列推10条最新URL（API日配额10条），标记已推送；over quota 时减半降级重试"""
import requests, os
from datetime import date

BASE = os.path.dirname(os.path.abspath(__file__))
TOKEN = 'zjjGnbA2oufj2XmY'  # ✅ 有效token (2026-07-23)
API = f'http://data.zz.baidu.com/urls?site=www.subaotw.cn&token={TOKEN}'

QUEUE = os.path.join(BASE, 'baidu-push-queue.txt')
PUSHED = os.path.join(BASE, 'baidu-pushed.txt')


def push(urls):
    """推 URL，over quota 时减半降级重试，返回成功条数"""
    batch = urls[:]
    while batch:
        resp = requests.post(API, data='\n'.join(batch), headers={'Content-Type': 'text/plain'},
                             timeout=15, proxies={'http': None, 'https': None})
        try:
            data = resp.json()
        except Exception:
            print(f'  响应异常: {resp.text[:200]}')
            return 0
        msg = str(data.get('message', '')).lower()
        if data.get('error') == 400 and 'over quota' in msg:
            if len(batch) == 1:
                print('  配额已耗尽(over quota)，今日结束')
                return 0
            batch = batch[:len(batch) // 2]
            print(f'  over quota，降级重试 {len(batch)} 条')
            continue
        success = data.get('success', 0)
        remain = data.get('remain', '?')
        print(f'  成功 {success}/{len(batch)}, 剩余配额 {remain}')
        return success
    return 0


def main():
    queue = []
    if os.path.exists(QUEUE):
        with open(QUEUE) as f:
            queue = [line.strip() for line in f if line.strip()]

    pushed_set = set()
    if os.path.exists(PUSHED):
        with open(PUSHED) as f:
            pushed_set = set(line.strip() for line in f if line.strip())

    to_push = [u for u in queue if u not in pushed_set][:10]

    if not to_push:
        print(f'{date.today()} Baidu Push: 队列已空，无新URL可推送')
        return

    print(f'{date.today()} Baidu Push: 待推送 {len(to_push)} 条')
    success = push(to_push)
    if success > 0:
        with open(PUSHED, 'a') as f:
            for u in to_push[:success]:
                f.write(u + '\n')
        print(f'  已标记 {success} 条到 baidu-pushed.txt')


if __name__ == '__main__':
    main()
