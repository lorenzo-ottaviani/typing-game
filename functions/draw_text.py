from .init_pygame import *

# draw text
def draw_text(text, FONT, WHITE, x, y):
    image = FONT.render(text, True, WHITE)
    rect = image.get_rect()
    rect.center = (x, y)
    SCREEN.blit(image, rect)