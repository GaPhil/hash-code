import os

from pprint import pprint

DatasetFolder = "Datasets"


def parse(fname):
    with open(fname, "r") as f:
        lines = f.readlines()

    if (len(lines) == 0):
        return []

    # Skip first line
    lines = lines[1:]

    pictures = []
    for line in lines:
        picture = ["-"]
        line = line.split(" ")
        picture[0] = line[0]  # Orientation
        if line[1] == "0":
            return picture
        line = line[2:]
        for tag in line:
            picture.append(tag.strip())
        pictures.append(picture)

    return pictures


def interest(slide1, slide2):
    # n^2
    common = 0
    slide1notslide2 = 0
    slide2notslide1 = 0
    for tag in slide1:
        if tag in slide2:
            common += 1
        else:
            slide1notslide2 += 1
    slide2notslide1 = len(slide2) - common
    return min(common, slide1notslide2, slide2notslide1)


def main():
    datasetPath = os.path.join(DatasetFolder, "a_example.txt")
    pictures = parse(datasetPath)
    pprint(pictures)

    print(interest(pictures[1], pictures[2]))

if __name__ == "__main__":
    main()
