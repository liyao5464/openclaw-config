#!/bin/bash
# 每晚23:45自动提炼：把当天日志里的重要内容沉淀到知识库
DATE=$(date +%Y-%m-%d)
LOG_FILE="/root/.openclaw/workspace/memory/${DATE}.md"

if [ ! -f "$LOG_FILE" ]; then
  echo "[$DATE] 今天没有日志文件，跳过提炼" >> /root/.openclaw/workspace/memory/reflect.log
  exit 0
fi

echo "[$DATE] 触发每晚提炼，日志文件: $LOG_FILE" >> /root/.openclaw/workspace/memory/reflect.log
