import pygame

#initialize pygame
pygame.init()

# Define size of the screen and add background
SCREEN_SIZE = 1400, 785
SCREEN = pygame.display.set_mode(SCREEN_SIZE)
BACKGROUND = "assets/images/wooden_background.jpg"

# Font choice
FONT = pygame.font.SysFont('Roboto', 35)
