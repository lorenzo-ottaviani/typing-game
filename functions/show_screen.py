import pygame

# Initialisation de Pygame
pygame.init()
pygame.font.init()

# Taille de la fenêtre de jeu
SCREEN_SIZE = 1400, 785
SCREEN = pygame.display.set_mode(SCREEN_SIZE)
BACKGROUND = "assets/images/wooden_background.jpg"

# Choix de la police
FONT = pygame.font.SysFont('Roboto', 35)
