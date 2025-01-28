"""
Authors : Lorenzo OTTAVIANI, Olivier PORTAL et Thibault CARON.
Date : 27/01/2025 11h45
Aim of the program :
    Execute a typing fruit game with PyGame.
Inputs :
Output :
"""
import pygame

pygame.init()


def main():
    """"""
running = True

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

if __name__ == "__main__":  # The program will be run only if executed directly, not if it is called by another program.
    main()
