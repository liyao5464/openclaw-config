---
name: ai-video-scriptor
description: Generate AI video scripts and prompts for Seedance, 可灵, 即梦等平台. Input your idea, get complete storyboard + video prompts + image prompts.
---

# AI Video Scriptor

Generate professional video scripts and AI prompts for various video generation platforms.

## Supported Platforms

- **Seedance 2.0** (ByteDance) - Audio-visual sync, multi-shot narrative
- **可灵 3.0** (Kuaishou) - 15s video, smart storyboarding
- **即梦/Dreamina** (ByteDance) - General purpose video generation
- **Pika** - Cinematic motion
- **Runway Gen-3** - Professional filmmaking

## Workflow

1. **User Input**: Describe your video idea/concept
2. **Platform Selection**: Choose target platform (or auto-recommend)
3. **Script Generation**: Create storyboard with shots
4. **Prompt Generation**: Generate optimized prompts for each shot
5. **Image Prompts** (Optional): Generate reference image prompts

## Usage

### Basic Usage

User: "帮我写一个科比和保罗湖人夺冠的纪录片脚本"

→ Output:
- Storyboard (3-5 shots)
- Video prompts for chosen platform
- Duration for each shot

### Advanced Usage

User: "写一个赛博朋克风格的咖啡广告，用Seedance 2.0"

→ Output:
- Detailed storyboard
- Seedance 2.0 optimized prompts
- Image reference prompts
- Camera movement suggestions

## Output Format

```
📽️ 视频脚本：[标题]

🎬 分镜表
━━━━━━━━━━━━━━━━━━━━━

镜头 1
时长：5秒
画面：[描述]
Prompt：[AI视频提示词]

镜头 2
时长：5秒
画面：[描述]
Prompt：[AI视频提示词]

...

📋 图片参考提示词（可选）
- 镜头1参考图：[提示词]
- 镜头2参考图：[提示词]

🎵 建议音乐/音效：[风格]
```

## Platform-Specific Tips

### Seedance 2.0
- Emphasize: audio-visual sync, lip sync, natural performance
- Use: close-ups for dialogue, multi-shot for narrative
- Avoid: complex hand movements

### 可灵 3.0
- Emphasize: 15s duration, smart storyboarding
- Use: camera movements, scene transitions
- Good for: long-form content

### 即梦/Dreamina
- General purpose
- Good balance of quality and speed

## Examples

See `examples/` folder for sample outputs.

## Author

Created for AI video creators.
