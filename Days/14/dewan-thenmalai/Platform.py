from enum import Enum

class Dir(Enum):
    NORTH = 0
    SOUTH = 1
    EAST = 2
    WEST = 3

class Platform:
    def __init__(self, input):
        self.grid = [[c for c in l] for l in input.split()]
        self.x_max = len(self.grid[0])
        self.y_max = len(self.grid)
        
    def __str__(self):
        return '\n'.join(''.join(l) for l in self.grid)
    
    def tiltPlatform(self, dir):
        match dir:
            case Dir.NORTH:
                for x in range(self.x_max):
                    empty = 0
                    for y in range(self.y_max):
                        match self.grid[y][x]:
                            case 'O':
                                self.grid[y][x] = '.'
                                self.grid[empty][x] = 'O'
                                empty += 1
                            case '#':
                                empty = y+1
            case Dir.SOUTH:
                for x in range(self.x_max):
                    empty = self.y_max-1
                    for y in reversed(range(self.y_max)):
                        match self.grid[y][x]:
                            case 'O':
                                self.grid[y][x] = '.'
                                self.grid[empty][x] = 'O'
                                empty -= 1
                            case '#':
                                empty = y-1
            case Dir.WEST:
                for y in range(self.y_max):
                    empty = 0
                    for x in range(self.x_max):
                        match self.grid[y][x]:
                            case 'O':
                                self.grid[y][x] = '.'
                                self.grid[y][empty] = 'O'
                                empty += 1
                            case '#':
                                empty = x+1
            case Dir.EAST:
                for y in range(self.y_max):
                    empty = self.x_max-1
                    for x in reversed(range(self.x_max)):
                        match self.grid[y][x]:
                            case 'O':
                                self.grid[y][x] = '.'
                                self.grid[y][empty] = 'O'
                                empty -= 1
                            case '#':
                                empty = x-1
    
    def calcLoad(self, dir):
        match dir:
            case Dir.NORTH:
                return sum([l.count('O')*(self.y_max-y) for y,l in enumerate(self.grid)])