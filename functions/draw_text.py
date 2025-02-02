# Import init_pygame (configs & pygame configs file)
from .init_pygame import *


def draw_text(text, FONT, WHITE, x, y):
    """
    Function used to draw a text into the screen.
    :param text: The text to draw.
    :param FONT: Text font.
    :param WHITE: Text colour.
    :param x: Horizontal text position.
    :param y: Vertical text position.
    :return: ∅
    """
    image = FONT.render(text, True, WHITE)
    rect = image.get_rect()
    rect.center = (x, y)
    SCREEN.blit(image, rect)
