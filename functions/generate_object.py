from functions.init_pygame import *
import random
from random import uniform
from functions.draw_text import draw_text

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
