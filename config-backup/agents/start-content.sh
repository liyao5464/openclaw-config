#!/bin/bash
# start-content.sh - 启动内容部（持久化后台运行）

cd /root/.openclaw/agents/content

# 先停止旧进程
pkill -f "openclaw gateway.*port 18791" 2>/dev/null
sleep 2

# 后台启动，输出到日志
nohup openclaw gateway start --port 18791 > /var/log/content.log 2>&1 &

echo "内容部已启动在端口 18791"
echo "查看日志: tail -f /var/log/content.log"
