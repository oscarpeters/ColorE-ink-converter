# Waveshare 5.65 Inch Color E-paper display image converter
This program fully automates the process from a `.PNG`, `.JPG`, and `.Jpeg` to a file format
which a microcontroller can read and use to show on the E-paper

## Inspirated by [CNlohr](https://github.com/cnlohr/ "CNLohr") his idea. 

Watching his [YouTube Video](https://www.youtube.com/watch?v=YawP9RjPcJA&t=248s "YouTube") gave me the spirit to make a display like his, but would not spent much time 
when converting a normal `.PNG` or `.JPG` to `.RAW` to be read by the microcontroller.

Therefore, made this not so handsome Python program to convert the pictures automaticly in matter of seconds.

The program is tested on `MacOs`, `Windows`, and `Linux` were the Windows version has some issues when
converting to dithered picture to a `.RAW` file. 

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
b/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" 
```


## Additional software:
**`GCC`** must be installed to do make `.RAW` files. 


## Exceptional credits
The converter program is copied from [CNlohr](https://github.com/cnlohr/epaper_projects "CNLohr") his repo, were I am using it to make the `.RAW` files. 
