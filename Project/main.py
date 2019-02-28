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

    vpictures = []
    hpictures = []
    for line in lines:
        picture = ["-"]
        line = line.split(" ")
        picture[0] = line[0]  # Orientation
        line = line[2:]
        for tag in line:
            picture.append(tag.strip())
        if (picture[0] == "H"):
            if (line[1] == "0"):
                continue
            hpictures.append(picture)
        else:
            vpictures.append(picture)

    return [hpictures, vpictures]


def createAllSlides(hpictures, vpictures):
    slideShow = []
    for pic in hpictures:
        slideShow.append(pic)
    for i in range(0, len(vpictures), 2):
        slideShow.append([vpictures[i], vpictures[i + 1]])
    return slideShow


def createSlide(*args):
    # Const
    l = len(args)
    if l == 1:
        return [args[0]]
    elif l == 2 and args[0][0] == "V" and args[1][0] == "V":
        return [args[0], args[1]]
    else:
        return None


def interest(slide1, slide2):
    # n^2
    common = 0
    slide1notslide2 = 0
    for tag in slide1:
        if tag in slide2:
            common += 1
        else:
            slide1notslide2 += 1
    slide2notslide1 = len(slide2) - common
    return min(common, slide1notslide2, slide2notslide1)


def getEdges(slides):
    edgeMatrix = [[0 for i in range(len(slides))] for j in range(len(slides))]
    for i in range(len(slides)):
        for j in range(len(slides)):
            edgeMatrix[i][j] = interest(slides[i], slides[j])
    return edgeMatrix


def main():
    datasetPath = os.path.join(DatasetFolder, "a_example.txt")
    [hpictures, vpictures] = parse(datasetPath)
    pprint(hpictures)
    pprint(vpictures)
    pprint(createSlide(["H", "sun"]))
    pprint(createSlide(["V", "sun"], ["V", "beach"]))
    print(createAllSlides(hpictures, vpictures))

    print(interest(hpictures[0], hpictures[1]))
    print(getEdges(createAllSlides(hpictures, vpictures)))


if __name__ == "__main__":
    main()
