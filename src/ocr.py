import cv2 as cv
import argparse
from easyocr import Reader
from utils import normalise, MostSimilar
import re
from constants import *

def main(image_path: str, show: str) -> tuple:
    has_won = False
    winner = None
    MVP = None

    img = cv.imread(image_path)
    img3 = img.copy()
    img3 = cv.cvtColor(img3, cv.COLOR_BGR2HSV)

    # Creating a mask for RED and GREEN and combining them using bitwise_or
    mask_green = cv.inRange(img3, lower_green, upper_green)
    mask_red = cv.inRange(img3, lower_red, upper_red)
    mask_yellow = cv.inRange(img3, lower_yellow, upper_yellow)

    mask = cv.bitwise_or(mask_green, mask_red, mask=None)
    mask = cv.bitwise_or(mask, mask_yellow, mask=None)

    # Normalising image and mask for screenshots of different resolutions
    img, mask = normalise(img, mask)

    imgMVP = img.copy()

    # Initialising OCR reader object and performing detection on the mask
    reader = Reader(lang_list=['en'], gpu=False)
    results = reader.readtext(mask)

    # Going through each detection and extracting the information
    for detection in results:
        top_left = tuple([int(val) for val in detection[0][0]])
        bottom_right = tuple([int(val) for val in detection[0][2]])
        text = detection[1]

        if text == '1st Killer' or text == 'lst Killer' or text == 'Ist Killer':
            imgMVP = imgMVP[top_left[1]:bottom_right[1], top_left[0]:int(bottom_right[0] + ((img3.shape[1] / img3.shape[0]) * 120))]
            imgMVP = cv.cvtColor(imgMVP, cv.COLOR_BGR2HSV)
            imgMVP = cv.bitwise_or(cv.inRange(imgMVP, lower_MVP, upper_MVP), cv.inRange(imgMVP, lower_gray, upper_gray), mask=None)

        if '3rd' in text.split() or 'Killer' in text.split():
            has_won = True

        if MostSimilar(text.lower(), ["red"])[1] > 0.4 and not has_won:
            winner = "Red"
            has_won = True

        elif MostSimilar(text.lower(), ["green"])[1] >= 0.6 and not has_won:
            winner = "Green"
            has_won = True

        img = cv.rectangle(img, top_left, bottom_right, (0, 255, 0), 2)

    if not has_won:
        print("ERROR CANT DETERMINE WINNER")
        winner = "None"

    if show == "True":
        cv.imshow("Detected", img)
        cv.imshow('mask', mask)
        cv.imshow('MVP', imgMVP)
        cv.waitKey(0)

    results2 = reader.readtext(imgMVP)
    ignored_words = ["MVP", "MIIP", "VIP", "VlP"]

    for detection in results2:
        matches = re.findall(pattern, detection[1])
        matches = [word for word in matches if word not in ignored_words]
        if matches:
            MVP = matches[0]
    print(winner, MVP)
    return winner, MVP

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Detect winner in an image based on HSV masking and OCR.")

    parser.add_argument("image_path", help="Path to image input")
    parser.add_argument("show", help="If True, will display the mask and the detection")
    args = parser.parse_args()

    main(args.image_path, args.show)

