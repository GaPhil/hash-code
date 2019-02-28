import os, random

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
        picture[0] = i  # Line number
        orientation = line[0]
        numTags = line[1]
        line = line[2:]
        for tag in line:
            picture.append(tag.strip())
        if (orientation == "H"):
            if (numTags == "0"):  # skip
                continue
            picture[0] = [picture[0], str(picture[0])]
            hpictures.append(picture)
        else:
            vpictures.append(picture)

    return [hpictures, vpictures]


def createAllSlides(hpictures, vpictures):
    slideShow = hpictures
    random.sample(vpictures, len(vpictures))
    for i in range(0, len(vpictures), 2):  # TODO: Randomize
        tags = list(set(vpictures[i][1:]).union(set(vpictures[i + 1][1:])))
        slideShow.append([[vpictures[i][0], str(vpictures[i][0]) + " " + str(vpictures[i + 1][0])]] + tags)
    return slideShow


def totalInterest(slideShow):
    total = 0
    for i in range(0, len(slideShow) - 1, 1):
        total += interest(slideShow[i], slideShow[i + 1])
    return total


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


def submitAnswer(slideshow):
    l = str(len(slideshow))
    answers = [s[0][1] for s in slideshow]
    out = "\n".join([l] + answers)
    return out


def main():
    a = "a_example.txt"
    b = "b_lovely_landscapes.txt"
    c = "c_memorable_moments.txt"
    d = "d_pet_pictures.txt"
    e = "e_shiny_selfies.txt"
    datasetPath = os.path.join(DatasetFolder, e)
    [hpictures, vpictures] = parse(datasetPath)
    slideshow = createAllSlides(hpictures, vpictures)

    max = -1
    best = slideshow
    l = len(slideshow)
    for i in range(10):
        slideshow = createAllSlides(hpictures, vpictures)
        newSlideShow = random.sample(slideshow, l)
        new = totalInterest(newSlideShow)
        if new > max:
            max = new
            best = newSlideShow
        print(max)
    out = submitAnswer(best)
    print(out)

    with open("out.txt", "w") as f:
        f.write(out)


if __name__ == "__main__":
    main()
