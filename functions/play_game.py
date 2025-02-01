from .init_pygame import *
# from .handle_key_press import handle_key_press
from .draw_text import draw_text
from .generate_object import generate_object
import time



def play_game(difficulty, frame_countdown, score, combo_text, player_lives, objects, frozen, frozen_timer, game_state):
    """

    :param event:
    :param difficulty:
    :param frame_countdown:
    :param score:
    :param player_lives:
    :param objects:
    :param frozen:
    :param frozen_timer:
    :param game_state:
    :return:
    """
    # pygame.event.set_blocked(pygame.MOUSEMOTION)
    # print("play game")
    draw_text(f"Lives: {player_lives}", FONT, WHITE, 0.1 * WIDTH, 0.1 * HEIGHT)
    draw_text(f"Score: {score}", FONT, WHITE, 0.2 * WIDTH, 0.1 * HEIGHT)

    if frame_countdown > 0:
        frame_countdown -= 1

    if frame_countdown == 0:
        if frozen == False:
            objects.append(generate_object())
        # print(f"objects post append: {objects}")
            if difficulty == "medium":
                frame_countdown = 45
            elif difficulty == "easy":
                frame_countdown = 60
            elif difficulty == "hard":
                frame_countdown = 30

    if frozen == False:
        if objects != None:
            for obj in objects:
                obj["x"] += obj["speed_x"]
                obj["y"] += obj["speed_y"] * obj["time"] + 5 * obj["time"] ** 2
            
    if frozen == True:
        frozen_timer = frozen_timer - 1
        if frozen_timer == 0:
            frozen = False
            frozen_timer = 300

    SCREEN.blit(BACKGROUND, (0, 0))
    draw_text(f"Lives: {player_lives}", FONT, WHITE, 0.1 * WIDTH, 0.1 * HEIGHT)
    draw_text(f"Score: {score}", FONT, WHITE, 0.2 * WIDTH, 0.1 * HEIGHT)
    if combo_text[1] > 0:
        draw_text(f"Combo X{combo_text[1]}!", FONT, WHITE, 0.45 * WIDTH, 0.4 * HEIGHT)
        combo_text[1] -= 1

    for obj in objects:
        SCREEN.blit(obj["img"], (obj["x"], obj["y"]))
        draw_text(obj["letter"], FONT_LETTER, WHITE,  obj["x"], obj["y"])

        if frozen == False:
            obj["time"] += 0.04
            # else:
            #     frozen_timer = frozen_timer - 1
            #     if frozen_timer == 0:
            #         frozen = False

    if objects != None:
        for obj in objects:
            if obj["y"] > HEIGHT:
                player_lives -= 1  # Deduct life once
                objects.remove(obj)
                
    if player_lives <= 0:
        game_state = "game_over"
            
    return frame_countdown, score, combo_text, player_lives, objects, frozen, frozen_timer, game_state