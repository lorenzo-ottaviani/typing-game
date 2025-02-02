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
    
    # Add french button
    french_button_image = pygame.image.load("assets/images/buttons/french_button.png")
    french_button = pygame.transform.scale(french_button_image, (200, 90)).convert_alpha()
    french_button_rect = french_button.get_rect()
    french_button_rect.topleft = (890, 220)
    
    niveau_button_image = pygame.image.load("assets/images/buttons/niveau_button.png")
    niveau_button = pygame.transform.scale(niveau_button_image, (200, 90)).convert_alpha()
    niveau_button_rect = niveau_button.get_rect()
    niveau_button_rect.topleft = (990, 300)

    draw_text(f"{language}", FONT_SUB_HEADER, WHITE, 990, 290)

    # Check mouse position
    x, y = pygame.mouse.get_pos()

    if language_button_rect.collidepoint(x, y):

        if event.type == pygame.MOUSEBUTTONDOWN:
            if language == "English":
                language = "Français"
                SCREEN.blit(french_button, french_button_rect)
                SCREEN.blit(niveau_button, niveau_button_rect)
            elif language == "Français":
                language = "English"
                SCREEN.blit(language_button, language_button_rect)

    return language