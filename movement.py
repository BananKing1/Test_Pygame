import pygame

def handle_movement(object, key, player_speed):
    # Movement (use independent ifs for diagonal movement)   
    if key[pygame.K_a]:
        object.move_ip(-player_speed, 0)
    if key[pygame.K_d]:
        object.move_ip(player_speed, 0)
    if key[pygame.K_w]:
        object.move_ip(0, -player_speed)
    if key[pygame.K_s]:
        object.move_ip(0, player_speed)

def bound(object, screen_width, screen_height):
    # Keep object inside the screen
    if object.left < 0:
        object.left = 0
    if object.right > screen_width:
        object.right = screen_width
    if object.top < 0:
        object.top = 0
    if object.bottom > screen_height:
        object.bottom = screen_height