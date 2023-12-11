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
        print(f"max distance: {d+1}")
        break
    for n in grid.neighbors(p):
        if n not in visited:
            visited.append(n)
            q.put((n, d+1))
