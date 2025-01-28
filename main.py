"""
Authors : Lorenzo OTTAVIANI, Olivier PORTAL et Thibault CARON.
Date : 27/01/2025 11h45
Aim of the program :
    Execute a typing fruit game with PyGame.
Inputs :
Output :
"""
from functions.init_pygame import *


def main():
    """"""
running = True

while running:
    
    SCREEN.blit(BACKGROUND, (0, 0))
    SCREEN.blit(APPLE, (WIDTH/2, HEIGHT/2))
    SCREEN.blit(BANANA, (WIDTH/3, HEIGHT/3))
    SCREEN.blit(CHERRY, (WIDTH/4, HEIGHT/6))
    SCREEN.blit(MANGO, (WIDTH/6, HEIGHT/4))
    SCREEN.blit(PEAR, (WIDTH/8, HEIGHT))
    SCREEN.blit(STRAWBERRY, (WIDTH/9, HEIGHT/8))

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
        
        pygame.display.flip()
        
pygame.quit()
pygame.font.quit()

if __name__ == "__main__":  # The program will be run only if executed directly, not if it is called by another program.
    main()
