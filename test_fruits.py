import pygame

from functions.CONFIGS import *

apple = pygame.image.load("assets/images/fruits/apple.png")
# apple = pygame.transform.scale(apple, (90, 90))

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)

clock = pygame.time.Clock()

x0 = 500
y0 = 300
v = 10
t0 = pygame.time.get_ticks()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    t = (pygame.time.get_ticks() - t0) / 50

    x = x0 + v * t
    y = y0 + v * t

    screen.fill((0, 0, 0))  # Optional: Clears the screen every frame (black background)
    screen.blit(apple, (x, y))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
