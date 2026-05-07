import pygame
import sys

# Initialize pygame
pygame.init()

# Screen size
WIDTH = 800
HEIGHT = 600

# Create game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Window title
pygame.display.set_caption("Shark & Marina")

# Clock controls FPS
clock = pygame.time.Clock()

# Game loop
running = True

while running:

    # Check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill background with ocean blue
    screen.fill((0, 119, 190))

    # Update screen
    pygame.display.update()

    # 60 FPS
    clock.tick(60)

pygame.quit()
sys.exit()