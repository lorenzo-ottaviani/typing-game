from .init_pygame import *
import random

x_min = 6/14 * WIDTH
x_max = 8/14 * WIDTH

def generate_object():
    object_data[] = {
        "type": random.choice(object_type),
        "img": pygame.image.load(f"images/{type}.png"),
        "letter": random.choice(OBJECT_LETTERS),
        "x" : random.randint(100, 500),          # where the object should be positioned on x-coordinate
        "y" : 800,
        "speed_x": random.randint(-20, 20),      # how fast the object should move in x direction. Controls the diagonal movement of objects
        "speed_y": random.randint(-80, -60),    # control the speed of objects in y-direction ( UP )
        "t": 0,                                 # manages the
        "hit": False,
    }