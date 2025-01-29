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

def draw_lives(display, x, y, player_lives, image) :
    for i in range(player_lives) :
        img = pygame.image.load(image)
        img_rect = img.get_rect()       #gets the (x,y) coordinates of the cross icons (lives on the the top rightmost side)
        img_rect.x = int(x + 35 * i)    #sets the next cross icon 35pixels awt from the previous one
        img_rect.y = y                  #takes care of how many pixels the cross icon should be positioned from top of the screen
        display.blit(img, img_rect)

def play_game(event):
    # print("play game")
    draw_text(f"Lives: {player_lives}", FONT, WHITE, 0.1 * WIDTH, 0.1 * HEIGHT)
    draw_text(f"Score: {score}", FONT, WHITE, 0.2 * WIDTH, 0.1 * HEIGHT)

    # for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
            # handle_key_press(event.key)
            print("key pressed")