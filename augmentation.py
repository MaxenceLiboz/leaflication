
import matplotlib.pyplot as plt
from PIL import Image, ImageFilter, ImageEnhance
import random

# from tensorflow.keras import layers


def rotation(image):
    return image.rotate(random.randint(-60, 60))


def blur(image):
    return image.filter(ImageFilter.BoxBlur(random.uniform(0.5, 2.5)))


def constrast(image):
    enhancer = ImageEnhance.Contrast(image)
    return enhancer.enhance(random.uniform(0.5, 5))


def scaling(image):
    width, height = image.size

    # Setting the points for cropped image
    left = random.randint(0, width // 6)
    top = random.randint(0, height // 6)
    right = random.randint(width // 4 * 3, width)
    bottom = top + right - left

    new_image = image.crop((left, top, right, bottom))
    return new_image.resize((width, height))


def illumination(image):
    enhancer = ImageEnhance.Brightness(image)
    return enhancer.enhance(0.4 * random.randint(1, 6))


if __name__ == "__main__":
    image = Image.open('image (1).JPG')
    image_arr = tf.keras.utils.img_to_array(image)

    # print(rotated_image)
    # plt.imshow(rotation(image))
    # plt.imshow(blur(image))
    # plt.imshow(constrast(image))
    # plt.imshow(scaling(image))
    plt.imshow(illumination(image))
    plt.show()
    # plt.imshow(tf.keras.preprocessing.image.array_to_img(rotated_image))
