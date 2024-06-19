import cv2 as cv
import re

def normalise(image, mask):
    if (image.shape[0], image.shape[1]) == (1440, 2560):
        start_w = 0
        start_h = 900

        end_w = 700
        end_h = 1440
        cropped = image[start_h:end_h, start_w:end_w]
        mask = mask[start_h:end_h, start_w:end_w]
        return cropped, mask


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

def jacquard_similarity(word1, word2):
    set1 = set(word1)
    set2 = set(word2)
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    return len(intersection) / len(union)

def MostSimilar(input_word, word_list):
    highest_similarity_score = -1
    most_similar = None

    for word in word_list:
        similarity_score = jacquard_similarity(input_word, word)
        if similarity_score > highest_similarity_score:
            highest_similarity_score = similarity_score
            most_similar = word

    return most_similar, highest_similarity_score


