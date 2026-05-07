import pygame
import sys
import math
import random

pygame.init()

# ======================
# SCREEN
# ======================
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shark & Marina")

clock = pygame.time.Clock()

# ======================
# LOAD IMAGES
# ======================
player_img = pygame.image.load("assets/marina.png")
shark_img = pygame.image.load("assets/shark.png")

player_img = pygame.transform.scale(player_img, (50, 50))
shark_img = pygame.transform.scale(shark_img, (80, 50))

# ======================
# GAME STATE
# ======================
running = True
game_over = False

# ======================
# PLAYER
# ======================
player_x, player_y = 100, 300
player_speed = 5

# ======================
# SHARK
# ======================
shark_x, shark_y = 600, 300
shark_speed = 2

# ======================
# SCORE
# ======================
score = 0

# wave animation
wave_offset = 0

# ======================
# GAME LOOP
# ======================
while running:
    clock.tick(60)

    # ======================
    # EVENTS
    # ======================
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ======================
    # GAME OVER SCREEN
    # ======================
    if game_over:
        screen.fill((0, 0, 0))

        font = pygame.font.SysFont(None, 70)
        text = font.render("GAME OVER", True, (255, 0, 0))
        screen.blit(text, (WIDTH//2 - 170, HEIGHT//2 - 80))

        font2 = pygame.font.SysFont(None, 30)
        text2 = font2.render("Press R to Restart | Q to Quit", True, (255, 255, 255))
        screen.blit(text2, (WIDTH//2 - 200, HEIGHT//2))

        keys = pygame.key.get_pressed()

        if keys[pygame.K_r]:
            player_x, player_y = 100, 300
            shark_x, shark_y = 600, 300
            score = 0
            game_over = False

        if keys[pygame.K_q]:
            running = False

        pygame.display.update()
        continue

    # ======================
    # PLAYER MOVEMENT
    # ======================
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # boundaries
    player_x = max(0, min(WIDTH - 50, player_x))
    player_y = max(0, min(HEIGHT - 50, player_y))

    # ======================
    # SHARK AI (randomized chase)
    # ======================
    if random.randint(0, 100) < 85:  # adds unpredictability
        if shark_x < player_x:
            shark_x += shark_speed
        if shark_x > player_x:
            shark_x -= shark_speed

        if shark_y < player_y:
            shark_y += shark_speed
        if shark_y > player_y:
            shark_y -= shark_speed

    # ======================
    # SCORE (survival time)
    # ======================
    score += 1

    # ======================
    # OCEAN BACKGROUND (gradient)
    # ======================
    for y in range(HEIGHT):
        color = (0, 80 + y // 6, 160 + y // 10)
        pygame.draw.line(screen, color, (0, y), (WIDTH, y))

    # ======================
    # WAVES
    # ======================
    wave_offset += 2

    for x in range(0, WIDTH, 20):
        y = HEIGHT // 2 + 20 * math.sin((x + wave_offset) * 0.05)
        pygame.draw.circle(screen, (255, 255, 255), (x, int(y)), 3)

    # ======================
    # DRAW PLAYER
    # ======================
    screen.blit(player_img, (player_x, player_y))

    # ======================
    # DRAW SHARK
    # ======================
    screen.blit(shark_img, (shark_x, shark_y))

    # ======================
    # SCORE TEXT
    # ======================
    font = pygame.font.SysFont(None, 30)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # ======================
    # COLLISION
    # ======================
    player_rect = pygame.Rect(player_x, player_y, 50, 50)
    shark_rect = pygame.Rect(shark_x, shark_y, 80, 50)

    if player_rect.colliderect(shark_rect):
        game_over = True

    pygame.display.update()

pygame.quit()
sys.exit()