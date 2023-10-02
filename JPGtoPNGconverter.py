from PIL import Image
import sys
import os

# Grab first and second argument from command line text
image_folder = sys.argv[1]
converted_images = sys.argv[2]

# Check if new file exists. If not, create it.
if not os.path.exists(converted_images):
    os.mkdir(converted_images)

# Turn the jpg folder contents into a list.   
list_jpg = os.listdir(image_folder)

# Loop over jgp folder and convert contents into png. Send newly converted images to new folder. 
for i in list_jpg:
    base_name, remove_jpg = os.path.splitext(i)
    img = Image.open(f'./images/{base_name}.jpg')
    img.save(f'./new/{base_name}.png', 'png')