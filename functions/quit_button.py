from .init_pygame import *

def quit_button(event, running = True):
    # Add button
    quit_button_image = pygame.image.load("assets/images/buttons/quit_button.png")
    quit_button = pygame.transform.scale(quit_button_image, (120, 165)).convert_alpha()
    quit_button_rect = quit_button.get_rect()
    quit_button_rect.topleft = (1050, 380)
    SCREEN.blit(quit_button, quit_button_rect)

    # Check mouse position
    mouse = pygame.mouse.get_pos()

    if (quit_button_rect[0]/2 + 700 <= mouse[0] <= quit_button_rect[1]/2 + WIDTH * 820 and quit_button_rect[0]/2 + 250 <= mouse[1]
                <= quit_button_rect[1]/2 + 415):
        quit_button = pygame.transform.scale(quit_button_image, (120 * 1.1, 165 * 1.1)).convert_alpha()
        quit_button_rect = quit_button.get_rect()
        quit_button_rect.topleft = (255, 375)
        SCREEN.blit(quit_button, quit_button_rect)
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            running = False
            SCREEN.blit(BACKGROUND, (0, 0))
    return running