import matplotlib.pyplot as plt
from PIL import Image, ImageFilter, ImageEnhance
import random
import math
import os

class ImageAugmentation:
    def __init__(self):
        self.augmentation_list = [
            self.rotation, self.blur, self.contrast, self.scaling, self.illumination, self.stretch
        ]


    def rotation(self):
        return self.image.rotate(random.randint(-60, 60))


    def blur(self):
        return self.image.filter(ImageFilter.BoxBlur(random.uniform(0.5, 2.5)))


    def contrast(self):
        enhancer = ImageEnhance.Contrast(self.image)
        return enhancer.enhance(random.uniform(0.5, 5))


    def scaling(self):
        width, height = self.image.size

        # Setting the points for cropped image
        left = random.randint(0, width // 6)
        top = random.randint(0, height // 6)
        right = random.randint(width // 4 * 3, width)
        bottom = top + right - left

        new_image = self.image.crop((left, top, right, bottom))
        return new_image.resize((width, height))


    def illumination(self):
        enhancer = ImageEnhance.Brightness(self.image)
        return enhancer.enhance(0.4 * random.randint(1, 6))


    def stretch(self):
        width, height = self.image.size

        # Setting the points for cropped image
        left = random.randint(0, 30)
        top = random.randint(height // 2 - 50, height // 2 - 20)
        right = random.randint(width - 30, width)
        bottom = random.randint(height // 2 + 20, height // 2 + 50)

        new_image = self.image.crop((left, top, right, bottom))
        return new_image.resize((width, height))

    
    def image_augmentation(self, file_path: str, show_images: bool = True):
        ## Load the image and its attributes
        image = Image.open(file_path)
        self.image: Image = image
        self.directory: str = os.path.dirname(file_path) if os.path.dirname(file_path) != "" else "."
        self.image_name: str = os.path.basename(file_path).split(".")[0]

        # Create a list of images with the original image and the augmented images
        image_list = [("original", self.image)]
        for augmentation in self.augmentation_list:
            image_list.append((augmentation.__name__, augmentation()))

        # Show all images with the orginal image side by side for comparison
        self.plot_images(image_list) if show_images else None

        # Save the new augmented images
        for i, (title, image) in enumerate(image_list):
            if (i == 0):
                continue
            image.save(f"{self.directory}/{self.image_name}_{title}.JPG")

    
    def plot_images(self, image_list):
        # Determine the grid size
        grid_size = math.ceil(len(image_list) ** 0.5)

        # Create a new figure
        plt.figure(figsize=(10, 10))

        # Loop over the images
        for i, (title, image) in enumerate(image_list):
            # Create a new subplot
            plt.subplot(grid_size, grid_size, i + 1)

            # Remove the axis
            plt.axis('off')

            # Set the title
            plt.title(title)

            # Show the image
            plt.imshow(image)

        # Show the plot
        plt.show()