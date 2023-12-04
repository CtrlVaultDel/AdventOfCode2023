import re

file = open('Input.txt', 'r')

input = file.read()

cubes = {
    "red": 12,
    "green": 13,
    "blue": 14
}

lines = input.split('\n')

div = [i.split(':') for i in lines]

games = [i[1].split(';') for i in div]

regex = r'([0-9]+) (red|blue|green)'

sum = 0

for i in range(len(games)):
    valid = True
    matches = [re.findall(regex, round) for round in games[i]]
    for draw in matches:
        for color in draw:
            if int(color[0]) > cubes[color[1]]:
                valid = False
    if(valid):
        sum += i+1

print(sum)