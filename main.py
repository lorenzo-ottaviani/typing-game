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
from functions.play_game import play_game


def main():
    """"""
# Init data
game_state = "menu"
max_objects = 4  # max number of obejects on screen at the same time (for difficulty & game)

loop = 0  # for testing

SCREEN.blit(BACKGROUND, (0, 0))

running = True

while running:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False

        if game_state == "menu":
            game_state = menu(event, game_state)

        elif game_state == "game":
            play_game(event)
            
            SCREEN.blit(APPLE, (100, 50))
            SCREEN.blit(BANANA, (650, 350))
            SCREEN.blit(BOMB, (250, 500))
            SCREEN.blit(CHERRY, (1000, 50))
            SCREEN.blit(ICE_CUBE, (150, 150))
            SCREEN.blit(MANGO, (400, 450))
            SCREEN.blit(PEAR, (900, 550))
            SCREEN.blit(STRAWBERRY, (1200, 450))
        
    pygame.display.flip()
    clock.tick(60) 
        
pygame.quit()
pygame.font.quit()

if __name__ == "__main__":  # The program will be run only if executed directly, not if it is called by another program.
    main()
