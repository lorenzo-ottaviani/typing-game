import pygame
from random import uniform

from functions.CONFIGS import *


def object_movement(object, t0):
    """"""

    def object_characteristics():
        """"""
        x_min = 6 / 14 * SCREEN_WIDTH
        x_max = 8 / 14 * SCREEN_WIDTH

        x = uniform(x_min, x_max)

        y = SCREEN_HEIGHT

        speed_x = uniform(-7, 7)
        speed_y = uniform(-17, -15)

        return x, y, speed_x, speed_y

    x, y, speed_x, speed_y = object_characteristics()

    t = (pygame.time.get_ticks() - t0) / 400  # Count the time during movement.
    x += speed_x
    y += speed_y * t + 5 * t ** 2

    return x, y


apple = pygame.image.load("assets/images/fruits/apple.png")
# apple = pygame.transform.scale(apple, (90, 90))

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)

clock = pygame.time.Clock()

t0 = pygame.time.get_ticks()  # Time at the beginning of object movement.

# x_min = 6/14 * SCREEN_WIDTH
# x_max = 8/14 * SCREEN_WIDTH
#
# x = uniform(x_min, x_max)
#
# y = SCREEN_HEIGHT
#
# speed_x = uniform(-7, 7)
# speed_y = uniform(-17, -15)
#
# t0 = pygame.time.get_ticks()  # initial time

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # t = t0  # Reset time at the beginning of object movement.

    t = (pygame.time.get_ticks() - t0) / 400  # Count the time during movement.

    # x += speed_x
    # y += speed_y * t + 5 * t**2
    x = object_movement(apple, t0)[0]
    y = object_movement(apple, t0)[1]
    screen.blit(apple, (x,y))
    screen.fill((0, 0, 0))  # Cancel old place of image during movement.
    # screen.blit(apple, object_movement(apple, t0))
    pygame.display.flip()

    clock.tick(60)

pygame.quit()