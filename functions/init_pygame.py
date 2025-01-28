import pygame
from pygame.locals import *

#initialize pygame
pygame.init()
pygame.font.init()

# Define size of the screen
WIDTH = 1400
HEIGHT = 785
SCREEN_SIZE = 1400, 785
SCREEN = pygame.display.set_mode(SCREEN_SIZE)

# Add background image
BACKGROUND_IMAGE = pygame.image.load("assets/images/wooden_background.jpg")
BACKGROUND = pygame.transform.scale(BACKGROUND_IMAGE, SCREEN_SIZE)

# Font choice
FONT = pygame.font.Font('Tsuchigumo.otf', 50)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Get fruits
APPLE = pygame.image.load("assets/images/fruits/apple.png")
BANANA = pygame.image.load("assets/images/fruits/banana.png")
CHERRY = pygame.image.load("assets/images/fruits/cherry.png")
MANGO = pygame.image.load("assets/images/fruits/mango.png")
PEAR = pygame.image.load("assets/images/fruits/pear.png")
STRAWBERRY = pygame.image.load("assets/images/fruits/strawberry.png")