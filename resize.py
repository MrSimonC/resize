from PIL import Image
import os
import sys
__version__ = '1.0'


def resize(file_path, new_width, sub_folder='resized'):
    # Resize any input image, outputting to a folder
    img = Image.open(file_path)
    new_height = int((float(img.size[1]) * float((new_width / float(img.size[0])))))
    img = img.resize((new_width, new_height), Image.ANTIALIAS)
    source_folder, source_file = os.path.split(file_path)
    save_to_dir = os.path.join(source_folder, sub_folder)
    if not os.path.exists(save_to_dir):
        os.makedirs(save_to_dir)
    save_to = os.path.join(source_folder, sub_folder, source_file)
    img.save(save_to)  # quality=75 default (0-95)


file = sys.argv[1]
width = int(sys.argv[2])
try:
    resize(file, width, sys.argv[3])
except IndexError:
    resize(file, width)
