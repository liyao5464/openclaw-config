#!/bin/bash
# start-all-agents.sh - 启动所有AI助手

echo "🚀 启动老里AI助手团队..."
echo ""

# 启动CEO
echo "📊 启动 CEO..."
cd /root/.openclaw/agents/ceo
nohup openclaw gateway start --port 18790 > /var/log/ceo.log 2>&1 &
echo "CEO 启动在端口 18790"

# 启动内容部
echo "🎯 启动 内容部..."
cd /root/.openclaw/agents/content
nohup openclaw gateway start --port 18791 > /var/log/content.log 2>&1 &
echo "内容部 启动在端口 18791"

# 启动运营部
echo "📈 启动 运营部..."
cd /root/.openclaw/agents/ops
nohup openclaw gateway start --port 18792 > /var/log/ops.log 2>&1 &
echo "运营部 启动在端口 18792"

# 启动商务部
echo "💰 启动 商务部..."
cd /root/.openclaw/agents/biz
nohup openclaw gateway start --port 18793 > /var/log/biz.log 2>&1 &
echo "商务部 启动在端口 18793"

echo ""
echo "✅ 所有助手已启动！"
echo ""
echo "查看日志:"
echo "  tail -f /var/log/ceo.log"
echo "  tail -f /var/log/content.log"
echo "  tail -f /var/log/ops.log"
echo "  tail -f /var/log/biz.log"
