import pygame
import math
import random
import sys

# เริ่มต้นการทำงานของ Pygame
pygame.init()

# ตั้งค่าขนาดหน้าจอ
WIDTH, HEIGHT = 700, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Multi-Language Heart Art")

# กำหนดสี (RGB)
BLACK = (0, 0, 0)
RED = (255, 50, 50)

# รายชื่อคำบอกรักหลากหลายภาษา
LOVE_WORDS = [
    "ฉันรักเธอ", "I love you", "Ich liebe dich", "Ti amo", "Je t'aime", 
    "Te amo", "愛してる", "사랑해", "Aku cinta kamu", "Seni seviyorum", 
    "Я тебя люблю", "Eu te amo", "Jag älskar dig", "Я тебе кохаю", "Σ' αγαπώ"
]

# ฟังก์ชันคำนวณพิกัดรูปหัวใจ (Parametric Heart Equations)
def get_heart_coordinate(t, scale=14):
    # สมการรูปหัวใจ
    x = 16 * (math.sin(t) ** 3)
    y = 13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t)
    
    # ปรับขนาดและย้ายตำแหน่งให้อยู่กึ่งกลางหน้าจอ
    pixel_x = int(WIDTH / 2 + x * scale)
    pixel_y = int(HEIGHT / 2 - y * scale) # ลบ y เพราะพิกัดจอคอมพิวเตอร์นับลงล่างเป็นบวก
    return pixel_x, pixel_y

# เลือกใช้ฟอนต์ระบบ (รองรับภาษาไทยและภาษาอื่นๆ)
try:
    font = pygame.font.SysFont("Arial", 14)
except:
    font = pygame.font.get_default_font()

# เตรียมข้อความที่จะวาด
rendered_texts = []
# ทำซ้ำเพื่อสร้างจุดคำหนาแน่นพอจนเห็นเป็นรูปทรง
for _ in range(400):
    t = random.uniform(0, 2 * math.pi)
    
    # สุ่มระยะกระจายตัวให้อยู่รอบๆ เส้นขอบและภายในหัวใจเล็กน้อย
    spread = random.uniform(0.8, 1.05) 
    x, y = get_heart_coordinate(t, scale=14 * spread)
    
    word = random.choice(LOVE_WORDS)
    text_surface = font.render(word, True, RED)
    text_rect = text_surface.get_rect(center=(x, y))
    rendered_texts.append((text_surface, text_rect))

# Main Loop สำหรับแสดงผลหน้าจอ
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill(BLACK)
    
    # วาดคำบอกรักทั้งหมดลงบนหน้าจอ
    for text_surface, text_rect in rendered_texts:
        screen.blit(text_surface, text_rect)
        
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
