#!/bin/bash
# OpenClaw 版本检查脚本 - 每天自动运行

# 配置
REPO="openclaw/openclaw"
TELEGRAM_CHANNEL="telegram"
TELEGRAM_TO="telegram:-1003863252740"  # 更新主题
CURRENT_VERSION_FILE="/tmp/openclaw_current_version.txt"

# 获取最新版本
LATEST=$(curl -s https://api.github.com/repos/$REPO/releases/latest | grep '"tag_name"' | cut -d'"' -f4)

if [ -z "$LATEST" ]; then
  echo "Failed to fetch latest version"
  exit 1
fi

# 读取当前记录的版本
if [ -f "$CURRENT_VERSION_FILE" ]; then
  CURRENT=$(cat "$CURRENT_VERSION_FILE")
else
  CURRENT=""
fi

# 比较版本
if [ "$LATEST" != "$CURRENT" ]; then
  # 有新版本
  echo "New version found: $LATEST (was: $CURRENT)"
  
  # 获取更新内容
  BODY=$(curl -s https://api.github.com/repos/$REPO/releases/latest | grep '"body"' | cut -d'"' -f4 | head -c 3000)
  
  # 格式化消息
  MSG="🦞 *OpenClaw 新版本发布*
  
📦 *最新版本*: $LATEST

📝 *更新内容*:
$BODY

🔗 查看完整更新: https://github.com/$REPO/releases"
  
  # 发送 Telegram
  message send --channel $TELEGRAM_CHANNEL --to "$TELEGRAM_TO" --message "$MSG"
  
  # 更新版本记录
  echo "$LATEST" > "$CURRENT_VERSION_FILE"
else
  echo "No new version, already at $LATEST"
fi
