import pygame
from random import uniform

from functions.CONFIGS import *

apple = pygame.image.load("assets/images/fruits/apple.png")
# apple = pygame.transform.scale(apple, (90, 90))

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)

clock = pygame.time.Clock()

x_min = 6/14 * SCREEN_WIDTH
x_max = 8/14 * SCREEN_WIDTH

x = uniform(x_min, x_max)

y = SCREEN_HEIGHT

vx = uniform(-7, 7)
vy = uniform(-17, -15)

t0 = pygame.time.get_ticks()  # Initial time

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # t = t0  # Reset time at the beginning of object movement.

    t = (pygame.time.get_ticks() - t0) / 400  # Count the time during movement.

    x += vx
    y += vy * t + 5 * t**2

    screen.fill((0, 0, 0))  # Cancel old place of image during movement.
    screen.blit(apple, (x,y))
    pygame.display.flip()

    clock.tick(60)

pygame.quit()

