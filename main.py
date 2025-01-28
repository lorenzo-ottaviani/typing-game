"""
Authors : Lorenzo OTTAVIANI, Olivier PORTAL et Thibault CARON.
Date : 27/01/2025 11h45
Aim of the program :
    Execute a typing fruit game with PyGame.
Inputs :
Output :
"""
import pygame
from functions.init_pygame import *


def main():
    """"""
running = True

while running:
    # flags = RESIZABLE
        SCREEN = pygame.display.set_mode(SCREEN_SIZE)

        BACKGROUND = pygame.transform.scale(pygame.image.load(BACKGROUND_IMAGE), SCREEN_SIZE)
        BACKGROUND = SCREEN.blit(BACKGROUND, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

if __name__ == "__main__":  # The program will be run only if executed directly, not if it is called by another program.
    main()
