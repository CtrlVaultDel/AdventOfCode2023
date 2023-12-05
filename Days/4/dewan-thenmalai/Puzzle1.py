import math
import re

file = open('Input.txt', 'r')

input = file.read()

lines = input.split('\n')

numberRegex = r'[0-9]+'

scores = []

for line in lines:
    numbers = line.split(':')[1]
    splitNumbers = numbers.split('|')
    winners = re.findall(numberRegex, splitNumbers[0])
    draw = re.findall(numberRegex, splitNumbers[1])
    matches = [(x in winners) for x in draw]
    score = math.floor(2**(matches.count(True)-1))
    scores.append(score)

print(sum(scores))