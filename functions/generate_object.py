from .init_pygame import *
import random

def generate_object(object):
    object_path = "images/" + object + ".png"
    object_data[object] = {
        "type": object,
        "img": pygame.image.load(object_path),
        "x" : random.randint(100,500),          # where the object should be positioned on x-coordinate
        "y" : 800,
        "speed_x": random.randint(-20, 20),      # how fast the object should move in x direction. Controls the diagonal movement of objects
        "speed_y": random.randint(-80, -60),    # control the speed of objects in y-direction ( UP )
        "t": 0,                                 # manages the
        "hit": False,
    }