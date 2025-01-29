from .init_pygame import *
from .handle_key_press import handle_key_press
from .draw_text import draw_text

# Game variables 
score = 0 
player_lives = 3
objects = []

frozen = False
frozen_timer = 900  # 900 frames /60 = 15
input_type = None
# level = 1

def play_game(event, game_state = "game"):
    # print("play game")
    draw_text(f"Lives: {player_lives}", FONT, WHITE, 0.1 * WIDTH, 0.1 * HEIGHT)
    draw_text(f"Score: {score}", FONT, WHITE, 0.2 * WIDTH, 0.1 * HEIGHT)

    # for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
            # handle_key_press(event.key)
            print(f"key pressed: {event.key}")

            if event.key == 13 or event.key == 27:  # 13: 'enter', 27: 'esc'
                  game_state = "menu"
                  print(f"event key: {event.key}, game state:{game_state} ")
                  SCREEN.blit(BACKGROUND, (0, 0))
    return game_state