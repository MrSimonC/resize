# Image Resizer
Simple image resizer for windows command line. 

Will resize images and place in a subfolder, keeping the image's filename. It keeps the original image intact.

## Usage
```dos
resize.exe image_path width [folder_name]
```
* image_path = file path to the image you want to resize
* width = the new image width
* folder_name _(optional)_ = the name of the subfolder you want created. Default is "resized".

Example:
```dos
resize.exe "c:\my file.png" 1000
```
...will resize your `c:\my file.png` image to be correct aspect ratio but with new width of 1000. 

It will output new image `c:\resized\my file.png`