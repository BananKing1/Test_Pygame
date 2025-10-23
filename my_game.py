import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = my_game.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
my_game.display.set_caption("My Pygame Window")

player = my_game.Rect(50, 50, 50, 50)  # x, y, width, height


running = True
while running:
    screen.fill(0,0,0)
    
    my_game.draw.rect(screen, (255, 0, 0), player)  # Draw the player as a red rectangle
    
    
    
    for event in my_game.event.get():
        if event.type == my_game.QUIT:
            running = False

    my_game.display.update()
my_game.quit()