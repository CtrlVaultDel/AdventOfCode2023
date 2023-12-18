file = open('Input.txt', 'r')
input = file.read()

def tupAdd(a,b):
    return (a[0]+b[0],a[1]+b[1])

#pretty straightforward Dijkstra's implementation
#only cabeat is that we have to explicitly check for travel direction and chain counts
def calcMinLoss(input):
    grid = {(i,j):int(c) for j,l in enumerate(input.split('\n')) for i,c in enumerate(l)}
    x_max,y_max = len(input.split('\n')[0]),len(input.split('\n'))
    #dirs is organized such that adding or subtracting 1 is equivalent to turning left or right
    dirs = [(1,0),(0,-1),(-1,0),(0,1)]
    
    #heap is a list of tuples containing a cost, positiontuple , and tuple containing the travel direction and "straight line" length
    #visited is similar, except without the cost
    heap = [(0,(0,0),(0,0))]
    visited = {((0,0),(0,0))}
    
    while heap:
        cost, pos, dirChain = min(heap, key=lambda x: x[0])
        heap.remove((cost,pos,dirChain))
        for turn in range(-1,2):
            if turn == 0:
                if dirChain[1] == 10: continue
                else: chain = dirChain[1] + 1
            else:
                chain = 1
                if dirChain[1] < 4: continue
            newDir = (dirChain[0]+turn)%4
            newPos = tupAdd(pos,dirs[newDir])
            if (newPos in grid) and ((newPos,(newDir,chain)) not in visited):
                newCost = cost + grid[newPos]
                if newPos == (x_max-1,y_max-1) and chain >= 4:
                    return newCost
                visited.add((newPos,(newDir,chain)))
                heap.append((newCost,newPos,(newDir,chain)))

print(calcMinLoss(input))