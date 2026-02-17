#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AI Video Scriptor - Generate video scripts and prompts
Usage: python scriptor.py "your idea" --platform seedance2
"""

import sys
import json
import argparse

# Platform-specific prompt templates
PLATFORM_TEMPLATES = {
    "seedance2": {
        "name": "Seedance 2.0",
        "strengths": ["音视频同步", "多镜头叙事", "自然表演"],
        "prompt_template": "{scene}。{camera}。{lighting}。{style}。",
        "tips": "强调嘴型同步、微表情、镜头连贯性"
    },
    "kling3": {
        "name": "可灵 3.0",
        "strengths": ["15秒生成", "智能分镜", "音画同步"],
        "prompt_template": "{scene}，{camera}，{lighting}，{style}",
        "tips": "适合长镜头和复杂场景切换"
    },
    "dreamina": {
        "name": "即梦/Dreamina",
        "strengths": ["通用性强", "速度快", "质量稳定"],
        "prompt_template": "{scene}。{camera}。{style}",
        "tips": "平衡质量与速度，适合日常创作"
    }
}

def generate_storyboard(idea, platform="seedance2"):
    """Generate storyboard based on idea and platform"""
    
    platform_info = PLATFORM_TEMPLATES.get(platform, PLATFORM_TEMPLATES["seedance2"])
    
    # Simple keyword extraction and scene generation
    # In real implementation, this would use LLM
    
    scenes = []
    
    # Default 3-5 shot structure
    default_structure = [
        {"type": "开场", "duration": 5, "camera": "镜头从远景缓缓推进"},
        {"type": "发展", "duration": 5, "camera": "中景拍摄"},
        {"type": "高潮", "duration": 5, "camera": "特写镜头"},
        {"type": "结尾", "duration": 5, "camera": "全景或拉远"}
    ]
    
    for i, struct in enumerate(default_structure, 1):
        scene = {
            "shot": i,
            "type": struct["type"],
            "duration": struct["duration"],
            "description": f"基于'{idea}'的{struct['type']}画面",
            "camera": struct["camera"],
            "prompt": generate_prompt(idea, struct, platform)
        }
        scenes.append(scene)
    
    return {
        "title": idea,
        "platform": platform_info["name"],
        "total_duration": sum(s["duration"] for s in scenes),
        "scenes": scenes,
        "tips": platform_info["tips"]
    }

def generate_prompt(idea, struct, platform):
    """Generate platform-specific prompt"""
    
    platform_info = PLATFORM_TEMPLATES.get(platform, PLATFORM_TEMPLATES["seedance2"])
    template = platform_info["prompt_template"]
    
    # Fill template
    prompt = template.format(
        scene=f"{idea}的{struct['type']}场景",
        camera=struct["camera"],
        lighting="柔和的自然光" if platform == "seedance2" else "电影级灯光",
        style="电影纪录片风格，4K画质，专业调色"
    )
    
    return prompt

def generate_image_prompts(storyboard):
    """Generate reference image prompts for each shot"""
    
    image_prompts = []
    for scene in storyboard["scenes"]:
        prompt = f"{scene['description']}的参考图，{scene['camera']}视角，高细节，专业摄影风格"
        image_prompts.append({
            "shot": scene["shot"],
            "prompt": prompt
        })
    
    return image_prompts

def format_output(storyboard, image_prompts=None):
    """Format output for display"""
    
    output = []
    output.append(f"📽️ 视频脚本：{storyboard['title']}")
    output.append(f"🎬 平台：{storyboard['platform']}")
    output.append(f"⏱️ 总时长：{storyboard['total_duration']}秒")
    output.append("")
    output.append("━━━━━━━━━━━━━━━━━━━━━")
    output.append("")
    
    for scene in storyboard["scenes"]:
        output.append(f"镜头 {scene['shot']} [{scene['type']}]")
        output.append(f"时长：{scene['duration']}秒")
        output.append(f"画面：{scene['description']}")
        output.append(f"运镜：{scene['camera']}")
        output.append(f"Prompt：{scene['prompt']}")
        output.append("")
    
    if image_prompts:
        output.append("📋 图片参考提示词")
        output.append("━━━━━━━━━━━━━━━━━━━━━")
        for img in image_prompts:
            output.append(f"镜头{img['shot']}：{img['prompt']}")
        output.append("")
    
    output.append(f"💡 提示：{storyboard['tips']}")
    
    return "\n".join(output)

def main():
    parser = argparse.ArgumentParser(description="AI Video Scriptor")
    parser.add_argument("idea", help="Your video idea/concept")
    parser.add_argument("--platform", "-p", default="seedance2", 
                       choices=["seedance2", "kling3", "dreamina"],
                       help="Target platform")
    parser.add_argument("--images", "-i", action="store_true",
                       help="Also generate image prompts")
    
    args = parser.parse_args()
    
    print(f"🎬 正在生成脚本...")
    print(f"主题：{args.idea}")
    print(f"平台：{PLATFORM_TEMPLATES[args.platform]['name']}")
    print()
    
    # Generate storyboard
    storyboard = generate_storyboard(args.idea, args.platform)
    
    # Generate image prompts if requested
    image_prompts = None
    if args.images:
        image_prompts = generate_image_prompts(storyboard)
    
    # Output
    print(format_output(storyboard, image_prompts))
    
    # Save to file
    filename = f"script_{args.idea[:20]}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(format_output(storyboard, image_prompts))
    print(f"\n💾 已保存到：{filename}")

if __name__ == "__main__":
    main()
