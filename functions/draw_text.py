from .init_pygame import *

# draw text
def draw_text(text, FONT, WHITE, x, y):
    image = FONT.render(text, True, WHITE)
    SCREEN.blit(image, (x, y))