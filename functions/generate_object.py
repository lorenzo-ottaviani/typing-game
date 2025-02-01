from .init_pygame import *
import random
from random import uniform


def generate_object():
    """
    Create a new object (fruit, bomb or ice-cube) to be display in the game.
    Takes the form of a dictionary.
    :return: The new object.
    """
    type = random.choice(object_type)
    object_data = {
        "type": type[0],
        "img": type[1],
        "letter": random.choice(OBJECT_LETTERS),
        "x": uniform(x_min, x_max),  # Where the object should be positioned on x-coordinate
        "y": HEIGHT,  # Object beginning at the bottom of the screen
        "speed_x": uniform(-7, 7),  # Control the speed of objects in x-direction ( RIGHT or LEFT )
        "speed_y": uniform(-17, -15),  # Control the speed of objects in y-direction ( UP )
        "time": 0,
    }
    return object_data
