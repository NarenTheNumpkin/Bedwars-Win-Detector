from ocr import main
import os
path = os.listdir("../test/images")
os.chdir("../test")


for i in path:
    result = main(os.path.join("images", i), show='False')
    with open("results.txt", "a") as file:
        file.writelines([result, '\t', i, '\n'])
