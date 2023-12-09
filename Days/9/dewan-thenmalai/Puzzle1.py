import numpy as np
from math import comb

def GregoryNewton(sequence):
    curSeq = sequence
    differences = [sequence]
    while not all([i == 0 for i in curSeq]):
        curSeq = np.diff(curSeq)
        differences.append(curSeq)
    coefficients = [x[0] for x in differences]
    terms = [c*comb(len(sequence), i) for i,c in enumerate(coefficients)]
    return sum(terms)
    

file = open('Input.txt', 'r')
input = file.read()
lines = input.split('\n')

predictions = []

for line in lines:
    sequence = [int(i) for i in line.split()]
    predictions.append(GregoryNewton(sequence))

print(sum(predictions))