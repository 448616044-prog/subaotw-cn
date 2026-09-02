#!/bin/bash
# subaotw.cn Baidu 主动推送 (每日10条，轮换)
URLS='https://www.subaotw.cn/blog/cn-to-tw-large-items-shipping
https://www.subaotw.cn/blog/cn-to-tw-moving-guide
https://www.subaotw.cn/blog/cn-to-tw-shipping-guide
https://www.subaotw.cn/blog/cn-to-tw-special-large-items
https://www.subaotw.cn/blog/cosmetics-shipping
https://www.subaotw.cn/blog/daily-items-to-taiwan
https://www.subaotw.cn/blog/electronics-shipping
https://www.subaotw.cn/blog/express-compare-guide
https://www.subaotw.cn/blog/food-shipping-guide
https://www.subaotw.cn/blog/food-to-taiwan'
curl -s -H 'Content-Type:text/plain' --data-binary "$URLS" "http://data.zz.baidu.com/urls?site=https://www.subaotw.cn&token=UAVg0xt7rxpTjzaL"
echo ""
