
import matplotlib.pyplot as plt
from PIL import Image, ImageFilter, ImageEnhance
import random
import math
import os
import click
from ImageAugmentation import ImageAugmentation

@click.command()
@click.option(
    "-f", "--image_path", default=None,
    help="Path to the file to augment",
    required=True
)
def augmentation(image_path):
    imageAugmentation = ImageAugmentation()
    imageAugmentation.image_augmentation(image_path)


if __name__ == "__main__":
    try:
        augmentation()
    except Exception as e:
        print(e)
    
