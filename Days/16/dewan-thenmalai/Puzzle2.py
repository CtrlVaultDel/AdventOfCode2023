from collections import defaultdict
from itertools import product
from MirrorHelper import MirrorGrid, Pos, Dir

file = open('Input.txt', 'r')
input = file.read()
mirrors = MirrorGrid(input)
starts = product(range(mirrors.x_max), range(mirrors.y_max))
starts = [Pos(x,y) for x,y in starts]

energizedCounts = []
for s in starts:
    if s.y == 0:
        energizedCounts.append(mirrors.calcEnergized(s, Dir.DOWN))
    elif s.y == mirrors.y_max-1:
        energizedCounts.append(mirrors.calcEnergized(s, Dir.UP))
    if s.x == 0:
        energizedCounts.append(mirrors.calcEnergized(s, Dir.RIGHT))
    elif s.x == mirrors.x_max-1:
        energizedCounts.append(mirrors.calcEnergized(s, Dir.LEFT))

print(max(energizedCounts))