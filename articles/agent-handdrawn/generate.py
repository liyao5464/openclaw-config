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

def sketch_circle(draw, cx, cy, r, fill=None, outline='#444', width=2):
    """画手绘风格的圆"""
    points = []
    steps = 50
    for i in range(steps + 1):
        angle = (i / steps) * 2 * math.pi
        x = cx + math.cos(angle) * (r + random.uniform(-2, 2))
        y = cy + math.sin(angle) * (r + random.uniform(-2, 2))
        points.append((x, y))
    if fill:
        draw.polygon(points[:-1], fill=fill)
    for i in range(len(points) - 1):
        draw.line([points[i], points[i+1]], fill=outline, width=width)

# 柔和配色
colors = {
    'bg': '#FAFAF8',
    'text': '#444444',
    'text_light': '#666666',
    'blue': '#D8E5F0',
    'green': '#D8F0D8',
    'orange': '#F5E8D8',
    'pink': '#F0E0E0',
    'purple': '#E8E0F0',
    'line': '#555555',
    'red': '#E8C8C8',
    'yellow': '#F5F0D8'
}

# 加载中文字体
try:
    font_title = ImageFont.truetype("/usr/share/fonts/google-noto-cjk/NotoSansCJK-DemiLight.ttc", 26)
    font_text = ImageFont.truetype("/usr/share/fonts/google-noto-cjk/NotoSansCJK-Light.ttc", 16)
    font_small = ImageFont.truetype("/usr/share/fonts/google-noto-cjk/NotoSansCJK-Light.ttc", 14)
except:
    font_title = ImageFont.load_default()
    font_text = ImageFont.load_default()
    font_small = ImageFont.load_default()

# ==================== 图1: 四层记忆架构 ====================
img1 = Image.new('RGB', (700, 550), colors['bg'])
draw1 = ImageDraw.Draw(img1)

# 标题
draw1.text((350, 45), "四层记忆架构", fill=colors['text'], anchor='mm', font=font_title)

# 四层盒子
layers = [
    ("1. 个人画像层", "SOUL.md  USER.md", colors['blue']),
    ("2. 工作记忆层", "每日素材", colors['green']),
    ("3. 素材库层", "选题库  读者画像", colors['orange']),
    ("4. 决策层", "HEARTBEAT.md", colors['pink'])
]

box_width = 420
box_height = 80
start_y = 100
spacing = 15

for i, (title, content, color) in enumerate(layers):
    y = start_y + i * (box_height + spacing)
    x = 350 - box_width // 2
    
    # 手绘框
    sketch_rect(draw1, x, y, x + box_width, y + box_height, fill=color, outline='#666', width=2)
    
    # 文字
    draw1.text((350, y + 25), title, fill=colors['text'], anchor='mm', font=font_text)
    draw1.text((350, y + 55), content, fill=colors['text_light'], anchor='mm', font=font_small)
    
    # 向下箭头（除了最后一层）
    if i < len(layers) - 1:
        arrow_y = y + box_height + 2
        sketch_line(draw1, 350, arrow_y, 350, arrow_y + spacing - 4, fill='#888', width=2)
        # 箭头尖端
        draw1.polygon([(345, arrow_y + spacing - 6), (355, arrow_y + spacing - 6), (350, arrow_y + spacing - 1)], fill='#888')

img1.save('/root/.openclaw/workspace/articles/agent-handdrawn/01-four-layers.png')
print("✅ 图1完成: 四层记忆架构")

# ==================== 图2: 先培训再上岗 ====================
img2 = Image.new('RGB', (700, 400), colors['bg'])
draw2 = ImageDraw.Draw(img2)

# 左边小人（手绘）
def draw_stick_figure(draw, cx, cy, color='#5A7A9A'):
    # 头
    sketch_circle(draw, cx, cy - 35, 20, fill=color, outline='#444', width=2)
    # 身体
    sketch_line(draw, cx, cy - 15, cx, cy + 30, fill='#444', width=2)
    # 手臂
    sketch_line(draw, cx - 20, cy, cx - 5, cy + 10, fill='#444', width=2)
    sketch_line(draw, cx + 20, cy, cx + 5, cy + 10, fill='#444', width=2)
    # 腿
    sketch_line(draw, cx, cy + 30, cx - 15, cy + 60, fill='#444', width=2)
    sketch_line(draw, cx, cy + 30, cx + 15, cy + 60, fill='#444', width=2)

# 左边人
draw_stick_figure(draw2, 150, 180, colors['orange'])

# 中间气泡（手绘椭圆）
sketch_rect(draw2, 220, 100, 520, 250, fill=colors['yellow'], outline='#888', width=2)
draw2.text((370, 175), "先培训", fill=colors['text'], anchor='mm', font=font_title)
draw2.text((370, 210), "再上岗", fill=colors['text'], anchor='mm', font=font_title)

# 右边机器人（简单几何形状）
# 机器人头
sketch_rect(draw2, 580, 130, 640, 180, fill=colors['blue'], outline='#444', width=2)
# 眼睛
draw2.ellipse((595, 145, 605, 155), fill='#333')
draw2.ellipse((615, 145, 625, 155), fill='#333')
# 天线
sketch_line(draw2, 600, 130, 595, 115, fill='#444', width=2)
sketch_line(draw2, 620, 130, 625, 115, fill='#444', width=2)
# 身体
sketch_rect(draw2, 570, 190, 650, 260, fill=colors['blue'], outline='#444', width=2)
# 手里拿着文件
sketch_rect(draw2, 540, 200, 570, 240, fill='white', outline='#666', width=1)
draw2.text((555, 220), "SOUL", fill=colors['text_light'], anchor='mm', font=font_small)
sketch_rect(draw2, 530, 220, 560, 260, fill='white', outline='#666', width=1)
draw2.text((545, 240), "USER", fill=colors['text_light'], anchor='mm', font=font_small)

img2.save('/root/.openclaw/workspace/articles/agent-handdrawn/02-training.png')
print("✅ 图2完成: 先培训再上岗")

# ==================== 图3: 一天工作流 ====================
img3 = Image.new('RGB', (800, 400), colors['bg'])
draw3 = ImageDraw.Draw(img3)

# 三个时间点
times = [
    ("08:00", "Agent自动搜集", colors['blue']),
    ("08:05", "5分钟确认选题", colors['green']),
    ("白天", "专注写作", colors['orange'])
]

start_x = 150
spacing_x = 250

for i, (time, desc, color) in enumerate(times):
    cx = start_x + i * spacing_x
    cy = 180
    
    # 手绘圆圈
    sketch_circle(draw3, cx, cy, 60, fill=color, outline='#666', width=2)
    
    # 时间
    draw3.text((cx, cy - 10), time, fill=colors['text'], anchor='mm', font=font_text)
    
    # 描述
    draw3.text((cx, cy + 85), desc, fill=colors['text'], anchor='mm', font=font_small)
    
    # 连接线
    if i < len(times) - 1:
        sketch_line(draw3, cx + 65, cy, cx + spacing_x - 65, cy, fill='#888', width=2)
        # 箭头
        draw3.polygon([(cx + spacing_x - 70, cy - 5), (cx + spacing_x - 70, cy + 5), (cx + spacing_x - 60, cy)], fill='#888')

# 底部文字
draw3.text((400, 320), "以前2小时 → 现在5分钟", fill=colors['text'], anchor='mm', font=font_title)

img3.save('/root/.openclaw/workspace/articles/agent-handdrawn/03-workflow.png')
print("✅ 图3完成: 一天工作流")

# ==================== 图4: IP调优对比 ====================
img4 = Image.new('RGB', (800, 450), colors['bg'])
draw4 = ImageDraw.Draw(img4)

# 左边：错误示例
sketch_rect(draw4, 80, 100, 380, 350, fill=colors['red'], outline='#966', width=2)
draw4.text((230, 140), "❌ 错误", fill='#844', anchor='mm', font=font_text)
draw4.text((230, 200), "USER.md", fill=colors['text'], anchor='mm', font=font_text)
draw4.text((230, 230), "只写2行", fill=colors['text'], anchor='mm', font=font_text)
draw4.text((230, 300), "推送不精准", fill=colors['text_light'], anchor='mm', font=font_small)

# 中间分隔线
sketch_line(draw4, 400, 80, 400, 370, fill='#CCC', width=2)

# 右边：正确示例
sketch_rect(draw4, 420, 100, 720, 350, fill=colors['green'], outline='#696', width=2)
draw4.text((570, 140), "✓ 正确", fill='#464', anchor='mm', font=font_text)
draw4.text((570, 190), "详细读者画像", fill=colors['text'], anchor='mm', font=font_text)
draw4.text((570, 220), "+", fill=colors['text'], anchor='mm', font=font_text)
draw4.text((570, 250), "内容方向", fill=colors['text'], anchor='mm', font=font_text)
draw4.text((570, 310), "推送精准80%", fill='#464', anchor='mm', font=font_text)

# 底部箭头
draw4.text((400, 400), "详细程度决定效果", fill=colors['text_light'], anchor='mm', font=font_small)

img4.save('/root/.openclaw/workspace/articles/agent-handdrawn/04-tuning.png')
print("✅ 图4完成: IP调优对比")

# ==================== 图5: 从1个开始 ====================
img5 = Image.new('RGB', (700, 450), colors['bg'])
draw5 = ImageDraw.Draw(img5)

# 阶梯图（手绘风格）
# 第一层
sketch_rect(draw5, 80, 320, 250, 380, fill=colors['blue'], outline='#666', width=2)
draw5.text((165, 335), "1个Agent", fill=colors['text'], anchor='mm', font=font_text)
draw5.text((165, 360), "找素材", fill=colors['text_light'], anchor='mm', font=font_small)

# 第二层
sketch_rect(draw5, 250, 260, 450, 320, fill=colors['green'], outline='#666', width=2)
draw5.text((350, 275), "3个Agent", fill=colors['text'], anchor='mm', font=font_text)
draw5.text((350, 300), "写稿+排版+发布", fill=colors['text_light'], anchor='mm', font=font_small)

# 第三层
sketch_rect(draw5, 450, 200, 650, 260, fill=colors['orange'], outline='#666', width=2)
draw5.text((550, 215), "N个Agent", fill=colors['text'], anchor='mm', font=font_text)
draw5.text((550, 240), "全自动", fill=colors['text_light'], anchor='mm', font=font_small)

# 小人站在第一层
# 头
sketch_circle(draw5, 165, 285, 15, fill=colors['orange'], outline='#444', width=2)
# 身体
sketch_line(draw5, 165, 270, 165, 245, fill='#444', width=2)
# 手臂（向上指）
sketch_line(draw5, 165, 255, 180, 240, fill='#444', width=2)
# 腿
sketch_line(draw5, 165, 320, 155, 320, fill='#444', width=2)
sketch_line(draw5, 165, 320, 175, 320, fill='#444', width=2)

# 标题
draw5.text((350, 80), "从1个开始", fill=colors['text'], anchor='mm', font=font_title)
draw5.text((350, 115), "慢慢扩展", fill=colors['text_light'], anchor='mm', font=font_small)

# 箭头指示
draw5.text((350, 420), "↑ 一步一步来", fill=colors['text_light'], anchor='mm', font=font_small)

img5.save('/root/.openclaw/workspace/articles/agent-handdrawn/05-start.png')
print("✅ 图5完成: 从1个开始")

print("\n🎉 全部5张手绘风格配图生成完毕！")
print("保存在: /root/.openclaw/workspace/articles/agent-handdrawn/")
