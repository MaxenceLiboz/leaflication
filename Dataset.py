from ImageAugmentation import ImageAugmentation
from os import listdir
from os.path import isfile, join
from matplotlib import pyplot as plt
from PIL import Image

# This class is going to be used to describe the dataset, balance it, and split it into training and testing sets.
class Dataset:
    def __init__(self, dataset_dir: str):
        self.dataset_dir: str = dataset_dir
        self.leaves: dict = {}
        self.total_images: int = 0
        self.training_set: dict = {}
        self.testing_set: dict = {}
        self.imageAugmentation = ImageAugmentation()


    # Need to implement the training and testing set split
    def distribution(self, verbose: bool = True):


        for dir in listdir(self.dataset_dir):
            if not isfile(join(self.dataset_dir, dir)):
                self.leaves[dir] = 0

        for dir in self.leaves:
            for file in listdir(join(self.dataset_dir, dir)):
                if isfile(join(self.dataset_dir, dir, file)):
                    self.leaves[dir] += 1

        if (verbose):
            print(self.leaves)

            # Create a pie chart with the distribution of the dataset
            fig = plt.figure(figsize=(15, 10))
            fig.add_subplot(1, 1, 1)
            plt.pie(self.leaves.values(), labels=self.leaves.keys(), autopct="%1.1f%%")
            plt.title("Distribution of the dataset")
            plt.legend(loc="upper right")
            plt.show()

        
    def balance(self, verbose: bool = True):
        if (self.leaves == {}):
            self.distribution(False)
        self.total_images = sum(self.leaves.values())
        max_images = max(self.leaves.values())

        for dir in self.leaves:
            augmentation_to_do = (max_images - self.leaves[dir]) // 6

            # Get the first 'x' images from the directory
            images = listdir(join(self.dataset_dir, dir))[:augmentation_to_do]

            if verbose:
                print(f"Augmenting images for {dir} with {augmentation_to_do} images which bring it to {self.leaves[dir] + (augmentation_to_do * 6)} images.")

            # Call the image_augmentation method on each image
            for image in images:
                image_path = join(self.dataset_dir, dir, image)
                self.imageAugmentation.image_augmentation(image_path, False)

        if (verbose):
            print(self.leaves)