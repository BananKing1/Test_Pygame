import pygame
import random

import movement
import keys
import combat

pygame.init()

# Get the screen size dynamically
info = pygame.display.Info()
SCREEN_WIDTH, SCREEN_HEIGHT = info.current_w, info.current_h

# Create a full-screen window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)

player = pygame.Rect(50, 50, 50, 50)  # x, y, width, height
player_speed = 1  # Movement speed
health = int(5)  # Player health

enemy = pygame.Rect(50, 50, 50, 50)  # x, y, width, height

bullet_speed = 1  # Bullet speed
bullets = []  # list to store bullets

running = True
while running:
    # Handle events first
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys_pressed = pygame.key.get_pressed()

    # Quit on ESC
    if keys_pressed[pygame.K_ESCAPE]:
        running = False

    # Movement & logic
    movement.handle_movement(player, keys_pressed, player_speed)
    movement.bound(player, SCREEN_WIDTH, SCREEN_HEIGHT)
    health = combat.collided(player, enemy, health)

    # Clear screen first
    screen.fill((0, 0, 0))

    # Shooting (move and draw bullets)
    combat.shoot(bullets, player, bullet_speed, screen)

    # Draw player and enemy
    pygame.draw.rect(screen, (255, 0, 0), player)
    pygame.draw.rect(screen, (0, 255, 0), enemy)

    # Handle bullet-enemy collision
    combat.bullet_hit(bullets, enemy, SCREEN_WIDTH, SCREEN_HEIGHT)

    pygame.display.update()


pygame.quit()

