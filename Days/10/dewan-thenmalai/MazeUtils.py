from enum import Enum

#Enumeration of directions that can be moved
class Dir(Enum):
    NORTH = 0
    SOUTH = 1
    EAST = 2
    WEST = 3
    
    def invert(self):
        match self:
            case Dir.NORTH:
                return Dir.SOUTH
            case Dir.SOUTH:
                return Dir.NORTH
            case Dir.EAST:
                return Dir.WEST
            case Dir.WEST:
                return Dir.EAST

#This helper functions determines if a given symbol allows you to move in that direction
def opens(sym, dir):
    match(sym, dir):
        case ['S', _] | ['|', (Dir.NORTH | Dir.SOUTH)] | ['-', (Dir.EAST | Dir.WEST)] | ['L', (Dir.NORTH | Dir.EAST)] | ['J', (Dir.NORTH | Dir.WEST)] | ['7', (Dir.SOUTH | Dir.WEST)] | ['F', (Dir.SOUTH | Dir.EAST)]:
            return True
    return False

#Coordinate class that can get adjacent spaces
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
    
    def isValid(self, x_max, y_max):
        return self.x >= 0 and self.x < x_max and self.y >= 0 and self.y < y_max
    
    def north(self):
        return Pos(self.x, self.y-1)
        
    def south(self):
        return Pos(self.x, self.y+1)
    
    def east(self):
        return Pos(self.x+1, self.y)
    
    def west(self):
        return Pos(self.x-1, self.y)

#Manage Grid and its elements
class Grid:
    def __init__(self, text):
        self.grid = [[c for c in l] for l in text.split()]
        self.x_max = len(self.grid[0])
        self.y_max = len(self.grid)
    
    def at(self, pos):
        return self.grid[pos.y][pos.x]
    
    def ground(self, pos):
        return self.at(pos) == '.'
    
    def set(self, pos, c):
        self.grid[pos.y][pos.x] = c
    
    def get(self, pos, dir):
        next = pos
        match dir:
            case Dir.NORTH:
                next = pos.north()
            case Dir.SOUTH:
                next = pos.south()
            case Dir.EAST:
                next = pos.east()
            case Dir.WEST:
                next = pos.west()
        if pos.isValid(self.x_max, self.y_max):
            return next
        return None
    
    #Checks if you can move from the given position to each adjacent space, then if that adjacent space can move in the opposite direction, i.e. back to the given position
    #If both are true then that is a valid passage
    def neighbors(self, pos):
        return [self.get(pos, d) for d in Dir if opens(self.at(pos), d) and opens(self.at(self.get(pos, d)), d.invert())]
