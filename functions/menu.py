from .init_pygame import *
from .draw_text import draw_text
from .play_button import play_button
from .quit_button import quit_button

def menu(event, game_state, running):
    
    # Add images behind background
    SCREEN.blit(APPLE, (100, 50))
    SCREEN.blit(BANANA, (350, 590))
    SCREEN.blit(BOMB, (1220, 70))
    SCREEN.blit(CHERRY, (1000, 50))
    SCREEN.blit(ICE_CUBE, (80, 550))
    SCREEN.blit(MANGO_TOP, (180, 250))
    SCREEN.blit(MANGO_BOTTOM, (120, 350))
    SCREEN.blit(PEAR, (900, 550))
    SCREEN.blit(STRAWBERRY_TOP, (1170, 350))
    SCREEN.blit(STRAWBERRY_BOTTOM, (1200, 450))
    
    # Add a menu background
    menu_background = pygame.Surface((1000, 600), pygame.SRCALPHA)
    # menu_background.set_alpha(40)
    menu_background.fill((255,255,255,20))
    SCREEN.blit(menu_background, (200, 185/2))
    
    # Add game logo
    logo_image = pygame.image.load("assets/images/Logo.png").convert_alpha()
    logo = pygame.transform.scale(logo_image, (700, 250))
    logo_rect = logo.get_rect()
    logo_rect.center = (730, 220)
    SCREEN.blit(logo, logo_rect)
    
    # Add explanation text to explain how to play
    draw_text("Comment jouer à Fruit Ninja Slicer ?", FONT_SUB_HEADER, ORANGE, 700, 380)
    draw_text("Cliquer sur le bouton jouer", FONT, ORANGE, 700, 440)
    draw_text("Des fruits vont apparaitre avec une lettre", FONT, ORANGE, 700, 480)
    draw_text("Vous devez taper la touche correspondante", FONT, ORANGE, 700, 520)
    draw_text("Les glaçons vous donnent un bonus de temps de 5 secondes", FONT, ORANGE, 700, 560)
    draw_text("Attention !!! Ne pas couper les bombes !!!", FONT, ORANGE, 700, 600)
    
    # Call play_button
    game_state = play_button(event)
    
    # Call play_button
    running = quit_button(event)
    
    print(game_state, running)
    return game_state, running