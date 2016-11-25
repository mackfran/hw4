# Name: Mackenzie Francisco
# uniqname: mackfran
# Section Day/Time: Thursday/1-2PM
# References:

import pygame
pygame.init();

# creates colors
white = (255,255,255)
black = (0,0,0)
red = (255, 0, 0)
green = (0, 255, 0)

# creates a surface
gameDisplay = pygame.display.set_mode((800,600)) # initializes with a tuple

# adds a title
pygame.display.set_caption("Decorating Disaster!")

pygame.display.update()