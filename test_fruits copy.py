from functions.init_pygame import *
import random
from random import uniform
from functions.draw_text import draw_text

x_min = 6/14 * WIDTH
x_max = 8/14 * WIDTH
frame_countdown = 60
objects = []

def generate_object():
    """"""
    object_data = {
        "img": random.choice(object_type),
        "letter": random.choice(OBJECT_LETTERS),
        "x" : uniform(x_min, x_max),  # where the object should be positioned on x-coordinate
        "y" : HEIGHT,
        "speed_x": uniform(-7, 7),  # how fast the object should move in x direction. Controls the diagonal movement of objects
        "speed_y": uniform(-17, -15),  # control the speed of objects in y-direction ( UP )     
        # "hit": False,
    }
    return object_data

t0 = pygame.time.get_ticks()  # Initial time


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    t = (pygame.time.get_ticks() - t0) / 1000  # Count the time during movement.

    if frame_countdown > 0:
        frame_countdown -= 1

    else:
        objects.append(generate_object())
        # print(f"objects post append: {objects}")
        frame_countdown = 60
        # t = t0

    print(f"t: {t}")
    print(f"t0: {t0}")
    tt = 0.2

    if objects != None:
        for obj in objects:
            obj["x"] += obj["speed_x"]
            obj["y"] += obj["speed_y"] * t + 5 * t ** 2
            # obj["y"] += obj["speed_y"] * tt

        # print(f"objects maj: {objects}")

        # t = t0  # Reset time at the beginning of object movement.

        SCREEN.fill((0, 0, 0))  # Cancel old place of image during movement.

        for obj in objects:
            SCREEN.blit(obj["img"], (obj["x"], obj["y"]))
            draw_text(obj["letter"], FONT_LETTER, WHITE,  obj["x"], obj["y"])

    
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
