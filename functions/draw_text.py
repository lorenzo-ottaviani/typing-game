from .init_pygame import *

# draw text
def draw_text(text, FONT, WHITE, x, y):
    """

    :param text:
    :param FONT:
    :param WHITE:
    :param x:
    :param y:
    :return:
    """
    image = FONT.render(text, True, WHITE)
    rect = image.get_rect()
    rect.center = (x, y)
    SCREEN.blit(image, rect)