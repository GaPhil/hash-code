import os

from pprint import pprint

DatasetFolder = "Datasets"


def parse(fname):
    with open(fname,"r") as f:
        lines = f.readlines()

    if (len(lines)==0):
        return []

    #Skip first line
    lines = lines[1:]

    pictures = []
    for line in lines:
        picture = ["-"]
        line = line.split(" ")
        picture[0] = line[0]#Orientation
        if line[1] == "0":
            return picture
        line = line[2:]
        for tag in line:
            picture.append(tag.strip())
        pictures.append(picture)

    return pictures

def main():
    datasetPath = os.path.join(DatasetFolder,"a_example.txt")
    pictures = parse(datasetPath)
    pprint(pictures)

if __name__ == "__main__":
    main()