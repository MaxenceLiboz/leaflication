from os import listdir
from os.path import isfile, join
from matplotlib import pyplot as plt
import click


@click.command()
@click.option(
    "-d", "--dataset_dir", default=None,
    help="Path to the dataset directory",
    required=True
)
@click.option(
    "-f", "--fruit_name", default=None,
    help="Name of the fruit to show the distribution",
    required=False
)
def distribution(dataset_dir, fruit_name):

    list_dir = {}
    for dir in listdir(dataset_dir):
        if (fruit_name is None
                or fruit_name.upper() and fruit_name.upper() in dir.upper()):
            list_dir[dir] = 0

    if list_dir == {}:
        print(f"No directory found with the name '{fruit_name}'")
        return

    for dir in list_dir:
        for file in listdir(join(dataset_dir, dir)):
            if isfile(join(dataset_dir, dir, file)):
                list_dir[dir] += 1
    print(list_dir)

    # Create a pie chart with the distribution of the dataset
    fig = plt.figure(figsize=(15, 10))
    fig.add_subplot(1, 1, 1)
    plt.pie(list_dir.values(), labels=list_dir.keys(), autopct="%1.1f%%")
    plt.title("Distribution of the dataset")
    plt.legend(loc="upper right")
    plt.show()


if __name__ == "__main__":
    try:
        distribution()
    except Exception as e:
        print(e)
