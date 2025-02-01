# Import init_pygame (configs & pygame configs file)
from .init_pygame import *

# Import functions
from .draw_text import draw_text
from .play_button import play_button
from .quit_button import quit_button
from .choose_difficulty import choose_difficulty
from .play_music import play_music, draw_music_button


def menu(event, game_state, music_state, difficulty, language):
    """
    The menu function.
    :param event: The variable of the pygame event loop.
    :param game_state: The game state ("menu", "game" or "game_over").
    :param music_state: The music state (set "on" or "off").
    :param difficulty: The game difficulty chosen.
    :param language: The language chose by the user.
    :return: Menu actions.
    """
    # Add images behind background
    SCREEN.blit(APPLE, (100, 50))
    SCREEN.blit(BANANA, (350, 590))
    SCREEN.blit(BOMB, (1220, 70))
    SCREEN.blit(CHERRY, (1000, 50))
    SCREEN.blit(ICE_CUBE, (80, 550))
    SCREEN.blit(MANGO_TOP, (180, 250))
    SCREEN.blit(MANGO_BOTTOM, (120, 350))
    SCREEN.blit(PEAR, (900, 550))
    SCREEN.blit(STRAWBERRY_TOP, (1170, 350))
    SCREEN.blit(STRAWBERRY_BOTTOM, (1200, 450))

    # Add a menu background
    menu_background = pygame.Surface((1000, 600), pygame.SRCALPHA)
    # menu_background.set_alpha(40)
    menu_background.fill((255, 255, 255, 20))
    SCREEN.blit(menu_background, (200, 185 / 2))

    # Add game logo
    logo_image = pygame.image.load("assets/images/Logo.png").convert_alpha()
    logo = pygame.transform.scale(logo_image, (700, 250))
    logo_rect = logo.get_rect()
    logo_rect.center = (730, 220)
    SCREEN.blit(logo, logo_rect)

    # Add explanation text to explain how to play
    if language == "English":
        # Language English
        draw_text("How to play Fruit Ninja Slicer ?", FONT_SUB_HEADER, ORANGE, 700, 380)
        draw_text("Click on the 'Play' button", FONT, ORANGE, 700, 440)
        draw_text("Some fruits will appear, tied with a letter", FONT, ORANGE, 700, 480)
        draw_text("You must type the corresponding key", FONT, ORANGE, 700, 520)
        draw_text("The ice cubes give a 5 second 'frozen' time bonus", FONT, ORANGE, 700, 560)
        draw_text("Careful !!! do not slice the bombs !!!", FONT, ORANGE, 700, 600)

    elif language == "French":
        # Language French
        draw_text("Comment jouer à Fruit Ninja Slicer ?", FONT_SUB_HEADER, ORANGE, 700, 380)
        draw_text("Cliquer sur le bouton jouer", FONT, ORANGE, 700, 440)
        draw_text("Des fruits vont apparaitre avec une lettre", FONT, ORANGE, 700, 480)
        draw_text("Vous devez taper la touche correspondante", FONT, ORANGE, 700, 520)
        draw_text("Les glaçons vous donnent un bonus de temps de 5 secondes", FONT, ORANGE, 700, 560)
        draw_text("Attention !!! Ne pas couper les bombes !!!", FONT, ORANGE, 700, 600)

    # Call quit_button
    quit_button(event)

    # Call play_button
    game_state = play_button(event)

    # Call difficulty_button
    difficulty = choose_difficulty(event, difficulty)

    # Call the music button
    music_state = play_music(event, music_state)
    draw_music_button(music_state)

    return game_state, music_state, difficulty
