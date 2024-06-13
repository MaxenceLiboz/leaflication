
# Documentation of the project Leafliction

## Requirement
First you must download the database: [link to download](https://cdn.intra.42.fr/document/document/17458/leaves.zip) (require intra access)  
Then the subject ask you to respect the flake8 norm (as we are using python), it will be downloaded in the env part.  
Make sure you are using the extension to see the error in vscode.

## Environement

You need to set up a venv in python with the requirements.txt
```
python3 -m venv .project-env
source .project-env/bin/activate
pip install -r requirements.txt
```
  
If you take the dataset from the 42 intra you must do some changes in order for it to work best on our project:  
First, add an Apple and Grape folder where you are going to put each subdirectory related to them.  
Second, you will change all the space by "_" with this command:
```
for file in leaves/images/*/*/*; do mv "$file" `echo $file | tr ' ' '_'` ; done
```

Then you are set to start coding or reviewing the project
## Part 1


Use of the library [click](https://click.palletsprojects.com/en/8.1.x/) that allow us to take argument of the user

All we need to do is look inside all the dir of the dataset to count the files
this will give us the distribution of the dataset.


## Part 2

Start looking at the [Pillow library (PIL fork)](https://pillow.readthedocs.io/en/stable/reference/Image.html)  

We will create a function for each augmentation we want to do. Theses augmentations are going to be:
- Rotation (Done)
- Blur (Done)
- Contrast (Done)
- Scaling (Done)
- Illumination (Done)
- Stretching (Done)

Each image will be saved in a folder with the name like so:  
- ORIGINAL_NAME_TYPE_OF_DATA_AUGMENTATION.jpg
