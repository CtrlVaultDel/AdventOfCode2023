from itertools import chain

file = open('Input.txt', 'r')
input = file.read()
grids = input.split('\n\n')

# extract a single string from arbitrarily nested lists of strings
def collapse(l):
    return ''.join(chain.from_iterable(l))

# check if 2 grids differ by exactly 1 character
def smudgeEqual(a,b):
    count = 0
    for i,j in zip(collapse(a),collapse(b)):
        count += (i != j)
        if count > 1:
            return False
    if count == 1:
        return True
    return False

def flipVertical(grid):
    return [''.join(r[::-1]) for r in grid]

def flipHorizontal(grid):
    return grid[::-1]

def checkVerticalReflections(grid):
    for i in [i+1 for i in range(len(grid[0])-1)]:
        reflection = flipVertical([''.join(r[:i]) for r in grid])
        a = min(i, len(grid[0])-i)
        if smudgeEqual([''.join(r[:a]) for r in reflection],[''.join(r[i:i+a]) for r in grid]):
            return i
    return 0

def checkHorizontalReflections(grid):
    for i in [i+1 for i in range(len(grid)-1)]:
        reflection = flipHorizontal(grid[:i])
        a = min(i, len(grid)-i)
        if smudgeEqual(reflection[:a],grid[i:i+a]):
            return 100*i
    return 0

summaries = []
for item in grids:
    grid = item.split('\n')
    summaries.append(checkVerticalReflections(grid))
    summaries.append(checkHorizontalReflections(grid))

print(sum(summaries))