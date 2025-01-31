from .init_pygame import *
from pygame import mixer

# Initialize music
mixer.init()
mixer.music.load('assets/music/bensound-summer_ogg_music.ogg')
mixer.music.play(-1)  # La musique démarre et tourne en boucle

play_music_icon = pygame.image.load("assets/images/play_music.png")
play_music_icon = pygame.transform.scale(play_music_icon, (60, 82)).convert_alpha()

stop_music_icon = pygame.image.load("assets/images/stop_music.png")
stop_music_icon = pygame.transform.scale(stop_music_icon, (60, 82)).convert_alpha()

music_button_rect = play_music_icon.get_rect(topleft=(260, 580))

music_state = "on"

def play_music(event, music_state):
    """

    :param event:
    :param music_state:
    :return:
    """

    # Change music_state
    if event.type == pygame.MOUSEBUTTONDOWN:
        x, y = pygame.mouse.get_pos()
        if music_button_rect.collidepoint(x, y):
            if music_state == "on":
                music_state = "off"
                mixer.music.stop()
                SCREEN.blit(stop_music_icon, music_button_rect)
            else:
                music_state = "on"
                mixer.music.play(-1)
                SCREEN.blit(play_music_icon, music_button_rect)
    return music_state    

def draw_music_button(music_state):
    """Affiche l'icône correspondante au statut de la musique."""
    if music_state == "on":
        SCREEN.blit(play_music_icon, music_button_rect)
    else:
        SCREEN.blit(stop_music_icon, music_button_rect)
