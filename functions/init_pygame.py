import pygame

#initialize pygame
pygame.init()

# Define size of the screen
SCREEN_SIZE = 1400, 785
SCREEN = pygame.display.set_mode(SCREEN_SIZE)

# Add background image
BACKGROUND = pygame.image.load("assets/images/wooden_background.jpg")
BACKGROUND = pygame.transform.scale(BACKGROUND, SCREEN_SIZE)

# Font choice
FONT = pygame.font.SysFont('Roboto', 35)
