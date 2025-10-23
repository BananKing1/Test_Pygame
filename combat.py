import pygame
import random

def hitbox(object1, object2, health):
    if object1.colliderect(object2):
        # Move object2 to a new position
        object2.x = random.randint(0, 750)
        object2.y = random.randint(0, 750)

        health -= 1  # Decrease health on hit
        print( "Health:", health)
    return health