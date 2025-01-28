"""
Authors : Lorenzo OTTAVIANI, Olivier PORTAL et Thibault CARON.
Date : 27/01/2025 11h45
Aim of the program :
    Execute a typing fruit game with PyGame.
Inputs :
Output :
"""
import pygame
import random
screen = pygame.display.set_mode((640, 240))

def main():
    """"""
    app_running = True
    while app_running:
        
        for event in pygame.event.get():
            print(event)

            if event.type == pygame.KEYDOWN:
                if event.key == 27 or event.key == 13: #esc or enter keys
                    app_running = False

        if event.type == pygame.QUIT:
            app_running = False

        # if event.unicode == "/x1b":
        #     app_running = False


if __name__ == "__main__":  # The program will be run only if executed directly, not if it is called by another program.
    main()
