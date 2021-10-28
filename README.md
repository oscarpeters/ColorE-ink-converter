## Inspirated by [CNlohr](https://github.com/cnlohr/ "CNLohr") for his contribution in making the next level interactive displays. 

Watching his YouTube video gave me the spirit to make a display like his, but would not spent much time 
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
## Making Converter file
```
sudo make all
```
## Exceptional credits
The converter program is copied from [CNlohr](https://github.com/cnlohr/epaper_projects "CNLohr") his repo, were I am using it to make the `.RAW` files. 
