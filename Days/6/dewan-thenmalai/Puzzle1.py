import math
import numpy as np

def solveQuadratic(t, d):
    a = -1
    b = float(t)
    c = -float(d)-0.01 #correction term to prevent exact roots
    x1 = (-b+math.sqrt((b**2)-(4*a*c)))/(2*a)
    x2 = (-b-math.sqrt((b**2)-(4*a*c)))/(2*a)
    return (x1, x2)

def getRange(t1, t2):
    return

file = open('Input.txt', 'r')

input = file.read()

lines = input.split('\n')

times = lines[0].split(':')[1].split()
distances = lines[1].split(':')[1].split()

races = list(zip(times, distances))
winners = []

for race in races:
    t1, t2 = solveQuadratic(race[0], race[1])
    range = abs(math.floor(t1) - math.floor(t2))
    winners.append(range)

print(np.prod(winners))