from .init_pygame import *
# from .handle_key_press import handle_key_press
from .draw_text import draw_text
from .generate_object import generate_object


def play_game(event, difficulty, frame_countdown, score, player_lives, objects, frozen, frozen_timer, game_state = "game"):
    ''''''
    # pygame.event.set_blocked(pygame.MOUSEMOTION)
    # print("play game")
    draw_text(f"Lives: {player_lives}", FONT, WHITE, 0.1 * WIDTH, 0.1 * HEIGHT)
    draw_text(f"Score: {score}", FONT, WHITE, 0.2 * WIDTH, 0.1 * HEIGHT)

    if frame_countdown > 0:
        frame_countdown -= 1

    else:
        objects.append(generate_object())
        # print(f"objects post append: {objects}")
        if difficulty == "medium":
            frame_countdown = 45
        elif difficulty == "easy":
            frame_countdown = 60
        elif difficulty == "hard":
            frame_countdown = 30

    if objects != None:
        for obj in objects:
            obj["x"] += obj["speed_x"]
            obj["y"] += obj["speed_y"] * obj["time"] + 5 * obj["time"] ** 2

        SCREEN.blit(BACKGROUND, (0, 0))
        draw_text(f"Lives: {player_lives}", FONT, WHITE, 0.1 * WIDTH, 0.1 * HEIGHT)
        draw_text(f"Score: {score}", FONT, WHITE, 0.2 * WIDTH, 0.1 * HEIGHT)

        for obj in objects:
            SCREEN.blit(obj["img"], (obj["x"], obj["y"]))
            draw_text(obj["letter"], FONT_LETTER, WHITE,  obj["x"], obj["y"])
            obj["time"] += 0.04

    # for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
            # handle_key_press(event.key)
            print(f"key pressed: {event.key}")

            if event.key == 13 or event.key == 27:  # 13: 'enter', 27: 'esc'
                  game_state = "menu"
                  print(f"event key: {event.key}, game state:{game_state} ")
                  SCREEN.blit(BACKGROUND, (0, 0))
    return game_state, frame_countdown, score, player_lives, objects, frozen, frozen_timer