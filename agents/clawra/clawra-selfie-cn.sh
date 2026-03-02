#!/bin/bash
# clawra-selfie-cn.sh - 国内版 Clawra 自拍脚本
# 使用阿里云 DashScope / 通义万相 替代 fal.ai

# ========== 配置区域 ==========
# 选择使用的API：
# API_PROVIDER="dashscope"    # 阿里云 DashScope (推荐)
# API_PROVIDER="baidu"        # 百度文心
API_PROVIDER="${API_PROVIDER:-dashscope}"

# API Key (从环境变量读取)
DASHSCOPE_API_KEY="${DASHSCOPE_API_KEY:-}"
BAIDU_API_KEY="${BAIDU_API_KEY:-}"
BAIDU_SECRET_KEY="${BAIDU_SECRET_KEY:-}"

# 固定参考图片 (Clawra形象)
REFERENCE_IMAGE="https://cdn.jsdelivr.net/gh/SumeLabs/clawra@main/assets/clawra.png"

# OpenClaw Gateway Token
OPENCLAW_GATEWAY_TOKEN="${OPENCLAW_GATEWAY_TOKEN:-}"

# ========== 函数定义 ==========

# 显示帮助
show_help() {
    echo "使用方法: $0 <场景描述> [模式] [标题]"
    echo ""
    echo "参数:"
    echo "  场景描述  - 例如: '在咖啡馆' '穿红色连衣裙'"
    echo "  模式      - mirror(全身/镜子自拍) 或 direct(近景/环境自拍), 默认 auto"
    echo "  标题      - 发送时的文字说明"
    echo ""
    echo "示例:"
    echo "  $0 '在海边看日落' direct '今天的海风好舒服~'"
    echo "  $0 '穿着卫衣' mirror '宅家日常'"
    echo ""
    echo "环境变量:"
    echo "  DASHSCOPE_API_KEY - 阿里云 DashScope API Key"
    echo "  OPENCLAW_GATEWAY_TOKEN - OpenClaw Gateway Token"
}

# 检查依赖
check_deps() {
    if ! command -v jq &> /dev/null; then
        echo "错误: 需要安装 jq (JSON处理工具)"
        echo "Ubuntu/Debian: sudo apt install jq"
        echo "CentOS/RHEL: sudo yum install jq"
        echo "macOS: brew install jq"
        exit 1
    fi
    
    if ! command -v curl &> /dev/null; then
        echo "错误: 需要安装 curl"
        exit 1
    fi
}

# 下载参考图片到本地
download_reference() {
    local temp_dir="/tmp/clawra"
    mkdir -p "$temp_dir"
    local local_path="$temp_dir/reference.png"
    
    if [ ! -f "$local_path" ]; then
        echo "下载参考图片..."
        curl -sL "$REFERENCE_IMAGE" -o "$local_path"
        if [ ! -f "$local_path" ]; then
            echo "错误: 无法下载参考图片"
            exit 1
        fi
    fi
    
    echo "$local_path"
}

# 自动检测模式
detect_mode() {
    local context="$1"
    
    # 近景关键词
    if echo "$context" | grep -qiE "咖啡馆|海边|公园|街道|特写|近景|脸部|表情|风景|背景"; then
        echo "direct"
    # 全身/穿搭关键词
    elif echo "$context" | grep -qiE "穿着|穿搭|衣服|裙子|镜子|全身| outfit|fashion"; then
        echo "mirror"
    else
        echo "direct"  # 默认近景
    fi
}

# 构建提示词
build_prompt() {
    local context="$1"
    local mode="$2"
    
    if [ "$mode" == "mirror" ]; then
        echo "一位年轻女性正在镜子前自拍，${context}，手机拿着自拍，镜子反射，全身照，自然光线，高清照片，真实感"
    else
        echo "一位年轻女性在${context}自拍，手机拿着自拍，近景特写，自然微笑，看向镜头，自然光线，高清照片，真实感"
    fi
}

# 使用 DashScope (阿里云) 生成图片
generate_dashscope() {
    local prompt="$1"
    local output_file="$2"
    
    if [ -z "$DASHSCOPE_API_KEY" ]; then
        echo "错误: 未设置 DASHSCOPE_API_KEY 环境变量"
        exit 1
    fi
    
    echo "使用 DashScope 生成图片..."
    echo "提示词: $prompt"
    
    # 调用 DashScope API (通义万相)
    local response=$(curl -s -X POST "https://dashscope.aliyuncs.com/api/v1/services/aigc/text2image/image-synthesis" \
        -H "Authorization: Bearer $DASHSCOPE_API_KEY" \
        -H "Content-Type: application/json" \
        -d "{
            \"model\": \"wanx-v1\",
            \"input\": {
                \"prompt\": \"$prompt\",
                \"negative_prompt\": \"丑陋、变形、多余的手指、模糊、低质量、卡通、动漫\"
            },
            \"parameters\": {
                \"size\": \"1024*1024\",
                \"n\": 1,
                \"style\": \"摄影\"
            }
        }")
    
    # 解析结果
    local task_id=$(echo "$response" | jq -r '.output.task_id // empty')
    
    if [ -z "$task_id" ] || [ "$task_id" == "null" ]; then
        echo "错误: 创建任务失败"
        echo "响应: $response"
        exit 1
    fi
    
    echo "任务创建成功，ID: $task_id"
    echo "等待生成完成..."
    
    # 轮询等待结果
    local max_attempts=30
    local attempt=0
    local image_url=""
    
    while [ $attempt -lt $max_attempts ]; do
        sleep 2
        attempt=$((attempt + 1))
        
        local status_response=$(curl -s -X GET "https://dashscope.aliyuncs.com/api/v1/tasks/${task_id}" \
            -H "Authorization: Bearer $DASHSCOPE_API_KEY")
        
        local status=$(echo "$status_response" | jq -r '.output.task_status // empty')
        
        if [ "$status" == "SUCCEEDED" ]; then
            image_url=$(echo "$status_response" | jq -r '.output.results[0].url // empty')
            break
        elif [ "$status" == "FAILED" ]; then
            echo "错误: 图片生成失败"
            echo "响应: $status_response"
            exit 1
        fi
        
        echo -n "."
    done
    
    if [ -z "$image_url" ]; then
        echo "错误: 等待超时"
        exit 1
    fi
    
    echo ""
    echo "图片生成成功!"
    
    # 下载图片
    curl -sL "$image_url" -o "$output_file"
    echo "$output_file"
}

# 使用图片URL生成 (图生图) - 需要支持图生图的服务
generate_with_reference() {
    local context="$1"
    local mode="$2"
    local output_file="/tmp/clawra/output.jpg"
    
    mkdir -p "$(dirname "$output_file")"
    
    local prompt=$(build_prompt "$context" "$mode")
    
    case "$API_PROVIDER" in
        dashscope)
            generate_dashscope "$prompt" "$output_file"
            ;;
        *)
            echo "错误: 不支持的 API 提供商: $API_PROVIDER"
            exit 1
            ;;
    esac
}

# 发送图片到飞书
send_to_feishu() {
    local image_file="$1"
    local caption="$2"
    
    # 检查 openclaw 命令
    if command -v openclaw &> /dev/null; then
        echo "通过 OpenClaw 发送..."
        # 这里需要根据实际情况调整发送命令
        # openclaw message send ...
        echo "图片已保存: $image_file"
        echo "请手动发送或使用 OpenClaw 发送"
    else
        echo "图片已保存到: $image_file"
        echo "提示: $caption"
    fi
}

# ========== 主程序 ==========

main() {
    # 检查参数
    if [ $# -lt 1 ]; then
        show_help
        exit 1
    fi
    
    local context="$1"
    local mode="${2:-auto}"
    local caption="${3:-Clawra的自拍~ 💕}"
    
    # 检查依赖
    check_deps
    
    # 自动检测模式
    if [ "$mode" == "auto" ]; then
        mode=$(detect_mode "$context")
        echo "自动检测模式: $mode"
    fi
    
    # 下载参考图片
    local ref_path=$(download_reference)
    echo "参考图片: $ref_path"
    
    # 生成图片
    local output_file="/tmp/clawra/selfie_$(date +%s).jpg"
    generate_with_reference "$context" "$mode" "$output_file"
    
    # 发送
    send_to_feishu "$output_file" "$caption"
    
    echo ""
    echo "✅ 完成! 图片保存在: $output_file"
}

# 运行主程序
main "$@"
