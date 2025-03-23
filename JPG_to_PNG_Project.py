from PIL import Image, ImageFilter
import sys
import os

def jpg_to_png():
    current_folder = sys.argv[1]
    new_folder = sys.argv[2]
    if not os.path.exists(new_folder):
        os.makedirs(new_folder)
    for file in os.listdir(current_folder):
        img = Image.open(f'{current_folder}{file}')
        remove_jpg = os.path.splitext(file)[0]
        img.save(f'{new_folder}{remove_jpg}.png', 'png')
        print('all done!')
jpg_to_png()
