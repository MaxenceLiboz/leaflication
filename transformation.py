from os import listdir
from os.path import isfile, join
from matplotlib import pyplot as plt
import click
from Dataset import Dataset


@click.command()
@click.option(
    "-d", "--directory", default=None,
    help="Path to the images directory",
)
@click.option(
    "-f", "--filename", default=None,
    help="Name of the image",
)
def transformation(directory, filename):
    dataset = Dataset(directory)
    if (directory is not None):
        dataset.imageTransformation.image_directory_transformation(directory)
    elif (filename is not None):
        dataset.imageTransformation.image_transformation(filename)
    else:
        print("No directory or filename provided. Use --help for more information.")


if __name__ == "__main__":
    try:
        transformation()
    except Exception as e:
        print("An error occurred.")
