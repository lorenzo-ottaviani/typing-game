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
    mouse = pygame.mouse.get_pos()

    if (play_button_rect[0]/2 + 100 <= mouse[0] <= play_button_rect[1]/2 + 220 and play_button_rect[0]/2 + 250 <= mouse[1]
                <= play_button_rect[1]/2 + 415):
        play_button = pygame.transform.scale(play_button_image, (120 * 1.1, 165 * 1.1)).convert_alpha()
        play_button_rect = play_button.get_rect()
        play_button_rect.topleft = (255, 375)
        SCREEN.blit(play_button, play_button_rect)
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            game_state = "game"
            print(game_state)
            SCREEN.blit(BACKGROUND, (0, 0))
    return game_state