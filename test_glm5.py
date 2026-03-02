#!/usr/bin/env python3
"""
GLM-5 快速测试脚本
使用方法：
1. 安装依赖: pip install requests
2. 设置API Key: export GLM5_API_KEY="your_key_here"
3. 运行: python test_glm5.py
"""

import requests
import os
import json

# API配置
API_URL = "https://api.z.ai/v1/chat/completions"
API_KEY = os.getenv("GLM5_API_KEY", "your_api_key_here")

# 测试用例
TEST_CASES = [
    {
        "name": "代码生成测试",
        "prompt": "用Python写一个快速排序算法，要求带注释和测试用例"
    },
    {
        "name": "数学推理测试", 
        "prompt": "一个水池有两个进水管，A管单独注满需要3小时，B管单独注满需要5小时。如果两个管子同时打开，注满水池需要多久？"
    },
    {
        "name": "长文本测试",
        "prompt": "请总结以下这段关于AI发展的观点，用3句话概括核心思想：" +
                  "人工智能的发展经历了几个阶段。早期是基于规则的系统，依赖专家手工编写规则。" +
                  "后来是机器学习时代，通过数据训练模型。现在是深度学习和大模型时代，" +
                  "模型参数规模爆炸式增长，涌现出强大的推理和生成能力。" +
                  "未来可能会向着Agentic AI发展，AI不仅能生成内容，还能自主规划、使用工具、完成复杂任务。"
    },
    {
        "name": "创意写作测试",
        "prompt": "写一段关于'AI助手陪伴人类'的短故事，200字左右，要有情感共鸣"
    },
    {
        "name": "Agent能力测试",
        "prompt": "请帮我规划一个周末的AI学习路径，包括：1) 学习资源推荐 2) 实践项目建议 3) 时间安排"
    }
]

def test_glm5(prompt, model="glm-5"):
    """调用GLM-5 API"""
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": model,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 2000
    }
    
    try:
        response = requests.post(API_URL, headers=headers, json=data, timeout=60)
        response.raise_for_status()
        result = response.json()
        return result['choices'][0]['message']['content']
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    print("🚀 GLM-5 能力测试\n")
    print("=" * 60)
    
    if API_KEY == "your_api_key_here":
        print("⚠️ 警告: 请先设置 GLM5_API_KEY 环境变量")
        print("export GLM5_API_KEY=\"your_actual_api_key\"\n")
        return
    
    for i, test in enumerate(TEST_CASES, 1):
        print(f"\n📌 测试 {i}: {test['name']}")
        print("-" * 60)
        print(f"💬 Prompt: {test['prompt'][:80]}...")
        print("\n🤖 GLM-5 回答:")
        print("-" * 60)
        
        response = test_glm5(test['prompt'])
        print(response[:500] + "..." if len(response) > 500 else response)
        print("=" * 60)
    
    print("\n✅ 测试完成！")

if __name__ == "__main__":
    main()
