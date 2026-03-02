#!/bin/bash
# gen-cover-smart.sh - 智能封面生成（文件夹风格）
# 用法: bash scripts/gen-cover-smart.sh "文章标题" "文章摘要（可选）" 输出文件.png

set -e

# 颜色输出
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 检查参数
if [ $# -lt 2 ]; then
    echo -e "${RED}用法: bash scripts/gen-cover-smart.sh \"文章标题\" 输出文件.png${NC}"
    echo -e "${YELLOW}示例: bash scripts/gen-cover-smart.sh \"普通人也能拥有8个AI助手\" articles/ai-helper-cover.png${NC}"
    exit 1
fi

TITLE="$1"
OUTPUT="$2"

# 提取核心主题（取前8个字左右作为主题）
THEME=$(echo "$TITLE" | sed 's/[：？！，。]/ /g' | awk '{print $1" "$2" "$3}' | sed 's/ *$//')
if [ -z "$THEME" ]; then
    THEME="AI工具"
fi

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}  智能封面生成器 - 文件夹风格${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""
echo -e "${GREEN}📄 文章标题: ${NC}$TITLE"
echo -e "${GREEN}🎯 核心主题: ${NC}$THEME"
echo ""

# 生成文件夹风格提示词
PROMPT="Create a professional 3D folder-style infographic cover for a tech tutorial article about「${TITLE}」.

=== CRITICAL STYLE REQUIREMENTS ===

【OVERALL ART STYLE】
- 3D skeuomorphic stationery style, clean and premium
- A4 clipboard with layered folders and index tabs
- Modern, professional, tech-forward aesthetic
- NOT flat design, NOT generic illustration

【COLOR PALETTE】
- Background: Cream/Beige (#F5F5DC) with subtle texture
- Primary accent: Klein Blue (#002FA7) for main highlights
- Secondary accent: Vibrant Orange (#FF6B35) for emphasis
- Text: Dark charcoal (#2C2C2C)
- Highlights: Soft yellow (#FFD93D) for badges

【COMPOSITION - FOLDER STYLE】
- Main element: A realistic 3D clipboard with metal clip at top
- Layered folders sticking out from clipboard
- Colorful index tabs (Klein Blue, Orange, Green) visible on the right side
- 3D mouse cursor pointing to key content
- Small notification badges with numbers (like "01", "02", "03")
- Paper texture with slight shadow for depth

【TYPOGRAPHY】
- Main title: Large bold sans-serif Chinese characters「${TITLE}」centered on the clipboard
- Subtitle: Smaller English text "AI TOOLS GUIDE" or "COMPLETE TUTORIAL" below
- Section markers: Numbers in colored circles (①, ②, ③)
- All text in CHINESE (primary), English as secondary accent

【DECORATIVE ELEMENTS】
- 3D push pins in Klein Blue and Orange
- Paper clips and binder clips
- Small sticky notes with corner folded
- Checkmark icons (✓) in green circles
- Alert/notification dots
- Subtle grid pattern background

【CONTENT LAYOUT】
- Title prominently displayed on the clipboard paper
- 3-4 key points shown as bullet points with icons
- Visual hierarchy: Title → Subtitle → Key points → Decorative elements
- Leave some breathing room, not overcrowded

【LIGHTING & SHADOW】
- Soft directional lighting from top-left
- Realistic shadows under clipboard and folders
- Subtle gradient on the metal clip
- Depth through layer separation

【AVOID】
- ❌ Flat 2D design
- ❌ Cluttered layout
- ❌ Too many colors (stick to palette)
- ❌ Cartoonish or childish elements
- ❌ Generic stock icons

【ASPECT RATIO】
- 16:9 (landscape, optimized for WeChat article covers)
- High resolution, crisp details

【MOOD】
- Professional yet approachable
- Tech-savvy but not intimidating
- Organized and trustworthy"

echo -e "${YELLOW}🎨 生成的提示词:${NC}"
echo -e "${BLUE}----------------------------------------${NC}"
echo "$PROMPT"
echo -e "${BLUE}----------------------------------------${NC}"
echo ""

# 询问用户是否确认
echo -e "${YELLOW}确认使用此提示词生成封面?${NC}"
echo -e "选项: ${GREEN}[Y]${NC} 确认生成 | ${YELLOW}[E]${NC} 编辑提示词 | ${RED}[N]${NC} 取消"
read -p "你的选择 (Y/E/N): " choice

case "$choice" in
    [Yy]*)
        echo -e "${GREEN}✅ 开始生成封面...${NC}"
        # 调用现有的 gen-image.sh
        bash "$(dirname "$0")/gen-image.sh" "$PROMPT" "$OUTPUT"
        ;;
    [Ee]*)
        echo -e "${YELLOW}📝 请输入修改后的提示词 (输入完成后按 Ctrl+D):${NC}"
        PROMPT=$(cat)
        echo -e "${GREEN}✅ 使用修改后的提示词生成封面...${NC}"
        bash "$(dirname "$0")/gen-image.sh" "$PROMPT" "$OUTPUT"
        ;;
    [Nn]*)
        echo -e "${RED}❌ 已取消生成${NC}"
        exit 0
        ;;
    *)
        echo -e "${RED}❌ 无效选择，已取消${NC}"
        exit 1
        ;;
esac

echo ""
echo -e "${GREEN}✅ 封面生成完成!${NC}"
echo -e "${GREEN}📁 保存位置: ${NC}$OUTPUT"
