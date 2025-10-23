import pygame

def quit_game(key):
    if key[pygame.K_ESCAPE]:
        return False  # signal to quit
    else:
        return True
    
def pause_game(key):
    return