# Image Winner Detection with HSV Masking and OCR

A simple Computer Vision project which determines the winner of a Bedwars game.

This project uses OpenCV and EasyOCR to detect the winner in an image based on HSV color masking and Optical Character Recognition (OCR). The script processes an image, identifies regions of interest based on color ranges, and extracts text to determine the winner.

## Features
**HSV Masking**: Utilizes HSV color space to create masks for specific color ranges.

**Optical Character Recognition**: Uses EasyOCR to read text from the masked regions.

**Winner Detection**: Determines the winner based on predefined criteria in the extracted text.

**Handling various image sizes**: Able to handle all types of screenshots of varying resolutions and smartly resizes the image based to focus on the scorecard.

Top Killer detection will be added soon.

## Command Line Usage
```
python ocr.py (path to image)
```

## Examples

### Original Image

![Image2](https://github.com/Wxua2005/Bedwars-Win-Detector/assets/137981148/6f5de116-9dc8-482b-ac5c-7250c76dc006)

### Detected Image 

 ![image](https://github.com/Wxua2005/Bedwars-Win-Detector/assets/137981148/73760ca2-3e04-46f1-b0cc-ce831c9f368d)

### Image Mask

The Mask filters out all unnecessary information and OCR detection is performed on this mask

![image](https://github.com/Wxua2005/Bedwars-Win-Detector/assets/137981148/026708d8-f3d9-4d97-a1f1-4b751bbf204a)

### Win Output

![Screenshot 2024-06-15 162926](https://github.com/Wxua2005/Bedwars-Win-Detector/assets/137981148/e7554685-0189-4ca5-93bb-612bf8129ae9)

## Discord
wxua
