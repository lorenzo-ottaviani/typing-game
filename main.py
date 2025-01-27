"""
Authors : Lorenzo OTTAVIANI, Olivier PORTAL et Thibault CARON.
Date : 27/01/2025 11h45
Aim of the program :
    Execute a typing fruit game with PyGame.
Inputs :
Output :
"""
from functions.CONFIGS import *
from functions.class_app import *
from functions.generate_random_fruits import generate_random_fruits


def main():
    """"""
    App().run()
    generate_random_fruits()


if __name__ == "__main__":  # The program will be run only if executed directly, not if it is called by another program.
    main()
