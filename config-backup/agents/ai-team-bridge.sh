#!/bin/bash
# ai-team-bridge.sh - AI助手团队消息中转
# 由小知了（秘书）统一管理

LOG_FILE="/var/log/ai-team-bridge.log"
mkdir -p /var/log 2>/dev/null || mkdir -p ~/logs

# Bot Tokens
CEO_BOT="8502623699:AAHvcI6KzV9aIOrSvRk_jR9mIdw_U9ltbvU"
CONTENT_BOT="8410310347:AAGdeSOEmHbxI6Riuk2eVllyYEY7aupYJwM"
OPS_BOT="7893941242:AAFRzUTiVt9MFBF2vOegR2ZAirXfuai6a94"

CHAT_ID="8404273573"

# 存储每个Bot的最后update_id
declare -A LAST_IDS
LAST_IDS[ceo]=0
LAST_IDS[content]=0
LAST_IDS[ops]=0

# 读取上次的ID
read_last_ids() {
    for role in ceo content ops; do
        if [ -f "/tmp/last_id_${role}" ]; then
            LAST_IDS[$role]=$(cat "/tmp/last_id_${role}")
        fi
    done
}

# 保存ID
save_last_id() {
    local role=$1
    local id=$2
    echo "$id" > "/tmp/last_id_${role}"
    LAST_IDS[$role]=$id
}

# 获取并处理消息
process_bot() {
    local role=$1
    local bot_token=$2
    local last_id=${LAST_IDS[$role]}
    
    local updates=$(curl -s "https://api.telegram.org/bot${bot_token}/getUpdates?offset=${last_id}&limit=10" 2>/dev/null)
    
    # 检查是否有新消息
    if echo "$updates" | grep -q '"ok":true'; then
        # 提取所有update_id
        local ids=$(echo "$updates" | grep -o '"update_id":[0-9]*' | grep -o '[0-9]*' | sort -n)
        
        for id in $ids; do
            if [ "$id" -ge "$last_id" ]; then
                # 提取消息内容
                local text=$(echo "$updates" | grep -A10 "\"update_id\":$id" | grep '"text":"' | head -1 | sed 's/.*"text":"//;s/",.*//;s/"$//')
                
                if [ -n "$text" ] && [ "$text" != "/start" ]; then
                    echo "[$(date '+%Y-%m-%d %H:%M:%S')] [$role] 收到: $text" >> "$LOG_FILE"
                    
                    # 根据角色生成回复
                    local response=$(generate_response "$role" "$text")
                    
                    # 发送回复
                    curl -s "https://api.telegram.org/bot${bot_token}/sendMessage?chat_id=${CHAT_ID}&text=${response}&parse_mode=HTML" > /dev/null 2>&1
                    
                    save_last_id "$role" $((id + 1))
                fi
            fi
        done
    fi
}

# 根据角色生成回复
generate_response() {
    local role=$1
    local user_msg=$2
    
    case "$role" in
        ceo)
            echo "老板好！📊<br><br>收到您的指示：<b>$user_msg</b><br><br>作为CEO，我建议：<br>• 立即安排相关部门执行<br>• 今日内给您进度汇报<br>• 如有需要协调的，我来统筹<br><br>请确认是否按此执行？"
            ;;
        content)
            echo "老板好！🎯<br><br>关于<b>$user_msg</b>：<br><br>【内容部建议】<br>• 本周可安排2-3个相关选题<br>• 预计产出1篇深度文章+2条短视频<br>• 需要老板确认具体内容方向<br><br>请指示优先级别？"
            ;;
        ops)
            echo "老板好！📈<br><br>收到数据需求：<b>$user_msg</b><br><br>【运营部数据】<br>• 今日新增粉丝：___<br>• 昨日阅读量：___<br>• 本周累计：___<br><br>详细报表正在整理，10分钟后发给您！"
            ;;
        *)
            echo "收到：$user_msg"
            ;;
    esac
}

# 主循环
main() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] AI助手团队中转服务启动" >> "$LOG_FILE"
    read_last_ids
    
    while true; do
        process_bot "ceo" "$CEO_BOT"
        process_bot "content" "$CONTENT_BOT"
        process_bot "ops" "$OPS_BOT"
        
        sleep 30  # 每30秒检查一次
    done
}

# 启动
main
