# Import init_pygame (configs & pygame configs file)
from .init_pygame import *

# Import functions
from .draw_text import draw_text
from .generate_object import generate_object


def play_game(difficulty, frame_countdown, score, combo_text, player_lives, objects, frozen, frozen_timer, game_state,
              language):
    """
    The game function.
    :param difficulty: The game difficulty chosen.
    :param frame_countdown: The speed of appearance of objects on screen: change with the difficulty.
    :param score: The game score.
    :param combo_text: Variable used to now if the player as done a combo.
    :param player_lives: Number o live of the player.
    :param objects: A list of all the objects to display in the screen.
    :param frozen: Freeze the game when "True".
    :param frozen_timer: The duration of a game freeze.
    :param game_state: The game state ("menu", "game" or "game_over").
    :param language: The language chose by the user.
    :return: Game actions.
    """
    if language == "English":
        draw_text(f"Lives: {player_lives}", FONT, WHITE, 0.1 * WIDTH, 0.1 * HEIGHT)
    elif language == "Français":
        draw_text(f"Vies: {player_lives}", FONT, WHITE, 0.1 * WIDTH, 0.1 * HEIGHT)

    draw_text(f"Score: {score}", FONT, WHITE, 0.2 * WIDTH, 0.1 * HEIGHT)

    if frame_countdown > 0:
        frame_countdown -= 1

    if frame_countdown == 0:
        if not frozen:
            objects.append(generate_object())
            if difficulty == "medium":
                frame_countdown = 45
            elif difficulty == "easy":
                frame_countdown = 60
            elif difficulty == "hard":
                frame_countdown = 30

    if not frozen:
        if objects is not None:
            for element in objects:
                element["x"] += element["speed_x"]
                element["y"] += element["speed_y"] * element["time"] + 5 * element["time"] ** 2

    if frozen:
        frozen_timer = frozen_timer - 1
        if frozen_timer == 0:
            frozen = False
            frozen_timer = 300

    SCREEN.blit(BACKGROUND, (0, 0))

    if language == "English":
        draw_text(f"Lives: {player_lives}", FONT, WHITE, 0.1 * WIDTH, 0.1 * HEIGHT)
    elif language == "Français":
        draw_text(f"Vies: {player_lives}", FONT, WHITE, 0.1 * WIDTH, 0.1 * HEIGHT)

    draw_text(f"Score: {score}", FONT, WHITE, 0.2 * WIDTH, 0.1 * HEIGHT)

    if combo_text[1] > 0:
        draw_text(f"Combo X{combo_text[0]}!", FONT, WHITE, 0.45 * WIDTH, 0.4 * HEIGHT)
        combo_text[1] = combo_text[1] - 1

    for element in objects:
        SCREEN.blit(element["img"], (element["x"], element["y"]))
        draw_text(element["letter"], FONT_LETTER, WHITE, element["x"], element["y"])

        if not frozen:
            element["time"] += 0.04

    if objects is not None:
        for element in objects:
            if element["y"] > HEIGHT:
                objects.remove(element)
                if element["type"] != "bomb":
                    player_lives -= 1  # Deduct life once

    if player_lives <= 0:
        game_state = "game_over"

    return frame_countdown, score, combo_text, player_lives, objects, frozen, frozen_timer, game_state, language
