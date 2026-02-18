#!/bin/bash
# start-ops.sh - 启动运营部（持久化后台运行）

cd /root/.openclaw/agents/ops

# 先停止旧进程
pkill -f "openclaw gateway.*port 18792" 2>/dev/null
sleep 2

# 后台启动，输出到日志
nohup openclaw gateway start --port 18792 > /var/log/ops.log 2>&1 &

echo "运营部已启动在端口 18792"
echo "查看日志: tail -f /var/log/ops.log"
