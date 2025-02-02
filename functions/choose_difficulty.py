# Import init_pygame (configs & pygame configs file)
from .init_pygame import *

# Import functions
from .draw_text import draw_text


def choose_difficulty(event, difficulty, language):
    """
    Function to change the game difficulty.
    :param event: The variable of the pygame event loop.
    :param difficulty: The game difficulty chosen.
    :param language: The language chose by the user.
    :return: The new difficulty set by the user.
    """
    # Add button
    if language == "English":
        difficulty_button_image = pygame.image.load("assets/images/buttons/difficulty_button.png")
    elif language == "Français":
        difficulty_button_image = pygame.image.load("assets/images/buttons/niveau_button.png")

    difficulty_button = pygame.transform.scale(difficulty_button_image, (200, 90)).convert_alpha()
    difficulty_button_rect = difficulty_button.get_rect()
    difficulty_button_rect.topleft = (990, 300)
    SCREEN.blit(difficulty_button, difficulty_button_rect)

    draw_text(f"{difficulty}", FONT_SUB_HEADER, WHITE, 1090, 370)

    # Check mouse position
    x, y = pygame.mouse.get_pos()

    if difficulty_button_rect.collidepoint(x, y):

        if event.type == pygame.MOUSEBUTTONDOWN:
            if difficulty == "medium":
                difficulty = "hard"
            elif difficulty == "hard":
                difficulty = "easy"
            elif difficulty == "easy":
                difficulty = "medium"

    return difficulty
