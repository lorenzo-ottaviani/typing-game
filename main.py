"""
Authors : Lorenzo OTTAVIANI, Olivier PORTAL et Thibault CARON.
Date : 31/01/2025 11h05
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
from functions.draw_text import draw_text



def main():
    """

    :return: 
    """
# Init data
game_state = "menu"
music_state = "on"
difficulty = "medium"
max_objects = 4  # max number of obejects on screen at the same time (for difficulty & game)
frame_countdown = 10
score = 0 
player_lives = 3
objects = []
frozen = False
frozen_timer = 900  # 900 frames /60 = 15 seconds
# input_type = None
# level = 1

SCREEN.blit(BACKGROUND, (0, 0))

running = True

while running:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False    

        if event.type == pygame.KEYDOWN:
        # handle_key_press(event.key)

            if game_state == "game" or game_state == "game_over":
                print(f"key pressed: {event.key}")

                if event.key == 13 or event.key == 27:  # 13: 'enter', 27: 'esc'
                        game_state = "menu"
                        print(f"event key: {event.key}, game state:{game_state} ")
                        SCREEN.blit(BACKGROUND, (0, 0))        

    if game_state == "menu":
        game_state, music_state = menu(event, game_state, music_state)
        # draw_music_button(music_state)

    elif game_state == "game":

        game_state, frame_countdown, score, player_lives, objects, frozen, frozen_timer = play_game(event, difficulty, frame_countdown, score, player_lives, objects, frozen, frozen_timer)
    
    elif game_state == "game_over":
        SCREEN.blit(BACKGROUND, (0, 0))
        draw_text("GAME OVER", FONT_HEADER, WHITE, 0.5 * WIDTH, 0.5 * HEIGHT)
        draw_text(f"Score: {score}", FONT_SMALL, WHITE, 0.5 * WIDTH, 0.5 * HEIGHT + 50)
        draw_text("Entrer Esc pour retourner au menu", FONT_SMALL, WHITE, 0.5 * WIDTH, 0.5 * HEIGHT + 80)
        score = 0
        player_lives = 3
        objects = []
    
    pygame.display.flip()
    clock.tick(60) 
        
pygame.quit()
pygame.font.quit()

if __name__ == "__main__":  # The program will be run only if executed directly, not if it is called by another program.
    main()
