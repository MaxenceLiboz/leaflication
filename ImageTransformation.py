from plantcv import plantcv as pcv
import cv2
import numpy as np
import matplotlib.pyplot as plt
import math
import os

class ImageTransformation:
    def __init__(self, image: np.ndarray = None):
        self.image: np.ndarray = None
        self.directory: str = None
        self.image_name: str = None
        self.transformations_list = [
            self.rgb_to_gray, self.mask, self.analyze_object
        ]


    # We already have bllur as data augmentation ? may have to change to something else
    # In the subject it seems they misspelled the word and used blur instead of rbg_to_gray
    def gaussian_blur(self):
        return pcv.gaussian_blur(img=self.image, ksize=(51, 51), sigma_x=0, sigma_y=None)
    

    # Turn rbg image to gray scale
    def rgb_to_gray(self):
        hsv = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)

        # find the green color 
        mask_green = cv2.inRange(hsv, (36,0,0), (86,255,255))
        # find the brown color
        mask_brown = cv2.inRange(hsv, (8, 60, 20), (30, 255, 200))
        # find the yellow color in the leaf
        mask_yellow = cv2.inRange(hsv, (21, 39, 64), (40, 255, 255))

        # find any of the three colors(green or brown or yellow) in the image
        gray_image = cv2.bitwise_or(mask_green, mask_brown)
        gray_image = cv2.bitwise_or(gray_image, mask_yellow)
        return gray_image
    

    # Remove the background of the image
    def mask(self):
        mask = self.rgb_to_gray()
        return cv2.bitwise_and(self.image, self.image, mask= mask)
    

    def analyze_object(self):
        labeled_mask = self.rgb_to_gray()
        return pcv.analyze.size(img=self.image, labeled_mask=labeled_mask)
    

    def image_transformation(self, image_path: str, show_images: bool = True, save_transformations: bool = False):

        if self.directory is None:
            self.directory: str = os.path.dirname(image_path) if os.path.dirname(image_path) != "" else "."
        self.image_name: str = os.path.basename(image_path).split(".")[0]
        
        img = cv2.imread(os.path.join(self.directory, os.path.basename(image_path)))
        self.image = img


        if (self.image is None):
            print("Image not found")
            return
        image_list = [("original", self.image)]
        for transformation in self.transformations_list:
            image_list.append((transformation.__name__, transformation()))

        if show_images:
            self.plot_images(image_list)

        if save_transformations:
            for i, (title, image) in enumerate(image_list):
                if (i == 0):
                    continue
                cv2.imwrite(f"{self.directory}/{self.image_name}_{title}.jpg", image)

    
    def image_directory_transformation(self, directory: str):
        self.directory = directory
        for file in os.listdir(directory):
            print(f"Transforming: {file}", end="\r")
            self.image_transformation(file, False, True)

    
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
            plt.imshow(image, cmap="gray")

        # Show the plot
        plt.show()


if __name__ == "__main__":
    imageTransformation = ImageTransformation()
    image_list = ["image.jpg", "image_healthy.jpg", "image_rust.jpg", "image_scab.jpg"]

    imageTransformation.image_directory_transformation("./leaves/images/Apple/Apple_Black_rot")