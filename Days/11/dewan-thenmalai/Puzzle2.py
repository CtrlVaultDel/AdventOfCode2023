from itertools import combinations
from SpaceHelper import SpaceImage, distance

def getRange(a,b):
    if b >= a:
        return range(a,b)
    else:
        return range(b,a)

file = open('Input.txt', 'r')
input = file.read()

FACTOR = 1000000
EXPANSION = FACTOR - 1

image = SpaceImage(input)
emptyRows = [i for i in range(image.y_max) if image._isEmptyRow(i)]
emptyCols = [j for j in range(image.x_max) if image._isEmptyCol(j)]
galaxyPairs = combinations(image.getGalaxies(),2)

output = []
for p in galaxyPairs:
    naiveDistance = distance(p[0],p[1])
    expandedDistance = naiveDistance + EXPANSION*len([i for i in emptyRows if i in getRange(p[0].y, p[1].y)]) + EXPANSION*len([j for j in emptyCols if j in getRange(p[0].x, p[1].x)])
    output.append(expandedDistance)

print(sum(output))
