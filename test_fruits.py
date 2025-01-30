import pygame
from random import uniform

from functions.CONFIGS import *

apple = pygame.image.load("assets/images/fruits/apple.png")
pear = pygame.image.load("assets/images/fruits/pear.png")
# apple = pygame.transform.scale(apple, (90, 90))

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)

clock = pygame.time.Clock()

x_min = 6/14 * SCREEN_WIDTH
x_max = 8/14 * SCREEN_WIDTH


def generate_object():
    """"""
    objet = {"type": "random(object_types)", "x": uniform(x_min, x_max), "y": SCREEN_HEIGHT,
             "speed_x": uniform(-7, 7), "speed_y": uniform(-17, -15), "apple": apple, "pear": pear}
    game_elements = {"x": objet["x"], "y": objet["y"], "speed_x": objet["speed_x"], "speed_y": objet["speed_y"]}
    return game_elements


# objet = {"type": "random(object_types)", "x": uniform(x_min, x_max), "y": SCREEN_HEIGHT, "speed_x": uniform(-7, 7),
#          "speed_y": uniform(-17, -15), "apple": apple, "pear": pear}

fructificator = []
for n in range(4):
    fructificator.append(generate_object())

# x_apple = uniform(x_min, x_max)
#
# x_pear = uniform(x_min, x_max)
#
# y_apple = SCREEN_HEIGHT
# y_pear = SCREEN_HEIGHT
#
# speed_x_apple = uniform(-7, 7)
# speed_y_apple = uniform(-17, -15)
#
# speed_x_pear = uniform(-7, 7)
# speed_y_pear = uniform(-17, -15)

t0 = pygame.time.get_ticks()  # Initial time

# x_apple = objet["x"] + objet["speed_x"]
# y_apple = objet["y"]

# x_pear = objet["x"] + objet["speed_x"]
# y_pear = objet["y"]

x_apple = fructificator[0]["x"] + fructificator[0]["speed_x"]
y_apple = fructificator[0]["y"]

x_pear = fructificator[1]["x"] + fructificator[1]["speed_x"]
y_pear = fructificator[1]["y"]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # t = t0  # Reset time at the beginning of object movement.

    t = (pygame.time.get_ticks() - t0) / 400  # Count the time during movement.

    # x_apple += speed_x_apple
    # y_apple += speed_y_apple * t + 5 * t**2
    #
    # x_pear += speed_x_pear
    # y_pear += speed_y_pear * t + 5 * t ** 2

    x_apple += fructificator[0]["speed_x"]
    y_apple += fructificator[0]["speed_y"] * t + 5 * t ** 2

    x_pear += fructificator[1]["speed_x"]
    y_pear += fructificator[1]["speed_y"] * t + 5 * t ** 2

    screen.fill((0, 0, 0))  # Cancel old place of image during movement.
    screen.blit(apple, (x_apple, y_apple))
    screen.blit(pear, (x_pear, y_pear))
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
