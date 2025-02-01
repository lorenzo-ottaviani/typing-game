"""
Authors : Lorenzo OTTAVIANI, Olivier PORTAL et Thibault CARON.
Date : 01/02/2025 11h05
Aim of the program :
    Execute a typing fruit game with PyGame.
Inputs : Letters input from the keyboard to play the game.
Output : Fruit Ninja Slicer using the graphical interface PyGame.
"""
# Import init_pygame (configs & pygame configs file)
from functions.init_pygame import *

# Import functions
from functions.menu import menu
from functions.play_game import play_game
from functions.draw_text import draw_text


def main():
    """
    Main function of the fruit slicer.
    :return: ∅
    """
    # Initialise program data
    game_state = "menu"
    music_state = "on"
    difficulty = "medium"
    language = "English"
    frame_countdown = 10  # Speed of appearance of objects on screen: change with the difficulty.
    score = 0
    combo = 0
    combo_text = (0, 0)
    player_lives = 3
    objects = []  # A list of all the objects to display in the screen.
    frozen = False
    frozen_timer = 300  # 300 frames /60 = 5 seconds

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
                        SCREEN.blit(BACKGROUND, (0, 0))

                if game_state == "game":
                    try:
                        key_char = event.unicode.upper()
                    except ValueError:
                        print("not a letter")

                    for element in objects:
                        if key_char == element["letter"] and element["type"] == "bomb":
                            player_lives = 0
                            objects.remove(element)
                        elif key_char == element["letter"] and element["type"] == "ice_cube":
                            frozen = True
                            objects.remove(element)
                        elif (key_char == element["letter"] and element["type"] != "bomb"
                              and element["type"] != "ice_cube"):
                            combo += 1
                            objects.remove(element)
                    if combo == 1:
                        score += 1
                    elif combo > 1:
                        score += combo * 3 - 2
                        combo_text = (combo, 30)
                    combo = 0

        if game_state == "menu":
            game_state, music_state, difficulty = menu(event, game_state, music_state, difficulty, language)

        elif game_state == "game":
            (frame_countdown, score, combo_text, player_lives, objects, frozen, frozen_timer, game_state) = (
                play_game(difficulty, frame_countdown, score, combo_text, player_lives, objects, frozen, frozen_timer,
                          game_state))

        elif game_state == "game_over":
            SCREEN.blit(BACKGROUND, (0, 0))
            draw_text("GAME OVER", FONT_HEADER, WHITE, 0.5 * WIDTH, 0.5 * HEIGHT)
            draw_text(f"Score: {score}", FONT_SMALL, WHITE, 0.5 * WIDTH, 0.5 * HEIGHT + 50)
            draw_text("Entrer Esc pour retourner au menu", FONT_SMALL, WHITE, 0.5 * WIDTH, 0.5 * HEIGHT + 80)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    pygame.font.quit()


if __name__ == "__main__":  # The program will be run only if executed directly, not if it is called by another program.
    main()
