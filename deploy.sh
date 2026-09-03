#!/bin/bash
# subaotw.cn 手动部署脚本（GitHub Actions 之外的备用通道）
#
# 用法:
#   bash deploy.sh
#
# 优先使用 GitHub Actions 自动部署（push main 触发 .github/workflows/deploy.yml）。
# 本脚本用于 Actions 未配置 secrets、或需要紧急手动发布时使用。
#
# 依赖：OPENSSH 私钥。可用环境变量 SSH_KEY 覆盖；
#       未指定时按候选列表自动探测第一个能免密登录的密钥。
#       （历史默认 ../../videotv-correct-ssh-key.txt 已不存在，故改为自动探测）

set -e

# 站点根目录 = 本脚本所在目录
LOCAL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SERVER="ubuntu@175.178.184.141"
SITE_DIR="/var/www/subaotw-cn"

# 1. 解析 SSH 密钥：环境变量优先，否则自动探测
CANDIDATES=(
  "$HOME/.ssh/videotv_github_actions"
  "$HOME/.ssh/videotv_deploy"
  "$HOME/.ssh/videotvai_deploy"
  "$LOCAL_DIR/../../videotv-correct-ssh-key.txt"
)
if [ -z "$SSH_KEY" ]; then
  for k in "${CANDIDATES[@]}"; do
    [ -f "$k" ] || continue
    if ssh -i "$k" -o StrictHostKeyChecking=no -o BatchMode=yes \
           -o ConnectTimeout=6 "$SERVER" "echo ok" >/dev/null 2>&1; then
      SSH_KEY="$k"
      break
    fi
  done
fi
SSH_KEY="${SSH_KEY:-${CANDIDATES[0]}}"

if [ ! -f "$SSH_KEY" ]; then
  echo "❌ 找不到 SSH 密钥: $SSH_KEY"
  echo "   可用环境变量指定: SSH_KEY=/path/to/key bash deploy.sh"
  exit 1
fi
echo "🔑 使用密钥: $SSH_KEY"

# 2. JS 语法校验（脚本存在才校验，不存在则跳过）
if [ -f "$LOCAL_DIR/scripts/validate-js.py" ]; then
  echo "🔍 部署前验证 JS 语法..."
  python3 "$LOCAL_DIR/scripts/validate-js.py" --quick || {
    echo ""
    echo "❌ JS 语法检查未通过，取消部署！"
    exit 1
  }
  echo "✅ JS 语法检查通过"
else
  echo "ℹ️  未找到 scripts/validate-js.py，跳过 JS 语法检查"
fi

echo ""
echo "🚀 部署 subaotw.cn → $SITE_DIR"

# 3. 确保服务器目录存在
ssh -i "$SSH_KEY" -o StrictHostKeyChecking=no "$SERVER" \
  "sudo mkdir -p $SITE_DIR && sudo chown ubuntu:ubuntu $SITE_DIR"

# 4. 打包
#    COPYFILE_DISABLE=1 + --exclude='._*' 双保险：阻止 macOS AppleDouble (._xxx)
#    文件被打进包里。这些文件会被 nginx 以 Content-Type: text/html 返回 200，
#    在抓取预算紧张的站点上纯属浪费（2026-08-31 曾清理 715 个此类垃圾文件）。
export COPYFILE_DISABLE=1
cd "$LOCAL_DIR"
tar -czf /tmp/subaotw-cn.tar.gz \
  --exclude='./.git' --exclude='./.github' --exclude='./.workbuddy' \
  --exclude='*.md' --exclude='__pycache__' --exclude='*.pyc' \
  --exclude='._*' --exclude='.DS_Store' --exclude='__MACOSX' \
  .
echo "📦 打包完成: $(du -h /tmp/subaotw-cn.tar.gz | cut -f1)"

# 5. 上传并解压
scp -i "$SSH_KEY" -o StrictHostKeyChecking=no /tmp/subaotw-cn.tar.gz "$SERVER:/tmp/"
rm -f /tmp/subaotw-cn.tar.gz

ssh -i "$SSH_KEY" -o StrictHostKeyChecking=no "$SERVER" \
  "cd $SITE_DIR && (tar -xzf /tmp/subaotw-cn.tar.gz 2>/dev/null || sudo tar -xzf /tmp/subaotw-cn.tar.gz) \
   && sudo rm -f /tmp/subaotw-cn.tar.gz \
   && find $SITE_DIR -name '._*' -type f -delete 2>/dev/null || true \
   && (nginx -t 2>/dev/null && sudo systemctl reload nginx 2>/dev/null || sudo nginx -t && sudo systemctl reload nginx) \
   && echo '✅ 部署完成' \
   && echo \"index.html: \$(wc -l < $SITE_DIR/index.html) lines\""
