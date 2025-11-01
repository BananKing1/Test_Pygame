import pygame
import random

import movement
import keys
import combat

pygame.init()

# Get the screen size dynamically
info = pygame.display.Info()
SCREEN_WIDTH  = info.current_w 
SCREEN_HEIGHT = info.current_h

# Create a full-screen window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)

pygame.display.set_caption("Our game")

player = pygame.Rect(50, 50, 50, 50)  # x, y, width, height
player_speed = 1  # Movement speed
health = int(5)  # Player health
score = int(0)

enemy = pygame.Rect(50, 50, 50, 50)  # x, y, width, height

bullet_speed = 1  # Bullet speed
bullets = []  # list to store bullets

clock = pygame.time.Clock()

asteroid = pygame.Rect(50, 50, 50, 50)
asteroid_speed = 1
asteroid_size = 40
asteroid_x = SCREEN_WIDTH
asteroid_y = random.randint(0, SCREEN_HEIGHT - asteroid_size)


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
    health = combat.collided_asteroid(player, asteroid, health, SCREEN_HEIGHT)

    # Clear screen first
    screen.fill((0, 0, 0))

    # Shooting (move and draw bullets)
    combat.shoot(bullets, player, bullet_speed, screen)

    # Draw player and enemy
    pygame.draw.rect(screen, (255, 0, 0), player)
    pygame.draw.rect(screen, (0, 255, 0), enemy)

    # Handle bullet-enemy collision
    combat.bullet_hit(bullets, enemy, SCREEN_WIDTH, SCREEN_HEIGHT)

    combat.asteroid(asteroid, asteroid_speed, asteroid_size, SCREEN_WIDTH, SCREEN_HEIGHT)
    pygame.draw.rect(screen, (255, 0, 0), asteroid)
    pygame.draw.rect(screen, (255, 0, 0), asteroid)
    score = combat.bullet_hit_asteroid(bullets, asteroid, SCREEN_WIDTH, SCREEN_HEIGHT, score)

    pygame.display.update()


pygame.quit()

