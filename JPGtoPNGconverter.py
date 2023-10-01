from PIL import Image
import sys
import os

image_folder = sys.argv[1]
converted_images = sys.argv[2]


# print(f'This is my image file {image_folder}, and this is my converted file: {converted_images}')

if not os.path.exists(converted_images):
    os.mkdir(converted_images)
else:
    print('This folder already exists')
    
#Grab each image from image_folder and convert them to png and place them in the converted_images folder
for img in image_folder:
    img == Image
    img.convert()    

# if len(sys.argv) >= 2:
#     image_path = sys.argv[1]
#     image_path1 = sys.argv[2]
#     image_path2 = sys.argv[3]
#     # print(image_path, image_path1, image_path2)
#     try:
#         img = Image.open(image_path)
#     except Exception as e:
#         print(f"Error opening image: {e}")
#         sys.exit(1)
# else:
#     print('Ohhhh man! Not quite.')
#     sys.exit(1)
    
    