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
    for i in range(0, len(lines)):
        line = lines[i]
        picture = ["-"]
        line = line.split(" ")
        picture[0] = str(i)  # Line number
        orientation = line[0]
        line = line[2:]
        for tag in line:
            picture.append(tag.strip())
        if (orientation == "H"):
            if (line[1] == "0"):  # skip
                continue
            hpictures.append(picture)
        else:
            vpictures.append(picture)

    return [hpictures, vpictures]


def createAllSlides(hpictures, vpictures):
    slideShow = hpictures
    for i in range(0, len(vpictures), 2):  # TODO: Randomize
        slideShow.append([vpictures[i][0] + " " + vpictures[i + 1][0]] + vpictures[i][1:] + vpictures[i + 1][1:])
    return slideShow


'''
def createSlide(*args):
    # Const
    l = len(args)
    if l == 1:
        return [args[0]]
    elif l == 2 and args[0][0] == "V" and args[1][0] == "V":
        return [args[0], args[1]]
    else:
        return None
'''


def totalInterest(slideShow):
    total = 0
    for i in range(0, len(slideShow) - 1, 1):
        total += interest(slideShow[i], slideShow[i + 1])
    return total


# def totalInterest(matrix):
#     total = 0
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             if i < j:
#                 total += matrix[i][j]
#     return total

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
    print(createAllSlides(hpictures, vpictures))

    print(interest(hpictures[0], hpictures[1]))
    print(getEdges(createAllSlides(hpictures, vpictures)))


if __name__ == "__main__":
    main()
