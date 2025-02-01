# Import init_pygame (configs & pygame configs file)
from .init_pygame import *

# Import functions
from .draw_text import draw_text


def choose_language(event, language):
    """
    Function to change the game language.
    :param event: The variable of the pygame event loop.
    :param language: The language chose by the user.
    :return: The new difficulty set by the user.
    """
    # Add button
    language_button_image = pygame.image.load("assets/images/buttons/language_button.png")
    language_button = pygame.transform.scale(language_button_image, (200, 90)).convert_alpha()
    language_button_rect = language_button.get_rect()
    language_button_rect.topleft = (890, 220)
    SCREEN.blit(language_button, language_button_rect)

    draw_text(f"{language}", FONT_SUB_HEADER, WHITE, 990, 290)

    # Check mouse position
    x, y = pygame.mouse.get_pos()

    if language_button_rect.collidepoint(x, y):

        if event.type == pygame.MOUSEBUTTONDOWN:
            if language == "English":
                language = "Français"
            # elif difficulty == "hard":
            #     difficulty = "easy"
            # elif difficulty == "easy":
            #     difficulty = "medium"

    return language