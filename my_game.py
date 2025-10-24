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

bullet = pygame.Rect(0, 0, 10, 5)  # x, y, width, height
bullet_speed = 1  # Bullet speed
bullets = []  # list to store bullets

enemy = pygame.Rect(50, 50, 50, 50)  # x, y, width, height

running = True
while running:
    screen.fill((0, 0, 0))
    key = pygame.key.get_pressed()

    # Movement & logic
    movement.handle_movement(player, key, player_speed)
    movement.bound(player, SCREEN_WIDTH, SCREEN_HEIGHT)
    health = combat.collided(player, enemy, health)

    running = keys.quit_game(key)

    # Shooting and bullets
    combat.shoot(bullets, player, key)
    combat.move_bullets(bullets, bullet_speed)
    combat.bullet_hit(bullets, enemy, SCREEN_WIDTH, SCREEN_HEIGHT)

    # Draw
    pygame.draw.rect(screen, (255, 0, 0), player)
    pygame.draw.rect(screen, (0, 255, 0), enemy)
    combat.draw_bullets(screen, bullets)
    
    # Handle window close event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()
