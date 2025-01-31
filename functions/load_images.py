from .init_pygame import *

def load_images(object_type):
    """

    :param object_type:
    :return:
    """
    image_path = "assets/images/fruits/" + object_type + ".png"
    object_data[object_type] = {
        "image" : pygame.image.load(image_path),
    }
    