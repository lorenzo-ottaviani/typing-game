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
from functions.play_music import draw_music_button



def main():
    """"""
# Init data
game_state = "menu"
music_state = "on"
max_objects = 4  # max number of obejects on screen at the same time (for difficulty & game)
frame_countdown = 45 
score = 0 
player_lives = 3
objects = []
frozen = False
frozen_timer = 900  # 900 frames /60 = 15
# input_type = None
# level = 1

SCREEN.blit(BACKGROUND, (0, 0))

running = True



while running:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False

        elif game_state == "menu":
            game_state, running, music_state = menu(event, game_state, running, music_state)

        elif game_state == "game":

            game_state, frame_countdown, score, player_lives, objects, frozen, frozen_timer, frame_countdown = play_game(event, frame_countdown, score, player_lives, objects, frozen, frozen_timer)
   
    draw_music_button(music_state)
    pygame.display.flip()
    clock.tick(60) 
        
pygame.quit()
pygame.font.quit()

if __name__ == "__main__":  # The program will be run only if executed directly, not if it is called by another program.
    main()
