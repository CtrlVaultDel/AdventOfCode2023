import re
import math
from itertools import cycle

file = open('Input.txt', 'r')
input = file.read()
lines = input.split('\n')

directions = {"L": 0, "R": 1}

lines = input.split('\n')
instructions = lines[0]
mapLines = lines[2:]

nodes = {l.split('=')[0].strip(): re.match(r"\((\w{3}), (\w{3})\)", l.split('=')[1].strip()).groups() for l in mapLines}

pool = cycle([c for c in instructions])

steps = 0
locations = [x for x in nodes.keys() if x[2] == 'A']
cycles = {}

for instr in pool:
    locations = [nodes[l][directions[instr]] for l in locations]
    steps += 1
    for l in locations:
        if l[2] == 'Z':
            cycles[l] = steps
    if len(cycles.values()) == 6:
        break

output = math.lcm(*cycles.values())
print(output)