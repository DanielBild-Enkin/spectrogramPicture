"""loads images and converts to array other functions can use"""
import numpy as np
from PIL import Image

def load_image(path):
    """loads images"""
    return Image.open(path)


def make_scaled_array(img):
    """converts image into array usuable by other functions.
    converts RGB to single number (gray scale).
    scales array from 0-127 to 0-1 and reverses scale to work
    with the Audacity spetrogram."""
    int_array = np.array(img)
    flat_int_array = np.sum(int_array, 2)
    scaled_array = np.flipud(1-(flat_int_array/382.5-1))
    return scaled_array
