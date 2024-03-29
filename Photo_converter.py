'''
This software (or any portion thereof that is not already copywritten by another
party may be licensed under the NewBSD or MIT licenses, preferring the MIT license.

MIT License         

Copyright (c) 2021  /'{$}'\ OscarPeters

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


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
from PIL import Image, ImageOps
from tqdm import tqdm


'''

User modifications change acordingly below

'''
# Waveshare size (5.65 inch)
size = (600, 448)  # panorama view
# size = (448, 600) # stand-up view

# Makes a White background, change accordingly (r,g,b,a)
background = Image.new('RGBA', size, (255, 255, 255, 255))
# Makes a Black background
# background = Image.new('RGBA', size, (0, 0, 0, 255))

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
 
# Initializes if the program can run properly
def init():
    # Checks system runnning program on, checks if GCC is installed, if not installs it        
    if platform.system() == 'Windows':
        if (which('gcc') is None):
            # For Windows the user has to install GCC manually, if not found raises an error
            raise TypeError(
                'GCC is not installed yet. Please follow the instructions on Github')
        else:
            subprocess.call(
                f'cd {file} | gcc -o .\converter.exe .\converter.c', shell=True)

    if platform.system() == 'Linux':
        if (which('magick') is None):
            print('Installing ImageMagick, this may take a while')
            subprocess.call('git clone https://github.com/ImageMagick/ImageMagick.git ImageMagick-7.1.0', shell=True)
            subprocess.run(['sh', 'ImageMagick-7.1.0/configure'])
            subprocess.call('sudo ldconfig /usr/local/lib', shell=True)
        if (which('gcc') is None):
            print('Installing GCC')
            subprocess.call(
                    f'sudo apt install build-essential manpages-dev -y', shell=True)
            subprocess.call(f'cd {file} | make ', shell=True)

    if platform.system() == 'Darwin':
        if (which('magick') is None):
            print('Installing ImageMagick')
            subprocess.call('brew install imagemagick', shell=True)
        if (which('gcc') is None):
            print('Installing GCC')
            subprocess.call(
                    f'brew install gcc && xcode-select --install', shell=True)
            subprocess.call(f'cd {file} | make ', shell=True)
        
        ## TODO: automatic see if executable is there or not and act on it.
        else:
            subprocess.call(f'cd {file} | make', shell=True)

    # Not yet tested
    subprocess.call('pip install pillow tqdm',shell=True)

def Pillow():
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
        if photo.endswith('.JPG') or photo.endswith('.JPEG') or photo.endswith('.jpeg') or photo.endswith('.jpg') or photo.endswith('.png'):

            # Open Photo to be converted and don't change the orientation, and change the size accordingly
            img = Image.open(f'{pathh}{photo}').convert('RGBA')
            img = ImageOps.exif_transpose(img)
            img.thumbnail(size, Image.LANCZOS)

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
        if (photo.endswith('.JPG') or photo.endswith('.JPEG') or photo.endswith('.jpeg') or photo.endswith('.jpg') or photo.endswith('.png')) is None:
            raise NameError(
                f'No pictures which end with either .png, .jpg or .jpeg\nError due to: {photo}')
        
            
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

        '''
        if Floyd-Steinberg doesn't look that great, you could try it with Riemersma dithering:
             subprocess.call(f'convert {old_path}{photo} -dither Riemersma -remap {old_path}palette.gif {new_path}{photo}', shell=True)
        '''
    print("\nPhotos converted to Dithered photos\n")


def Converter(converter_path, final_path, png_path):
    if platform.system() == 'Windows':
        for photo in os.listdir(png_path):
            if photo.endswith('.png'):
                # problem with using converter program with arguments automaticly
                subprocess.call(
                    f'cd {file} | .\converter {png_path}{photo} {final_path}{photo}.RAW', shell=True)
        for photo in os.listdir(final_path):
            if not photo.endswith('.RAW'):
                subprocess.call(f'del {final_path}{photo}', shell=True)
                print('Deleted unnecassary files in SD-card map')

    elif platform.system() == 'Darwin' or 'Linux':
        # Looking into the PNG map and converts these pictures to .RAW file by using the converter program from CNlohr
        for photo in os.listdir(png_path):
            if photo.endswith('.png'):
                subprocess.call(
                    f'cd {converter_path} && ./converter {png_path}{photo} {final_path}{photo}.RAW', shell=True)
        for photo in os.listdir(final_path):
            if not photo.endswith('.RAW'):
                subprocess.call(f'rm {final_path}{photo}', shell=True)
                print('Deleted unnecassary files in SD-card map')
    else:
        print("Don't know what you running this on?!")
    print("Converter is done.\nThe RAW files can be loaded into the SD-card\n")


if __name__ == '__main__':
    init()
    Pillow()
    FloydSteinberg(png_path_undithered, png_path)
    Converter(converter_path, final_path, png_path)
