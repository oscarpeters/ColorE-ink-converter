# Waveshare 5.65 Inch Color E-paper display image converter
This program fully automates the process from a `.PNG`, `.JPG`, and `.Jpeg` to a file format
which a microcontroller can read and use to show on the E-paper

![Alt Text](https://github.com/oscarpeters/ColorE-ink-converter/blob/main/Lena(converter)gif.gif)

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

## Exceptional credits
The converter program is copied from [CNlohr](https://github.com/cnlohr/epaper_projects "CNLohr") his repo, were I am using it to make the `.RAW` files. 
