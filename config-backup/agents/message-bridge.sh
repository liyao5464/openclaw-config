#!/bin/bash
# message-bridge.sh - 消息中转脚本
# 每分钟检查一次Telegram消息，调用AI回复

LOG_FILE="/var/log/message-bridge.log"
LAST_UPDATE_ID_FILE="/tmp/last_update_id"

# CEO Bot
CEO_BOT="8502623699:AAHvcI6KzV9aIOrSvRk_jR9mIdw_U9ltbvU"
# 内容部 Bot  
CONTENT_BOT="8410310347:AAGdeSOEmHbxI6Riuk2eVllyYEY7aupYJwM"
# 运营部 Bot
OPS_BOT="7893941242:AAFRzUTiVt9MFBF2vOegR2ZAirXfuai6a94"

CHAT_ID="8404273573"

# 获取上次处理的update_id
get_last_id() {
    if [ -f "$LAST_UPDATE_ID_FILE" ]; then
        cat "$LAST_UPDATE_ID_FILE"
    else
        echo "0"
    fi
}

# 保存update_id
save_last_id() {
    echo "$1" > "$LAST_UPDATE_ID_FILE"
}

# 处理CEO消息
process_ceo() {
    local last_id=$(get_last_id)
    local updates=$(curl -s "https://api.telegram.org/bot${CEO_BOT}/getUpdates?offset=${last_id}&limit=10")
    
    echo "$updates" | grep -o '"update_id":[0-9]*' | grep -o '[0-9]*' | while read id; do
        if [ "$id" -gt "$last_id" ]; then
            local text=$(echo "$updates" | grep -A5 "\"update_id\":$id" | grep '"text":"' | head -1 | sed 's/.*"text":"//;s/".*//')
            if [ -n "$text" ] && [ "$text" != "/start" ]; then
                echo "[$(date)] CEO收到: $text" >> "$LOG_FILE"
                # 这里可以调用AI生成回复
                # 暂时发送固定回复
                curl -s "https://api.telegram.org/bot${CEO_BOT}/sendMessage?chat_id=${CHAT_ID}&text=CEO收到：$text%0A%0A正在处理中..."
                save_last_id "$((id + 1))"
            fi
        fi
    done
}

# 主循环
echo "[$(date)] 消息中转服务启动" >> "$LOG_FILE"

while true; do
    process_ceo
    sleep 60
done
