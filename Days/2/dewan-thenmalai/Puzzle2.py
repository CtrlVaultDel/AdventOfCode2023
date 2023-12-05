import re

file = open('Input.txt', 'r')

input = file.read()

lines = input.split('\n')

div = [i.split(':') for i in lines]

games = [i[1].split(';') for i in div]

regex = r'([0-9]+) (red|blue|green)'

output = []

for i in range(len(games)):
    minColor = {
        "red": 0,
        "green": 0,
        "blue": 0
    }
    matches = [re.findall(regex, round) for round in games[i]]
    for draw in matches:
        for color in draw:
            if int(color[0]) > minColor[color[1]]:
                minColor[color[1]] = int(color[0])
    power = minColor["red"] * minColor["blue"] * minColor["green"]
    output.append(power)

print(sum(output))