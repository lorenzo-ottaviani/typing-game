import pygame
from pygame.locals import *
from .CONFIGS import *


class App:
    """Create a single-window app with multiple scenes."""

    def __init__(self):
        """Initialize pygame and the application."""
        pygame.init()
        # flags = RESIZABLE
        App.screen = pygame.display.set_mode(SCREEN_SIZE)

        background = pygame.transform.scale(pygame.image.load(BACKGROUND_IMAGE), SCREEN_SIZE)
        App.background = App.screen.blit(background, (0, 0))

        App.running = True

    def run(self):
        """Run the main event loop."""
        while App.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    App.running = False
            pygame.display.update()
        pygame.quit()
