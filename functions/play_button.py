from .init_pygame import *
from .play_game import play_game

def play_button(event, game_state = "menu"):
    # Add button
    play_button_image = pygame.image.load("assets/images/buttons/play_button.png")
    play_button = pygame.transform.scale(play_button_image, (120, 165)).convert_alpha()
    play_button_rect = play_button.get_rect()
    play_button_rect.topleft = (260, 380)
    SCREEN.blit(play_button, play_button_rect)

    # Check mouse position
    x, y = pygame.mouse.get_pos()

    if  play_button_rect.collidepoint(x, y):
        play_button = pygame.transform.scale(play_button_image, (120 * 1.1, 165 * 1.1)).convert_alpha()
        play_button_rect = play_button.get_rect()
        play_button_rect.topleft = (255, 375)
        SCREEN.blit(play_button, play_button_rect)
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            game_state = "game"
            SCREEN.blit(BACKGROUND, (0, 0))
    return game_state