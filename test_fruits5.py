import pygame
from random import uniform, choice
from functions.CONFIGS import *  # Import everything from Config.py

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)

clock = pygame.time.Clock()

x_min = 6 / 14 * SCREEN_WIDTH
x_max = 8 / 14 * SCREEN_WIDTH

# List to hold the fruits (game objects)
fructificator = []

def generate_object():
    """Generates a random object (fruit) with a type, position, and speed."""
    objet = {
        "type": choice(object_type),  # Random fruit image
        "x": uniform(x_min, x_max),   # Random X position
        "y": SCREEN_HEIGHT,           # Start from the top of the screen
        "speed_x": uniform(-7, 7),    # Random X speed (left or right)
        "speed_y": uniform(-17, -15)  # Random Y speed (falling down)
    }
    return objet

# Track the initial time for motion calculations
t0 = pygame.time.get_ticks()

# Store the x and y positions of the fruits
x_values = []
y_values = []

# Maximum number of fruits
MAX_FRUITS = 8

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Add a new fruit if there are fewer than MAX_FRUITS
    if len(fructificator) < MAX_FRUITS:
        new_fruit = generate_object()
        fructificator.append(new_fruit)
        x_values.append(new_fruit["x"])
        y_values.append(new_fruit["y"])

    # Calculate time since the game started to simulate gravity and movement
    t = (pygame.time.get_ticks() - t0) / 400  # Adjust speed of movement

    # Update positions of the fruits based on their speed and gravity effect
    for i in range(len(fructificator)):
        x_values[i] += fructificator[i]["speed_x"]
        y_values[i] += fructificator[i]["speed_y"] * t + 5 * t ** 2  # Parabolic motion

        # Check if the fruit is out of the screen (y position is too high)
        if y_values[i] > SCREEN_HEIGHT:
            # Remove the fruit from the list if it goes off-screen
            fructificator[i] = generate_object()  # Replace it with a new fruit
            x_values[i] = fructificator[i]["x"]
            y_values[i] = fructificator[i]["y"]

    # Clear the screen (background)
    screen.fill((0, 0, 0))  # You can change this if you want a specific background color

    # Draw the fruits on the screen at their updated positions
    for i in range(len(fructificator)):
        screen.blit(fructificator[i]["type"], (x_values[i], y_values[i]))  # Blit the fruit image

    # Update the display to show the newly rendered frame
    pygame.display.flip()

    # Control the frame rate (60 FPS)
    clock.tick(60)

pygame.quit()
