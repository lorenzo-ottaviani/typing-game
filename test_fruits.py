import pygame
from random import uniform, choice

from functions.CONFIGS import *

# apple = pygame.image.load("assets/images/fruits/apple.png")
# pear = pygame.image.load("assets/images/fruits/pear.png")
# apple = pygame.transform.scale(apple, (90, 90))

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)

clock = pygame.time.Clock()

x_min = 6/14 * SCREEN_WIDTH
x_max = 8/14 * SCREEN_WIDTH


def generate_object():
    """"""
    objet = {"type": choice(object_type), "x": uniform(x_min, x_max), "y": SCREEN_HEIGHT,
             "speed_x": uniform(-7, 7), "speed_y": uniform(-17, -15), "apple": "apple", "pear": "pear"}
    game_elements = {"type": objet["type"], "x": objet["x"], "y": objet["y"], "speed_x": objet["speed_x"],
                     "speed_y": objet["speed_y"]}
    return game_elements


# objet = {"type": "random(object_types)", "x": uniform(x_min, x_max), "y": SCREEN_HEIGHT, "speed_x": uniform(-7, 7),
#          "speed_y": uniform(-17, -15), "apple": apple, "pear": pear}

fructificator = []
for k in range(4):
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

for n in range(4):
    exec(f"x{n + 1} = {fructificator[n]["x"] + fructificator[n]["speed_x"]}")
    exec(f"y{n + 1} = {fructificator[n]["y"]}")

    # x1 = fructificator[0]["x"] + fructificator[0]["speed_x"]
    # y1 = fructificator[0]["y"]
    #
    # x2 = fructificator[1]["x"] + fructificator[1]["speed_x"]
    # y2 = fructificator[1]["y"]
    #
    # x3 = fructificator[2]["x"] + fructificator[2]["speed_x"]
    # y3 = fructificator[2]["y"]
    #
    # x4 = fructificator[3]["x"] + fructificator[3]["speed_x"]
    # y4 = fructificator[3]["y"]

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

    # x1 += fructificator[0]["speed_x"]
    # y1 += fructificator[0]["speed_y"] * t + 5 * t ** 2
    #
    # x2 += fructificator[1]["speed_x"]
    # y2 += fructificator[1]["speed_y"] * t + 5 * t ** 2
    #
    # x3 += fructificator[2]["speed_x"]
    # y3 += fructificator[2]["speed_y"] * t + 5 * t ** 2
    #
    # x4 += fructificator[3]["speed_x"]
    # y4 += fructificator[3]["speed_y"] * t + 5 * t ** 2

    screen.fill((0, 0, 0))  # Cancel old place of image during movement.

    x_values = [x1, x2, x3, x4]
    y_values = [y1, y2, y3, y4]

    for i in range(4):
        x_values[i] += fructificator[i]["speed_x"]
        y_values[i] += fructificator[i]["speed_y"] * t + 5 * t ** 2

    x1, x2, x3, x4 = x_values
    y1, y2, y3, y4 = y_values

    for j in range(4):
        screen.blit(fructificator[j]["type"], (x_values[j], y_values[j]))

    # screen.blit(fructificator[0]["type"], (x1, y1))
    # screen.blit(fructificator[1]["type"], (x2, y2))
    # screen.blit(fructificator[2]["type"], (x3, y3))
    # screen.blit(fructificator[3]["type"], (x4, y4))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
