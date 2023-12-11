from itertools import combinations
from SpaceHelper import SpaceImage, distance

file = open('Input.txt', 'r')
input = file.read()

image = SpaceImage(input)
image.expandSpace()
galaxyPairs = combinations(image.getGalaxies(),2)
output = sum([distance(p[0], p[1]) for p in galaxyPairs])
print(output)