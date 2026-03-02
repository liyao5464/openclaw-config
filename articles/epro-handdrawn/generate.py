from PIL import Image, ImageDraw, ImageFont
import random
import math

# 手绘风格的辅助函数
def sketch_line(draw, x1, y1, x2, y2, fill='#444', width=2, wobble=2):
    """画一条手绘风格的线条，带一点抖动"""
    steps = max(abs(x2-x1), abs(y2-y1)) // 3
    if steps < 5:
        steps = 5
    points = []
    for i in range(steps + 1):
        t = i / steps
        x = x1 + (x2 - x1) * t + random.uniform(-wobble, wobble)
        y = y1 + (y2 - y1) * t + random.uniform(-wobble, wobble)
        points.append((x, y))
    for i in range(len(points) - 1):
        draw.line([points[i], points[i+1]], fill=fill, width=width)

def sketch_ellipse(draw, cx, cy, rx, ry, fill=None, outline='#444', width=2):
    """画手绘风格的椭圆"""
    points = []
    steps = 60
    for i in range(steps + 1):
        angle = (i / steps) * 2 * math.pi
        x = cx + math.cos(angle) * (rx + random.uniform(-2, 2))
        y = cy + math.sin(angle) * (ry + random.uniform(-2, 2))
        points.append((x, y))
    if fill:
        draw.polygon(points, fill=fill)
    for i in range(len(points) - 1):
        draw.line([points[i], points[i+1]], fill=outline, width=width)

def sketch_rect(draw, x1, y1, x2, y2, fill=None, outline='#444', width=2):
    """画手绘风格的矩形"""
    points = [(x1, y1), (x2, y1), (x2, y2), (x1, y2), (x1, y1)]
    wobble_points = []
    for p in points:
        wobble_points.append((p[0] + random.uniform(-1.5, 1.5), p[1] + random.uniform(-1.5, 1.5)))
    if fill:
        draw.polygon(wobble_points[:-1], fill=fill)
    for i in range(len(wobble_points) - 1):
        draw.line([wobble_points[i], wobble_points[i+1]], fill=outline, width=width)

# 柔和配色方案
colors = {
    'bg': '#FAFAF8',
    'text': '#444444',
    'text_light': '#777777',
    'accent1': '#C8D9F0',  # 淡蓝
    'accent2': '#F5D9C8',  # 暖橙
    'accent3': '#D0E8D2',  # 淡绿
    'accent4': '#F0D5D5',  # 淡粉
    'accent5': '#E5D8F0',  # 淡紫
    'accent6': '#F5EED8',  # 米黄
    'line': '#555555',
    'light_line': '#AAAAAA'
}

# ==================== 图1: AI金鱼失忆 ====================
img1 = Image.new('RGB', (800, 600), colors['bg'])
draw1 = ImageDraw.Draw(img1)

# 尝试加载字体，失败就用默认
try:
    font_title = ImageFont.truetype("/usr/share/fonts/google-noto-cjk/NotoSansCJK-DemiLight.ttc", 28)
    font_text = ImageFont.truetype("/usr/share/fonts/google-noto-cjk/NotoSansCJK-Light.ttc", 18)
    font_small = ImageFont.truetype("/usr/share/fonts/google-noto-cjk/NotoSansCJK-Light.ttc", 14)
except:
    font_title = ImageFont.load_default()
    font_text = ImageFont.load_default()
    font_small = ImageFont.load_default()

# 标题
draw1.text((400, 60), "AI like a goldfish...", fill=colors['text'], anchor='mm', font=font_title)
draw1.text((400, 95), "7 seconds memory", fill=colors['text'], anchor='mm', font=font_text)

# 鱼缸（手绘椭圆）
sketch_ellipse(draw1, 400, 360, 130, 130, fill='#E8F0F8', outline='#6A8AAA', width=2)
sketch_ellipse(draw1, 400, 360, 125, 125, fill='#F5F9FC', outline='#6A8AAA', width=2)

# 金鱼身体（手绘椭圆）
sketch_ellipse(draw1, 400, 350, 50, 35, fill='#F5DCC8', outline='#C4956A', width=2)

# 鱼尾
tail_points = [(450, 350), (500, 320), (490, 350), (500, 380)]
tail_wobble = [(p[0] + random.uniform(-2, 2), p[1] + random.uniform(-2, 2)) for p in tail_points]
for i in range(len(tail_wobble) - 1):
    draw1.line([tail_wobble[i], tail_wobble[i+1]], fill='#D4875C', width=2)

# 鱼鳍
fin_points = [(380, 320), (370, 300), (390, 315)]
fin_wobble = [(p[0] + random.uniform(-1, 1), p[1] + random.uniform(-1, 1)) for p in fin_points]
for i in range(len(fin_wobble) - 1):
    draw1.line([fin_wobble[i], fin_wobble[i+1]], fill='#D4875C', width=2)

# 鱼眼
draw1.ellipse((365, 340, 375, 350), fill='#333333')
draw1.ellipse((367, 342, 371, 346), fill='white')

# 问号气泡
bubble_centers = [(400, 180), (460, 150), (340, 160)]
bubble_texts = ['?', '?', '...']
for (bx, by), bt in zip(bubble_centers, bubble_texts):
    sketch_ellipse(draw1, bx, by, 28, 25, fill='white', outline='#999999', width=1)
    draw1.text((bx, by), bt, fill='#666666', anchor='mm', font=font_text)

# 底部说明
draw1.text((400, 530), "(每次对话都从零开始)", fill=colors['text_light'], anchor='mm', font=font_small)

img1.save('/root/.openclaw/workspace/articles/epro-handdrawn/01-goldfish.png')
print("✅ 图1完成: AI金鱼失忆")

# ==================== 图2: 6类记忆分类 ====================
img2 = Image.new('RGB', (900, 600), colors['bg'])
draw2 = ImageDraw.Draw(img2)

# 标题
draw2.text((450, 50), "6 Types of Memory", fill=colors['text'], anchor='mm', font=font_title)

# 6个分类框（手绘矩形，柔和颜色）
categories = [
    ("个人信息", "Personal Info", colors['accent1']),
    ("偏好习惯", "Preferences", colors['accent2']),
    ("相关事物", "Related Things", colors['accent3']),
    ("发生过的事", "Past Events", colors['accent4']),
    ("工作经验", "Work Experience", colors['accent5']),
    ("通用方法论", "Methods", colors['accent6'])
]

# 布局: 3x2
positions = [
    (150, 120), (450, 120), (750, 120),
    (150, 350), (450, 350), (750, 350)
]

border_colors = ['#5A7A9A', '#9A7A5A', '#5A9A7A', '#9A5A5A', '#7A5A9A', '#9A8A5A']
for (cat_cn, cat_en, cat_color), (px, py), border_color in zip(categories, positions, border_colors):
    # 手绘边框
    sketch_rect(draw2, px - 110, py - 70, px + 110, py + 70, 
                fill=cat_color, outline=border_color, width=2)
    # 文字
    draw2.text((px, py - 15), cat_cn, fill=colors['text'], anchor='mm', font=font_text)
    draw2.text((px, py + 15), cat_en, fill=colors['text_light'], anchor='mm', font=font_small)

img2.save('/root/.openclaw/workspace/articles/epro-handdrawn/02-categories.png')
print("✅ 图2完成: 6类记忆分类")

# ==================== 图3: L0/L1/L2三层结构 ====================
img3 = Image.new('RGB', (800, 650), colors['bg'])
draw3 = ImageDraw.Draw(img3)

# 标题
draw3.text((400, 40), "Three-Layer Structure", fill=colors['text'], anchor='mm', font=font_title)
draw3.text((400, 75), "L0 → L1 → L2", fill=colors['text_light'], anchor='mm', font=font_text)

# 三层金字塔
layer_colors = ['#D8E8F5', '#D8F0D8', '#F5E8D8']  # 淡蓝、淡绿、淡橙
layer_heights = [120, 160, 180]
layer_widths = [200, 350, 500]
layer_labels = ["L2: Details", "L1: Summary", "L0: Tags"]
layer_desc = ["Full content", "Structured outline", "One-line summary"]

y_start = 520
for i, (h, w, color, label, desc) in enumerate(zip(layer_heights, layer_widths, layer_colors, layer_labels, layer_desc)):
    y = y_start - sum(layer_heights[:i+1]) + 40
    x_center = 400
    
    # 手绘梯形
    left = x_center - w // 2
    right = x_center + w // 2
    top = y
    bottom = y + h - 10
    
    # 四个角点（梯形）
    if i == 0:  # 顶层是矩形
        points = [(left + 40, top), (right - 40, top), (right, bottom), (left, bottom)]
    else:
        prev_w = layer_widths[i-1] if i > 0 else 0
        offset = (w - prev_w) // 4 if i > 0 else 40
        points = [(left + offset, top), (right - offset, top), (right, bottom), (left, bottom)]
    
    # 抖动
    wobble_points = [(p[0] + random.uniform(-2, 2), p[1] + random.uniform(-2, 2)) for p in points]
    wobble_points.append(wobble_points[0])
    
    # 填充和边框
    draw3.polygon(wobble_points[:-1], fill=layer_colors[i], outline='#5A6A7A', width=2)
    
    # 文字
    mid_y = (top + bottom) // 2
    draw3.text((x_center, mid_y - 10), label, fill=colors['text'], anchor='mm', font=font_text)
    draw3.text((x_center, mid_y + 15), desc, fill=colors['text_light'], anchor='mm', font=font_small)

# 添加箭头说明
arrow_y = 540
draw3.text((400, arrow_y), "▼ Like a library: Title → Catalog → Full Book", 
           fill=colors['text_light'], anchor='mm', font=font_small)

img3.save('/root/.openclaw/workspace/articles/epro-handdrawn/03-layers.png')
print("✅ 图3完成: 三层结构")

# ==================== 图4: 7个AI员工 ====================
img4 = Image.new('RGB', (900, 500), colors['bg'])
draw4 = ImageDraw.Draw(img4)

# 标题
draw4.text((450, 50), "7 AI Agents with Memory", fill=colors['text'], anchor='mm', font=font_title)

# 7个简单手绘机器人
robot_fill_colors = ['#D8E5F0', '#F0E0D0', '#D8F0D8', '#F0D8D8', '#E8D8F0', '#F5EED8', '#D8E8F0']
robot_names = ["Main", "Director", "Nanny", "Writer", "Coder", "Design", "Research"]

start_x = 100
spacing = 115

for i, (fill_color, name) in enumerate(zip(robot_fill_colors, robot_names)):
    cx = start_x + i * spacing
    cy = 280
    
    # 机器人头部（手绘椭圆）
    sketch_ellipse(draw4, cx, cy - 30, 35, 30, fill=fill_color, outline='#666666', width=2)
    
    # 眼睛（两个点）
    draw4.ellipse((cx - 12, cy - 35, cx - 6, cy - 29), fill='#333333')
    draw4.ellipse((cx + 6, cy - 35, cx + 12, cy - 29), fill='#333333')
    
    # 微笑（下半圆弧线）
    smile_points = []
    for angle in range(0, 181, 10):  # 0到180度是下半圆
        rad = math.radians(angle)
        sx = cx + math.cos(rad) * 12
        sy = cy - 18 + math.sin(rad) * 5  # 向下弯曲
        smile_points.append((sx + random.uniform(-1, 1), sy + random.uniform(-1, 1)))
    for j in range(len(smile_points) - 1):
        draw4.line([smile_points[j], smile_points[j+1]], fill='#333333', width=2)
    
    # 身体（简单矩形）
    sketch_rect(draw4, cx - 25, cy, cx + 25, cy + 50, fill=fill_color, outline='#666666', width=2)
    
    # 手臂
    sketch_line(draw4, cx - 25, cy + 15, cx - 40, cy + 35, fill='#666666', width=2)
    sketch_line(draw4, cx + 25, cy + 15, cx + 40, cy + 35, fill='#666666', width=2)
    
    # 名字
    draw4.text((cx, cy + 75), name, fill=colors['text'], anchor='mm', font=font_small)

img4.save('/root/.openclaw/workspace/articles/epro-handdrawn/04-agents.png')
print("✅ 图4完成: 7个AI员工")

print("\n🎉 全部4张手绘风格配图生成完毕！")
print("保存在: /root/.openclaw/workspace/articles/epro-handdrawn/")
