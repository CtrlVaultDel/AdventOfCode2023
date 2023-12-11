from queue import Queue
from MazeUtils import Grid, Pos

file = open('Input.txt', 'r')
input = file.read()

grid = Grid(input)
q = Queue()
visited = []
for y in range(grid.y_max):
    for x in range(grid.x_max):
        curr = Pos(x, y)
        if grid.at(curr) == 'S':
            visited.append(curr)
            q.put((curr, 0))
#Breadth-first search of maze space "tree" with 'S' as the root node
while not q.empty():
    p, d = q.get()
    if not grid.ground(p) and all([n in visited for n in grid.neighbors(p)]):
        break
    for n in grid.neighbors(p):
        if n not in visited:
            visited.append(n)
            q.put((n, d+1))
c = 0
for y in range(grid.y_max):
    out = True
    for x in range(grid.x_max):
        curr = Pos(x,y)
        orig = grid.at(curr)
        #Because 'S' can replace one of "F7|", it's possible that the below will return a Containment Error for your input
        #If printed row contains 'S', add 'S' to the string, making it "F7|S" and run again
        if (curr in visited) and (orig in "F7|"):
            out = not out
        if not out and curr not in visited:
            c += 1
            grid.set(curr, 'I')
        if out:
            grid.set(curr, 'O')
        if curr in visited:
            grid.set(curr, ' ')
    if not out:
        print(grid.grid[y]) 
        print("Containment Error")
        exit(-1)
print(c)