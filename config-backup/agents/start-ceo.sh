#!/bin/bash
# start-ceo.sh - 启动CEO（持久化后台运行）

cd /root/.openclaw/agents/ceo

# 先停止旧进程
pkill -f "openclaw gateway.*port 18790" 2>/dev/null
sleep 2

# 后台启动，输出到日志
nohup openclaw gateway start --port 18790 > /var/log/ceo.log 2>&1 &

echo "CEO已启动在端口 18790"
echo "查看日志: tail -f /var/log/ceo.log"
