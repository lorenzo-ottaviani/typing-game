"""
Authors : Lorenzo OTTAVIANI, Olivier PORTAL et Thibault CARON.
Date : 27/01/2025 11h45
Aim of the program :
    Execute a typing fruit game with PyGame.
Inputs :
Output :
"""
# Init pygame
from functions.init_pygame import *

# import functions
from functions.menu import menu


def main():
    """"""
running = True
show_menu = False

while running:
    
    # Show background
    SCREEN.blit(BACKGROUND, (0, 0))
    show_menu = True
    # SCREEN.blit(APPLE, (100, 50))
    # SCREEN.blit(BANANA, (650, 350))
    # SCREEN.blit(BOMB, (250, 500))
    # SCREEN.blit(CHERRY, (1000, 50))
    # SCREEN.blit(ICE_CUBE, (150, 150))
    # SCREEN.blit(MANGO, (400, 450))
    # SCREEN.blit(PEAR, (900, 550))
    # SCREEN.blit(STRAWBERRY, (1200, 450))

    for event in pygame.event.get():
        if show_menu == True:
            menu()
        else:
            show_menu = False
        
        if event.type == pygame.QUIT:
            running = False
        
        pygame.display.flip()
        
pygame.quit()
pygame.font.quit()

if __name__ == "__main__":  # The program will be run only if executed directly, not if it is called by another program.
    main()
