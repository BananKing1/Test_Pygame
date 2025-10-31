import pygame
import random

def collided(object1, object2, health):
    if object1.colliderect(object2):
        # Move object2 to a new position
        object2.x = random.randint(0, 750)
        object2.y = random.randint(0, 750)

        health -= 1  # Decrease health on hit
        print( "Health:", health)
    return health

def shoot(bullets, player, key):
    """Create a new bullet when SPACE is pressed."""
    if key[pygame.K_SPACE]:
        bullet = pygame.Rect(player.centerx - 5, player.top, 10, 20)
        bullets.append(bullet)

def move_bullets(bullets, bullet_speed):
    """Move bullets upward and remove them if they go off-screen."""
    for bullet in bullets[:]:
        bullet.y -= bullet_speed
        if bullet.bottom < 0:
            bullets.remove(bullet)

def draw_bullets(screen, bullets):
    """Draw bullets on the screen."""
    for bullet in bullets:
        pygame.draw.rect(screen, (255, 255, 0), bullet)

def bullet_hit(bullets, enemy, screen_width, screen_height):
    """Check for bullet collision with enemy."""
    for bullet in bullets[:]:
        if bullet.colliderect(enemy):
            bullets.remove(bullet)
            enemy.x = random.randint(0, screen_width - 50)
            enemy.y = random.randint(0, screen_height - 50)
