#!/usr/bin/env python3
"""
ARC Reactor Watch Generator — Triangular shape, red/neon gradient + blue/green electric signals
Dark black background. Generates reference frames.
Uses: Pillow (PIL) + numpy. Works on Termux/Android/aarch64.
"""
import math, os
from PIL import Image, ImageDraw
import numpy as np

WIDTH, HEIGHT = 1920, 1080
FPS = 30
DURATION = 8
TOTAL_FRAMES = DURATION * FPS
FRAMES_DIR = "/data/data/com.termux/files/home/jarvis-ai-portfolio/frames/arc_reactor"
os.makedirs(FRAMES_DIR, exist_ok=True)

BG_BLACK = (0, 0, 0)
NEON_RED = (255, 0, 52)
NEON_BLUE = (0, 150, 255)
NEON_GREEN = (72, 255, 130)
WHITE_GLOW = (255, 255, 255)

def render_frame(frame_num):
    t = frame_num / FPS
    img = Image.new('RGB', (WIDTH, HEIGHT), BG_BLACK)
    draw = ImageDraw.Draw(img)
    cx, cy = WIDTH // 2, HEIGHT // 2
    size = 350
    
    # Rotation
    rot = t * 0.5
    
    # Outer triangle (red gradient)
    verts = []
    for i in range(3):
        angle = rot + i * (2 * math.pi / 3) - math.pi / 2
        verts.append((cx + size * math.cos(angle), cy + size * math.sin(angle)))
    
    # Fill triangle with red gradient
    for i in range(3):
        x1, y1 = verts[i]
        x2, y2 = verts[(i+1) % 3]
        r = 255 if i == 0 else 200
        g = 0 if i < 2 else 50
        b = 52 if i < 2 else 30
        draw.polygon([verts[i], verts[(i+1) % 3], (cx, cy)], fill=(r, g, b))
    
    # Inner triangle (blue, rotating opposite)
    inner_r = size * 0.65
    inner_verts = []
    for i in range(3):
        angle = -rot * 1.3 + i * (2 * math.pi / 3) - math.pi / 2
        inner_verts.append((cx + inner_r * math.cos(angle), cy + inner_r * math.sin(angle)))
    
    for i in range(3):
        draw.polygon([inner_verts[i], inner_verts[(i+1) % 3], (cx, cy)], fill=(0, 100, 255))
    
    # Watch face circle
    face_r = size * 0.28
    draw.ellipse([cx-face_r, cy-face_r, cx+face_r, cy+face_r], fill=(10, 0, 20), outline=NEON_RED, width=3)
    
    # Crystal glass
    draw.ellipse([cx-face_r*0.8, cy-face_r*0.8, cx+face_r*0.8, cy+face_r*0.8],
                 outline=WHITE_GLOW, width=2)
    
    # Electric arcs between outer and inner vertices
    for i in range(3):
        x1, y1 = verts[i]
        x2, y2 = inner_verts[i]
        for j in range(4):
            frac = j / 3
            px = x1 + (x2 - x1) * frac
            py = y1 + (y2 - y1) * frac
            offset = math.sin(t * 8 + j * 1.5 + i * 2) * 12
            angle_perp = math.atan2(y2 - y1, x2 - x1) + math.pi / 2
            arc_x = px + offset * math.cos(angle_perp)
            arc_y = py + offset * math.sin(angle_perp)
            color = NEON_GREEN if i % 2 == 0 else NEON_BLUE
            draw.ellipse([arc_x-3, arc_y-3, arc_x+3, arc_y+3], fill=color)
            if j > 0:
                prev_x = x1 + (x2 - x1) * ((j-1)/3)
                prev_y = y1 + (y2 - y1) * ((j-1)/3)
                p_angle = math.atan2(y2 - y1, x2 - x1) + math.pi / 2
                p_off = math.sin(t * 8 + (j-1) * 1.5 + i * 2) * 12
                p_x = prev_x + p_off * math.cos(p_angle)
                p_y = prev_y + p_off * math.sin(p_angle)
                draw.line([(p_x, p_y), (arc_x, arc_y)], fill=color, width=2)
    
    # Glowing white elements at outer vertices
    for i, (vx, vy) in enumerate(verts):
        glow_r = 8 + 4 * math.sin(t * 5 + i * 2)
        for g in range(1, 4):
            a = int(100 / g)
            draw.ellipse([vx - glow_r*(1+g*0.3), vy - glow_r*(1+g*0.3),
                         vx + glow_r*(1+g*0.3), vy + glow_r*(1+g*0.3)],
                         fill=(255, 255, 255, a))
        draw.ellipse([vx - glow_r, vy - glow_r, vx + glow_r, vy + glow_r], fill=WHITE_GLOW)
    
    # Clock hands
    ha = t * 0.2
    draw.line([(cx, cy), (cx + face_r*0.4*math.cos(ha), cy + face_r*0.4*math.sin(ha))], fill=NEON_RED, width=3)
    ma = t * 1.2
    draw.line([(cx, cy), (cx + face_r*0.6*math.cos(ma), cy + face_r*0.6*math.sin(ma))], fill=NEON_BLUE, width=2)
    sa = t * 6
    draw.line([(cx, cy), (cx + face_r*0.5*math.cos(sa), cy + face_r*0.5*math.sin(sa))], fill=NEON_GREEN, width=1)
    
    # Center hub
    draw.ellipse([cx-10, cy-10, cx+10, cy+10], fill=WHITE_GLOW)
    draw.ellipse([cx-5, cy-5, cx+5, cy+5], fill=NEON_RED)
    
    # Electric particles
    for i in range(60):
        angle = (i / 60) * 2 * math.pi + t * 0.3
        r = 80 + 40 * math.sin(t * 2 + i)
        px = cx + r * math.cos(angle + t * 0.5)
        py = cy + r * math.sin(angle + t * 0.5)
        color = NEON_BLUE if i % 2 == 0 else NEON_GREEN
        s = 2 + math.sin(t * 5 + i) * 1.5
        for g in range(1, 3):
            a = int(60 / g)
            draw.ellipse([px-s*g, py-s*g, px+s*g, py+s*g], fill=(color[0], color[1], color[2], a))
        draw.ellipse([px-s, py-s, px+s, py+s], fill=color)
    
    # Scan lines
    for y in range(0, HEIGHT, 4):
        draw.line([(0, y), (WIDTH, y)], fill=(0, 0, 0, 3))
    
    return img

def main():
    print(f"Generating {TOTAL_FRAMES} ARC Reactor Watch frames...")
    for i in range(TOTAL_FRAMES):
        if i % 30 == 0: print(f"  Frame {i}/{TOTAL_FRAMES}")
        img = render_frame(i)
        img.save(os.path.join(FRAMES_DIR, f"watch_{i:04d}.jpg"), "JPEG", quality=95)
    print(f"✅ {TOTAL_FRAMES} frames saved to {FRAMES_DIR}")

if __name__ == '__main__':
    main()
