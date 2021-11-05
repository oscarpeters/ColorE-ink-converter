'''
    -----Inspired by the work of CNlohr-----
        
        Follow the instructions on GitHub    

        The images must be one of the below:
            - Jpeg
            - JPG
            - PNG
        
'''
import os
import subprocess
import platform
from shutil import which
from typing import Tuple
from PIL import Image, ImageOps
from tqdm import tqdm

# Automatic path information
file = (os.path.dirname(os.path.realpath(__file__)))
if platform.system() == 'Darwin' or 'Linux':
    # Linux & MacOs #
    pathh = file + '/input/'
    png_path = file + '/png/'
    png_path_undithered = file + '/png/undithered/'
    converter_path = file
    final_path = file + '/sdcard/'

if platform.system() == 'Windows':
    # Windows #
    pathh = os.path.join(file, 'input', "")
    png_path = os.path.join(file, 'png', "")
    png_path_undithered = os.path.join(file, 'png', 'undithered', "")
    converter_path = r'(file)'
    final_path = os.path.join(file, 'sdcard', "")

# Waveshare size (5.65 inch)
size = (600, 448)  # panorama view
# size = (448, 600) # stand-up view


# Initializes if the program can run properly
def init():
    # Checks system runnning program on, checks if GCC is installed, if not installs it
    if platform.system() == 'Darwin' or 'Linux': 
        if (which('gcc') is None): 
                print("gcc not installed")
                if platform.system() == 'Darwin':
                    subprocess.call(
                        f'brew install gcc && xcode-select --install', shell=True)
                    subprocess.call(f'cd {file} | make ', shell=True)
                elif platform.system() == 'Linux':
                    subprocess.call(
                        f'sudo apt install build-essential manpages-dev -y', shell=True)
                    subprocess.call(f'cd {file} | make ', shell=True)
    if platform.system() == 'Windows':
        if (which('gcc') is None):
            # For Windows the user has to install GCC manually, if not found raises an error
            raise TypeError('GCC is not installed yet. Please follow the instructions on Github')
        else:
            subprocess.call(f'cd {file} | gcc -o .\converter.exe .\converter.c', shell=True)

def main():
    # Makes a White background, change accordingly (r,g,b,a)
    background = Image.new('RGBA', size, (255, 255, 255, 255))
    background.save('background.png', 'PNG')

    # Counter for photo counter
    i = 0

    for photo in os.listdir(pathh):
        if photo.endswith('.JPG') or photo.endswith('.jpeg') or photo.endswith('.jpg') or photo.endswith('.png'):
            i += 1

    # Bar graph
    t = tqdm(desc="First stage converter", total=i,
             unit=" Images", disable=not True, smoothing=0.1, colour='#800000')

    # Making 5.65 inch pictures from within the INPUT map
    for photo in os.listdir(pathh):
        # converts only files ending with .jpg, .jpeg & .png
        if photo.endswith('.JPG') or photo.endswith('.jpeg') or photo.endswith('.jpg') or photo.endswith('.png'):

            # Open Photo to be converted and don't change the orientation, and change the size accordingly
            img = Image.open(f'{pathh}{photo}').convert('RGBA')
            img = ImageOps.exif_transpose(img)
            img.thumbnail(size, Image.ANTIALIAS)

            # Finding the middle of the photo to paste it in
            img_w, img_h = img.size

            # Achtergrond
            bg = Image.open('background.png')
            bg_w, bg_h = bg.size
            offset = (((bg_w - img_w) // 2), ((bg_h - img_h) // 2))
            bg.paste(img, offset)

            bg.convert('RGB').save(f'{png_path_undithered}{photo}.png', "PNG")
            t.update()
            # Uncomment to look at the output of the resized PNG pictures
            # bg.show()
        if photo.endswith('.JPG') or photo.endswith('.jpeg') or photo.endswith('.jpg') or photo.endswith('.png') is None:
            raise NameError('No pictures which end with either .png, .jpg or .jpeg')
    print(f'\nThere have been {i} photos converted\n')


# Dithering by Floyd-Steinberg algorithm
def FloydSteinberg(old_path, new_path):
    print(old_path)
  # makes the color palette E-ink
    subprocess.call(f'convert  \
      -size 50x50              \
      xc:"rgb(0,0,0)"          \
      xc:"rgb(255,255,255)"    \
      xc:"rgb(67,138,258)"     \
      xc:"rgb(100,64,255)"     \
      xc:"rgb(191,0,0)"        \
      xc:"rgb(255,243,56)"     \
      xc:"rgb(232,126,0)"      \
      xc:"rgb(194,164,244)"    \
      +append                  \
      {old_path}palette.gif', shell=True)
    print('\nWaveshare 5.65 inch 7-color palette made')

    for photo in os.listdir(old_path):
        if photo.endswith('.png'):
            subprocess.call(
                f'convert {old_path}{photo} -dither FloydSteinberg -define "dither:diffusion-amount=100%" -remap {old_path}palette.gif {new_path}{photo}', shell=True)

        ''' if Floyd-Steinberg doesn't look that great, you could try it with Riemersma dithering
             subprocess.call(f'convert {old_path}{photo} -dither Riemersma -remap {old_path}palette.gif {new_path}{photo}', shell=True)
        '''
    print("\nPhotos converted to Dithered photos\n")


def Converter(converter_path, final_path, png_path):
    if platform.system() == 'Windows':
        for photo in os.listdir(png_path):
            if photo.endswith('.png'):
                # problem with using converter program with arguments automaticly
                subprocess.call(f'cd {file} | .\converter.exe {png_path}{photo} {final_path}{photo}.RAW', shell=True)
            if not photo.endswith('.png'):
                subprocess.call(f'del {final_path}{photo}', shell=True)
                print('Deleted unnecassary files in SD-card map')
            
    elif platform.system() == 'Darwin' or 'Linux':
        # Looking into the PNG map and converts these pictures to .RAW file by using the converter program from CNlohr
        for photo in os.listdir(png_path):
            if photo.endswith('.png'):
                subprocess.call(
                    f'cd {converter_path} && ./converter {png_path}{photo} {final_path}{photo}.RAW', shell=True)
            if not photo.endswith('.png'):
                subprocess.call(f'rm {final_path}{photo}')
                print('Deleted unnecassary files in SD-card map')
    else:
        print("Don't know what you running this on?!")
    print("Converter is done.\nThe RAW files can be loaded into the SD-card\n")


if __name__ == '__main__':
    init()
    main()
    FloydSteinberg(png_path_undithered, png_path)
    Converter(converter_path, final_path, png_path)
