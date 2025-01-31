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
stored_scores = []
player_lives = 13
objects = []
frozen = False
frozen_timer = 300  # 900 frames /60 = 15 seconds
# input_type = None
# level = 1

SCREEN.blit(BACKGROUND, (0, 0))

running = True

while running:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False    

        if event.type == pygame.KEYDOWN:
            if game_state == "game" or game_state == "game_over":

                if event.key == 13 or event.key == 27:  # 13: 'enter', 27: 'esc'
                    if game_state == "game_over":
                        score = 0
                        player_lives = 3
                        objects = []
                    game_state = "menu"
                    # print(f"event key: {event.key}, game state:{game_state} ")
                    SCREEN.blit(BACKGROUND, (0, 0)) 
            
            if game_state == "game":
                # handle_key_press(event.key)
                try:
                    key_char = event.unicode.upper()
                except ValueError:
                    print("not a letter")

                for object in objects: 
                    if key_char == object["letter"] and object["type"] == "bomb":
                        player_lives = 0
                        # game_state == "game_over"
                        # print(f"game state: {game_state}")
                        # print(f"object: {object}")
                        objects.remove(object)
                    elif key_char == object["letter"] and object["type"] == "ice_cube":
                        frozen = True
                        objects.remove(object)
                    elif key_char == object["letter"] and object["type"] != "bomb" and object["type"] != "ice_cube":
                        # print(f"get sliced")
                        score += 1
                        objects.remove(object)


    if game_state == "menu":
        game_state, music_state, difficulty = menu(event, game_state, music_state, difficulty)
        # draw_music_button(music_state)

    elif game_state == "game":
        frame_countdown, score, player_lives, objects, frozen, frozen_timer, game_state = play_game(difficulty, frame_countdown, score, player_lives, objects, frozen, frozen_timer, game_state)
    
    elif game_state == "game_over":
        SCREEN.blit(BACKGROUND, (0, 0))
        # stored_scores.append(score)
        draw_text("GAME OVER", FONT_HEADER, WHITE, 0.5 * WIDTH, 0.5 * HEIGHT)
        draw_text(f"Score: {score}", FONT_SMALL, WHITE, 0.5 * WIDTH, 0.5 * HEIGHT + 50)
        draw_text("Entrer Esc pour retourner au menu", FONT_SMALL, WHITE, 0.5 * WIDTH, 0.5 * HEIGHT + 80)
    
    pygame.display.flip()
    clock.tick(60) 
        
pygame.quit()
pygame.font.quit()

if __name__ == "__main__":  # The program will be run only if executed directly, not if it is called by another program.
    main()
