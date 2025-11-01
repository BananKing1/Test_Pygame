import pygame
import random

last_shot = 0
shot_delay = 150  # milliseconds between shots

def shoot(bullets, player, bullet_speed, screen):
    """Handles shooting, moving, and drawing bullets in all directions."""
    global last_shot
    keys = pygame.key.get_pressed()
    now = pygame.time.get_ticks()

    # Shooting UP
    if keys[pygame.K_UP] and now - last_shot > shot_delay:
        bullet = pygame.Rect(player.centerx - 2, player.top, 10, 10)
        bullets.append({'rect': bullet, 'dir': (0, -1)})  # (dx, dy)
        last_shot = now

    # Shooting DOWN
    if keys[pygame.K_DOWN] and now - last_shot > shot_delay:
        bullet = pygame.Rect(player.centerx - 2, player.bottom, 10, 10)
        bullets.append({'rect': bullet, 'dir': (0, 1)})
        last_shot = now

    # Shooting LEFT
    if keys[pygame.K_LEFT] and now - last_shot > shot_delay:
        bullet = pygame.Rect(player.left, player.centery - 2, 10, 10)
        bullets.append({'rect': bullet, 'dir': (-1, 0)})
        last_shot = now

    # Shooting RIGHT
    if keys[pygame.K_RIGHT] and now - last_shot > shot_delay:
        bullet = pygame.Rect(player.right, player.centery - 2, 10, 10)
        bullets.append({'rect': bullet, 'dir': (1, 0)})
        last_shot = now

    # Move bullets
    for bullet in bullets[:]:
        dx, dy = bullet['dir']
        bullet['rect'].x += dx * bullet_speed
        bullet['rect'].y += dy * bullet_speed
        # Remove bullets that leave the screen
        if (bullet['rect'].bottom < 0 or bullet['rect'].top > screen.get_height() or
            bullet['rect'].right < 0 or bullet['rect'].left > screen.get_width()):
            bullets.remove(bullet)

    # Draw bullets
    for bullet in bullets:
        pygame.draw.rect(screen, (255, 255, 0), bullet['rect'])

def bullet_hit(bullets, enemy, sw, sh):
    for bullet in bullets[:]:
        if bullet['rect'].colliderect(enemy):
            bullets.remove(bullet)
            enemy.x = random.randint(0, sw - 50)
            enemy.y = random.randint(0, sh - 50)


def collided(object1, object2, health):
    if object1.colliderect(object2):
        # Move object2 to a new position
        object2.x = random.randint(0, 750)
        object2.y = random.randint(0, 750)
        health -= 1  # Decrease health on hit
        print("Health:", health)
    return health


def asteroid(asteroid, asteroid_speed, asteroid_size, sw, sh):
    # Move cube left
    asteroid.x -= asteroid_speed

    # Reset cube when it leaves the screen & randomize Y
    if asteroid.x < -asteroid_size:
        asteroid.x = sw
        asteroid.y = random.randint(0, sh - asteroid_size)


def bullet_hit_asteroid(bullets, enemy, sw, sh, score):
    for bullet in bullets[:]:
        if bullet['rect'].colliderect(enemy):
            bullets.remove(bullet)
            enemy.x = sw
            enemy.y = random.randint(0, sh - 50)

            score += 100
            print("Score:", score)
    return score

def collided_asteroid(object1, object2, health, sw):
    if object1.colliderect(object2):
        # Move object2 to a new position
        object2.x = sw
        object2.y = random.randint(0, 750)
        health -= 1  # Decrease health on hit
        print("Health:", health)
    return health