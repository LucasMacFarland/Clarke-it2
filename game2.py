import pygame
import random
import sys

# initialize pygame
pygame.init()

# screen settings
WIDTH, HEIGHT = 700, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Run for Your Life")

# Colors
WHITE = (230, 255, 255)

# Player settings
player_size = 50
player_pos = [random.randint(0, WIDTH - player_size), HEIGHT - player_size - 10]
player_speed = 5  # Reduced for smoother movement
player_lives = 3
player_score = 0

# Load player image
player_image = pygame.image.load("images/image2.png")
player_image = pygame.transform.scale(player_image, (player_size, player_size))
player_rect = player_image.get_rect(topleft=player_pos)
player_mask = pygame.mask.from_surface(player_image)
player_jump = False

# Frame rate
clock = pygame.time.Clock()
FPS = 60

# Game loop
running = True
while running:
    clock.tick(FPS)

    # --- Event Handling ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- Movement Keys ---
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player_rect.x -= player_speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player_rect.x += player_speed
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player_rect.y -= player_speed
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player_rect.y += player_speed

    # --- Boundary Checking ---
    if player_rect.left < 0:
        player_rect.left = 0
    if player_rect.right > WIDTH:
        player_rect.right = WIDTH
    if player_rect.top < 0:
        player_rect.top = 0
    if player_rect.bottom > HEIGHT:
        player_rect.bottom = HEIGHT

    # --- Drawing ---
    screen.fill(WHITE)
    screen.blit(player_image, player_rect.topleft)
    pygame.display.flip()

# Exit cleanly
pygame.quit()
sys.exit()












