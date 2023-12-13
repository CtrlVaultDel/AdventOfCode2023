file = open('Input.txt', 'r')
input = file.read()
grids = input.split('\n\n')

# reflect grid over a vertical line
def flipVertical(grid):
    return [''.join(r[::-1]) for r in grid]

# reflect grid over a horizontal line
def flipHorizontal(grid):
    return grid[::-1]

# the below 2 methods run the same algorithm along different axes
# it works by "folding" the grid at a location and checking if the overlapping sections are equal
    # loop over all possible fold locations, which range from (0,1) to (len(axis)-2,len(axis)-1), done by looping a single variable, "i " from 1 to len(axis)-1
    # reflect the first i rows/cols of the grid
    # take the minimum of the length of the reflected portion and the length of the remaining unreflected grid, "a"
    # compare the first a rows/cols of the reflected portion and the unreflected portion
    # if it matches, we have the right location

def checkVerticalReflections(grid):
    for i in [i+1 for i in range(len(grid[0])-1)]:
        reflection = flipVertical([''.join(r[:i]) for r in grid])
        a = min(i, len(grid[0])-i)
        if [''.join(r[:a]) for r in reflection] == [''.join(r[i:i+a]) for r in grid]:
            return i
    return 0

def checkHorizontalReflections(grid):
    for i in [i+1 for i in range(len(grid)-1)]:
        reflection = flipHorizontal(grid[:i])
        a = min(i, len(grid)-i)
        if reflection[:a] == grid[i:i+a]:
            return 100*i
    return 0

summaries = []
for item in grids:
    grid = item.split('\n')
    summaries.append(checkVerticalReflections(grid))
    summaries.append(checkHorizontalReflections(grid))

print(sum(summaries))