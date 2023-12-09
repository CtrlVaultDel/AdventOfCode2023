import re
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
location = "AAA"
for instr in pool:
    location = nodes[location][directions[instr]]
    steps += 1
    if location == "ZZZ":
        break;

print(steps)