#!/bin/bash
# Baidu daily URL push — cron: 0 8 * * * cd /var/www/subaotw-cn && bash baidu-daily-push.sh
# Quota: ~10 URLs/day → pushes next unpushed batch from baidu-push-urls.txt

cd "$(dirname "$0")"

API="http://data.zz.baidu.com/urls?site=https://www.subaotw.cn&token=UAVg0xt7rxpTjzaL"
TODAY=$(date +%Y-%m-%d)
LOG="/tmp/baidu-push-subaotw.log"
URL_FILE="baidu-push-urls.txt"
PUSHED_FILE="baidu-pushed.txt"

# Read all URLs
mapfile -t ALL_URLS < "$URL_FILE"

# Read already pushed URLs
declare -A PUSHED
if [ -f "$PUSHED_FILE" ]; then
  while IFS= read -r line; do
    [[ "$line" =~ ^# ]] && continue
    [[ -z "$line" ]] && continue
    PUSHED["$line"]=1
  done < "$PUSHED_FILE"
fi

# Find first 10 unpushed URLs
BATCH=()
for url in "${ALL_URLS[@]}"; do
  [[ -z "$url" ]] && continue
  [[ -n "${PUSHED[$url]}" ]] && continue
  BATCH+=("$url")
  [[ ${#BATCH[@]} -ge 10 ]] && break
done

if [ ${#BATCH[@]} -eq 0 ]; then
  echo "[$TODAY] All URLs pushed! (${#ALL_URLS[@]} total)" >> "$LOG"
  exit 0
fi

# Push batch
count=0
for url in "${BATCH[@]}"; do
  result=$(curl -s -X POST "$API" -H "Content-Type: text/plain" -d "$url" 2>&1)
  echo "[$TODAY] $url → $result" >> "$LOG"
  if echo "$result" | grep -q '"success"'; then
    ((count++))
    echo "$url" >> "$PUSHED_FILE"
  elif echo "$result" | grep -q 'over quota'; then
    echo "[$TODAY] Quota exceeded after $count" >> "$LOG"
    break
  fi
  sleep 1
done

echo "[$TODAY] Done: $count pushed, $((${#ALL_URLS[@]} - $(wc -l < "$PUSHED_FILE" | tr -d ' '))) remaining" >> "$LOG"
