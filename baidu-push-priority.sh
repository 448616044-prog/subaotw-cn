#!/bin/bash
# 高优先级百度推送 — 凌晨00:01执行，抢每日配额
# 推送顺序：sitemap → hub页 → 高价值新内容 → 常规内容

API="http://data.zz.baidu.com/urls?site=https://www.subaotw.cn&token=UAVg0xt7rxpTjzaL"
LOG="/tmp/baidu-push-priority.log"
PUSH_LOG="/Users/mac/WorkBuddy/Claw/物流項目/baidu-push-log.md"

# 优先URL列表 — 按价值排序，前10条每次推送
# Day 1-3: sitemap + hub + 7/2新内容（8篇高价值移植）
# Day 4+: 常规页面按品类推进
URLS=(
  # === 批次1: 基础设施（Baiduspider入口）===
  "https://www.subaotw.cn/sitemap.xml"
  "https://www.subaotw.cn/"
  "https://www.subaotw.cn/article-list"
  "https://www.subaotw.cn/tw-to-cn/"

  # === 批次2: 高价值新内容 ===
  "https://www.subaotw.cn/blog/cn-to-tw-shipping-guide"
  "https://www.subaotw.cn/blog/food-shipping-guide"
  "https://www.subaotw.cn/blog/noodles-ramen-shipping"
  "https://www.subaotw.cn/blog/tea-shipping-guide"
  "https://www.subaotw.cn/blog/cosmetics-shipping"
  "https://www.subaotw.cn/blog/electronics-shipping"
  "https://www.subaotw.cn/blog/health-products-shipping"
  "https://www.subaotw.cn/blog/battery-products-shipping"
  "https://www.subaotw.cn/blog/tw-to-cn-prohibited-items"

  # === 批次3: 台湾→大陆核心品类页 ===
  "https://www.subaotw.cn/tw-to-cn/noodles-to-cn"
  "https://www.subaotw.cn/tw-to-cn/taiwan-snacks-to-cn"
  "https://www.subaotw.cn/tw-to-cn/birds-nest-to-cn"
  "https://www.subaotw.cn/tw-to-cn/perfume-to-cn"
  "https://www.subaotw.cn/tw-to-cn/chinese-medicine-to-cn"
  "https://www.subaotw.cn/tw-to-cn/glucose-meter-to-cn"
  "https://www.subaotw.cn/tw-to-cn/homemade-food-to-cn"
  "https://www.subaotw.cn/tw-to-cn/commercial-goods-to-cn"
  "https://www.subaotw.cn/tw-to-cn/computer-parts-to-cn"

  # === 批次4: 大陆→台湾品类页 ===
  "https://www.subaotw.cn/blog/clothes-to-taiwan"
  "https://www.subaotw.cn/blog/food-to-taiwan"
  "https://www.subaotw.cn/blog/furniture-to-taiwan"
  "https://www.subaotw.cn/blog/home-appliances-to-taiwan"
  "https://www.subaotw.cn/blog/daily-items-to-taiwan"
  "https://www.subaotw.cn/blog/phone-to-taiwan"

  # === 批次5: 指南/工具页 ===
  "https://www.subaotw.cn/tw-to-cn/customs-tax-guide"
  "https://www.subaotw.cn/tw-to-cn/personal-items-to-cn"
  "https://www.subaotw.cn/tw-to-cn/shipping-channel-compare"
  "https://www.subaotw.cn/tw-to-cn/taiwanese-in-china-guide"
  "https://www.subaotw.cn/guide/"
  "https://www.subaotw.cn/tw-to-cn/jewelry-crystal"

  # === 批次6: 设备出口页（大陆→台湾）===
  "https://www.subaotw.cn/equipment/"
  "https://www.subaotw.cn/heavy-machinery"
  "https://www.subaotw.cn/building-materials-taiwan"
  "https://www.subaotw.cn/bulk-cargo-taiwan"
  "https://www.subaotw.cn/moving-taiwan"
  "https://www.subaotw.cn/luggage-shipping"
  "https://www.subaotw.cn/moving-from-taiwan"
  "https://www.subaotw.cn/oversized-cargo"

  # === 批次7: 剩余页面 ===
  "https://www.subaotw.cn/appliance-shipping"
  "https://www.subaotw.cn/blog/shipping-fee-guide"
  "https://www.subaotw.cn/blog/express-compare-guide"
  "https://www.subaotw.cn/blog/gaming-console-to-taiwan"
  "https://www.subaotw.cn/blog/prohibited-items-2026"
  "https://www.subaotw.cn/tw-to-cn/battery-products"
)

# 取前10个
BATCH=$(printf '%s\n' "${URLS[@]}" | head -10)
DATA=$(printf '%s\n' "${URLS[@]}" | head -10)

RESP=$(curl -s -w "\n%{http_code}" -H "Content-Type: text/plain" --data "$DATA" "$API" 2>&1)
CODE=$(echo "$RESP" | tail -1)
BODY=$(echo "$RESP" | head -1)

TS=$(date '+%Y-%m-%d %H:%M:%S')
echo "[$TS] HTTP $CODE: $BODY" >> "$LOG"

if echo "$BODY" | grep -q '"success"'; then
    echo "✅ 推送成功" >> "$LOG"
    # 同步写主日志
    echo "## $TS — 凌晨推送" >> "$PUSH_LOG"
    echo "- **推送URL数**: 10" >> "$PUSH_LOG"
    echo "- **API返回**: $BODY" >> "$PUSH_LOG"
    echo "- **状态**: ✅ 成功" >> "$PUSH_LOG"
    echo "" >> "$PUSH_LOG"
else
    echo "❌ $BODY" >> "$LOG"
    echo "## $TS — 凌晨推送" >> "$PUSH_LOG"
    echo "- **推送URL数**: 10（尝试）" >> "$PUSH_LOG"
    echo "- **API返回**: $BODY" >> "$PUSH_LOG"
    echo "- **状态**: ❌ 配额已满或失败" >> "$PUSH_LOG"
    echo "" >> "$PUSH_LOG"
fi
