import pygame
from random import uniform, choice

from functions.CONFIGS import *

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)

clock = pygame.time.Clock()

x_min = 6/14 * SCREEN_WIDTH
x_max = 8/14 * SCREEN_WIDTH


def generate_object():
    """"""
    objet = {"type": choice(object_type), "x": uniform(x_min, x_max), "y": SCREEN_HEIGHT,
             "speed_x": uniform(-7, 7), "speed_y": uniform(-17, -15), "time": 0}
    return objet


fructificator = [generate_object() for _ in range(4)]

x_values = [obj["x"] for obj in fructificator]
y_values = [obj["y"] for obj in fructificator]

running = True 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # Clear the screen

    for i in range(4):
        x_values[i] += fructificator[i]["speed_x"]
        y_values[i] += fructificator[i]["speed_y"] * fructificator[i]["time"] + 5 * fructificator[i]["time"] ** 2
        screen.blit(fructificator[i]["type"], (x_values[i], y_values[i]))
        fructificator[i]["time"] += 0.04  # Time increment

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
