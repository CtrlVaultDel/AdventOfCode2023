import math
import re

file = open('Input.txt', 'r')

input = file.read()

lines = input.split('\n')

numberRegex = r'[0-9]+'

cardCounts = [1] * len(lines)

for i in range(len(lines)):
    line = lines[i]
    numbers = line.split(':')[1]
    splitNumbers = numbers.split('|')
    winners = re.findall(numberRegex, splitNumbers[0])
    draw = re.findall(numberRegex, splitNumbers[1])
    matches = [(x in winners) for x in draw]
    winCount = matches.count(True)
    for j in range(1, winCount + 1):
        cardCounts[i + j] += 1 * cardCounts[i]
    
print(sum(cardCounts))