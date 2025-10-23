import pygame
import movement
import keys

pygame.init()

# Get the screen size dynamically
info = pygame.display.Info()
SCREEN_WIDTH, SCREEN_HEIGHT = info.current_w, info.current_h

# Create a full-screen window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)

player = pygame.Rect(50, 50, 50, 50)  # x, y, width, height
player_speed = 1  # Movement speed

enemy = pygame.Rect(50, 50, 50, 50)  # x, y, width, height

running = True
while running:
    screen.fill((0, 0, 0))  # Fill background with black
    
    pygame.draw.rect(screen, (255, 0, 0), player)  # Draw the player
    pygame.draw.rect(screen, (0, 255, 0), enemy)

    # Get key states
    key = pygame.key.get_pressed()

    movement.handle_movement(player,key, player_speed)
    movement.bound(player, SCREEN_WIDTH, SCREEN_HEIGHT)
    running = keys.quit_game(key)  # Check for quit condition
    
    # Handle window close event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()
