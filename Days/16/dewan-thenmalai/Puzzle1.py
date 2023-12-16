from collections import defaultdict
from MirrorHelper import MirrorGrid, Pos, Dir

file = open('Input.txt', 'r')
input = file.read()

mirrors = MirrorGrid(input)
start = Pos(0,0)
print(mirrors.calcEnergized(start, Dir.RIGHT))