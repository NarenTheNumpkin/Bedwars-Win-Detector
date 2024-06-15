import cv2 as cv

def normalise(image, mask):
    if (image.shape[0], image.shape[1]) == (1440, 2560):
        start_w = 0
        start_h = 900

        end_w = 700
        end_h = 1440
        cropped = image[start_h:end_h, start_w:end_w]
        mask = mask[start_h:end_h, start_w:end_w]
        return cropped, mask

    # idea -- before we encounter ELIMINATED or any other keyword (3rd Killer) we can put bool value to test wins and correctly decide who won.

    elif (image.shape[0], image.shape[1]) == (1080,1920):
        start_w = 0
        start_h = 480

        end_w = 1039
        end_h = 1080

        cropped = image[start_h:end_h, start_w:end_w]
        mask = mask[start_h:end_h, start_w:end_w]
        return cropped, mask

    else:
        return image, mask

def Similarity(string, string2="Green"):
    string = string.lower()
    string = string.capitalize()
    if len(string) != len(string2):
        return 0
    correct = 0
    for i in range(len(string)):
        if string[i] == string2[i]:
            correct += 1

    return correct/len(string)


