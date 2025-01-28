import pygame
import random

from .CONFIGS import *
from .class_app import *

fruit_data = {}

def generate_random_fruits(fruit):
    # stock fruits images
    fruits_types = ["apple", "banana", "bomb", "cherry", "ice_cube", "mango", "pear", "strawberry"]
    fruit = random.choice(fruits_types)
    
    # 
    fruit_data[fruit] = {
        'img' : pygame.image.load("assets/images/fruits" + fruit + ".png")
    }
    App.screen.blit(fruit_data[0], (50, 50))
    print(fruit)
    print(fruit_data)



