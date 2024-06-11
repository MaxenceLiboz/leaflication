from os import listdir
from os.path import isfile, join
from matplotlib import pyplot as plt
import click
from Dataset import Dataset


@click.command()
@click.option(
    "-d", "--dataset_dir", default=None,
    help="Path to the dataset directory",
    required=True
)
def distribution(dataset_dir):
    dataset = Dataset(dataset_dir)
    dataset.distribution()


if __name__ == "__main__":
    try:
        distribution()
    except Exception as e:
        print("An error occurred. Make sure the dataset directory has as many subdirectories as categorie for the fruit.")
