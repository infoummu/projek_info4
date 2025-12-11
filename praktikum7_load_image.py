import pygame
import sys

# Inisialisasi Pygame
pygame.init()

# Set ukuran layar
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Praktikum 6 - Manipulasi Gambar")

# Warna
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Memuat gambar background
try:
    background = pygame.image.load('grase.jpeg')  # Ganti dengan path gambar Anda
    # Mengatur ukuran background sesuai layar
    background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
except:
    print("File background.jpg tidak ditemukan!")
    # Buat background default jika file tidak ditemukan
    background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    background.fill((100, 150, 200))  # Warna biru muda

# Memuat gambar foreground (karakter atau objek)
try:
    character = pygame.image.load('kelinci.webp')  # Ganti dengan path gambar Anda
    # Mengatur ukuran character
    character_width = 100
    character_height = 150
    character = pygame.transform.scale(character, (character_width, character_height))
except:
    print("File character.png tidak ditemukan!")
    # Buat karakter default jika file tidak ditemukan
    character = pygame.Surface((200, 300))
    character.fill((255, 0, 0))  # Warna merah

# Posisi character (di tengah layar)
character_x = (SCREEN_WIDTH - character.get_width()) // 2
character_y = (SCREEN_HEIGHT - character.get_height()) // 2

# Font untuk teks
font = pygame.font.Font(None, 36)

# Loop utama
running = True
clock = pygame.time.Clock()
x, y = character_x, character_y
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    
    # Menggambar background
    screen.blit(background, (0, 0))
    
    # Menggambar character di atas background
    
    screen.blit(character, (x, y))
    x, y = x+5, y+5
     
    
    # Menambahkan teks informasi
    info_text = font.render("Praktikum 6 - Load Image dengan Pygame", True, BLACK)
    screen.blit(info_text, (50, 50))
    
    # Update display
    pygame.display.flip()
    
    # Mengatur FPS
    clock.tick(60)

# Keluar dari Pygame
pygame.quit()
sys.exit()