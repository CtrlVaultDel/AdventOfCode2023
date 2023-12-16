from collections import defaultdict
from enum import Enum

class Dir(Enum):
    UP = 0
    DOWN = 1
    RIGHT = 2
    LEFT = 3

class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x},{self.y})"
    
    def __eq__(self, other):
        if type(self) == type(other):
            return self.x == other.x and self.y == other.y
        return False
    
    def __hash__(self):
        return hash((self.x,self.y))
    
    def isValid(self, x_max, y_max):
        return self.x >= 0 and self.x < x_max and self.y >= 0 and self.y < y_max
    
    def up(self):
        return Pos(self.x, self.y-1)
        
    def down(self):
        return Pos(self.x, self.y+1)
    
    def right(self):
        return Pos(self.x+1, self.y)
    
    def left(self):
        return Pos(self.x-1, self.y)

class MirrorGrid:
    def __init__(self, input):
        self.grid = [[c for c in l] for l in input.split('\n')]
        self.y_max = len(self.grid)
        self.x_max = len(self.grid[0])
    
    def at(self, pos):
        try:
            return self.grid[pos.y][pos.x]
        except IndexError:
            print(pos)
    
    def get(self, pos, dir):
        next = pos
        match dir:
            case Dir.UP:
                next = pos.up()
            case Dir.DOWN:
                next = pos.down()
            case Dir.LEFT:
                next = pos.left()
            case Dir.RIGHT:
                next = pos.right()
        if pos.isValid(self.x_max, self.y_max):
            return next
        return None
    
    #dir is the direction of travel of the light, e.g. a beam that moves from left to right is represented by Dir.RIGHT
    def reflect(self, mirror, dir):
        match (mirror, dir):
            case ('\\', Dir.LEFT) | ('/', Dir.RIGHT):
                return Dir.UP
            case ('\\', Dir.RIGHT) | ('/', Dir.LEFT):
                return Dir.DOWN
            case ('\\', Dir.UP) | ('/', Dir.DOWN):
                return Dir.LEFT
            case ('\\', Dir.DOWN) | ('/', Dir.UP):
                return Dir.RIGHT
    
    #dir is the direction of travel of the light, e.g. a beam that moves from left to right is represented by Dir.RIGHT
    def split(self, split, dir):
        match (split, dir):
            case ('|', Dir.LEFT) | ('|', Dir.RIGHT):
                return [Dir.UP, Dir.DOWN]
            case ('-', Dir.UP) | ('-', Dir.DOWN):
                return [Dir.LEFT, dir.RIGHT]
            case ('-', Dir.LEFT) | ('-', Dir.RIGHT) | ('|', Dir.UP) | ('|', Dir.DOWN):
                return [dir]
    
    def calcEnergized(self, start, dir):
        #these need to be globals so that recursive calls are checking the same lists
        visited = defaultdict(int)
        loopCheck = set()
        
        #Because splitters produce 2 output beams, a simple loop is insufficient. By defining this local function I can recursively call it for each beam split.
        def loopGrid(pos, dir):
            while pos:
                #I had this weird bug where I'd get positions that weren't valid, so I need to do an explicit check here
                if (pos,dir) in loopCheck or not pos.isValid(self.x_max, self.y_max):
                    break
                visited[pos] += 1
                loopCheck.add((pos,dir))
                match self.at(pos):
                    case '.':
                        pos = self.get(pos, dir)
                    case '\\' | '/' as mirror:
                        dir = self.reflect(mirror, dir)
                        pos = self.get(pos, dir)
                    case '|' | '-' as splitter:
                        dirs = self.split(splitter, dir)
                        if(len(dirs) == 2):
                            loopGrid(self.get(pos,dirs[0]), dirs[0])
                            loopGrid(self.get(pos,dirs[1]), dirs[1])
                        else:
                            dir = dirs[0]
                            pos = self.get(pos, dir)
        
        loopGrid(start, dir)
        return len(visited)