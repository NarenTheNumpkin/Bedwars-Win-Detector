import cv2 as cv
import argparse
from easyocr import Reader
import numpy as np
from utils import normalise, Similarity


def main(image_path):
    img = cv.imread(image_path)
    img3 = img.copy()
    img3 = cv.cvtColor(img3, cv.COLOR_BGR2HSV)

    lower = np.array([0, 66, 100])
    upper = np.array([0, 255, 255])

    lower_green = np.array([40, 120, 203])
    upper_green = np.array([79, 255, 255])

    has_won = False
    winner = None

    mask_green = cv.inRange(img3, lower_green, upper_green)
    mask_red = cv.inRange(img3, lower, upper)
    mask = cv.bitwise_or(mask_green, mask_red,mask=None)

    img, mask = normalise(img, mask)

    reader = Reader(lang_list=['en'], gpu=False)
    results = reader.readtext(mask)

    for detection in results:
        top_left = tuple([int(val) for val in detection[0][0]])
        bottom_right = tuple([int(val) for val in detection[0][2]])
        text = detection[1]

        if '3rd' in text.split() or 'Killer' in text.split():
            has_won = True

        if Similarity(text, "Red") > 0.4 and not has_won:
            winner = "Red"
            has_won = True

        elif Similarity(text) >= 0.6 and not has_won:
            winner = "Green"
            has_won = True

        img = cv.rectangle(img, top_left, bottom_right, (0, 255, 0), 2)

    if not has_won:
        print("ERROR CANT DETERMINE WINNER")

    print(winner)
    cv.imshow("Detected", img)
    cv.imshow('mask', mask)
    cv.waitKey(0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Detect winner in an image based on HSV masking and OCR.")
    parser.add_argument("image_path", help="Path to image input")

    args = parser.parse_args()
    main(args.image_path)
