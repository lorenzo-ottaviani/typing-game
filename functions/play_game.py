from .init_pygame import *
from .handle_key_press import handle_key_press

# Game variables 
score = 0 
lives = 3
objects = []
frozen = False
frozen_timer = 900  # 900 frames /60 = 15
input_type = None
# level = 1

def play_game(event):
    # print("play game")

    # for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
            # handle_key_press(event.key)
            print("key pressed")