# Waveshare 5.65 Inch Color E-paper display image converter
![Linux](https://img.shields.io/badge/-Linux-grey?logo=linux)
![OSX](https://img.shields.io/badge/-OSX-black?logo=apple)

This program fully automates the process from a `.PNG`, `.JPG`, and `.Jpeg` to a file format
which a microcontroller can read and use to show on the E-paper

![Alt Text](https://github.com/oscarpeters/ColorE-ink-converter/blob/main/Lena(converter)gif.gif)

The image is resized and white stripes are added to get the aspect ratio right. Dithering is added because of the 7 colors which the display can produce.
This picture is an example while the original image and the converted image are overlayed and resized to fit on top of eachother.

The `Epaper display` is **600 x 448** pixels while `Lena Test Image` is **512 x 512** pixels. Therefore, the white stripes on each end of the dithered picture. 

## Inspirated by [CNlohr](https://github.com/cnlohr/ "CNLohr") YouTube video. 

Watching his [YouTube Video](https://www.youtube.com/watch?v=YawP9RjPcJA&t=248s "YouTube") gave me the spirit to make a display like his, but would not spent much time 
when converting a normal `.PNG` or `.JPG` to `.RAW` to be read by the microcontroller.

Therefore, made this not so handsome Python program to convert the pictures automatically in matter of seconds.

The program is tested on `MacOs`, `Windows`, and `Linux` were the Windows version has some issues when
converting dithered picture to a `.RAW` file.  

| Maps        | Usage           |
| ------------- |:-------------:|
| Input      | Put here the Pictures you want to be converted | 
| PNG    | Converted dithered pictures output   |
| PNG/undithered | size matched pictures, debug      |
| SDcard | `.RAW` files to be placed onto an SD-card|

## Setup: 
#### Install Python libraries
```
pip install pillow tqdm
``` 

#### Install *ImageMagick*
| Platform        | How-to           |
| ------------- |:-------------:|
| Windows | [ImageMagick Website](https://imagemagick.org/script/download.php "ImageMagick")|
| Linux | ```sudo apt install imagemagick ``` |
| MacOs |  ```brew install imagemagick ``` |

* When using MacOs, `Homebrew` should be installed by:
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
**Additional information:**
The script is looking if ImageMagick is installed on Linux & MacOs, and will install it if necassary.

## Additional software:
**`GCC`** must be installed to make `.RAW` files. 
### Windows :
* Install MingW by following this [YouTube video](https://www.youtube.com/watch?v=sXW2VLrQ3Bs "Installing GCC on Windows")

**The Python script is looking if GCC is installed and will for Linux & MacOs automatically install it if not installed yet.**


## SD-card formatting

There are a couple of issues when using some SD-cards from unknown brands, these SD-cards have a different block size which when converting the correct format
will not work. 

I am using `Lexar 633x 32Gb` SD-cards which work fine.
SD-card must be converted to `FAT32` with a **MAXIMUM** size of **35MB**.  

## Credits
The converter program is copied from [CNlohr](https://github.com/cnlohr/epaper_projects "CNLohr") his repo, were I am using it to make the `.RAW` files. 
