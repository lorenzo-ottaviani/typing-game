from functions.init_pygame import *
import random
from random import uniform
from functions.draw_text import draw_text

frame_countdown = 45
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
        "time": 0,
        # "hit": False,
    }
    return object_data

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if frame_countdown > 0:
        frame_countdown -= 1

    else:
        objects.append(generate_object())
        # print(f"objects post append: {objects}")
        frame_countdown = 45

    if objects != None:
        for obj in objects:
            obj["x"] += obj["speed_x"]
            obj["y"] += obj["speed_y"] * obj["time"] + 5 * obj["time"] ** 2

        SCREEN.fill((0, 0, 0))  # Cancel old place of image during movement.

        for obj in objects:
            SCREEN.blit(obj["img"], (obj["x"], obj["y"]))
            draw_text(obj["letter"], FONT_LETTER, WHITE,  obj["x"], obj["y"])
            obj["time"] += 0.04

    pygame.display.flip()
    clock.tick(60)

pygame.quit()