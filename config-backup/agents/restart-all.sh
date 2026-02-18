#!/bin/bash
# restart-all.sh - 重启所有AI助手

echo "🔄 重启所有AI助手..."
echo ""

# CEO
echo "📊 重启 CEO..."
bash /root/.openclaw/agents/start-ceo.sh
sleep 3

# 内容部
echo "🎯 重启 内容部..."
bash /root/.openclaw/agents/start-content.sh
sleep 3

# 运营部
echo "📈 重启 运营部..."
bash /root/.openclaw/agents/start-ops.sh
sleep 3

echo ""
echo "✅ 全部重启完成！"
echo ""
echo "查看状态:"
echo "  ps aux | grep openclaw"
echo ""
echo "查看日志:"
echo "  tail -f /var/log/ceo.log"
echo "  tail -f /var/log/content.log"
echo "  tail -f /var/log/ops.log"
