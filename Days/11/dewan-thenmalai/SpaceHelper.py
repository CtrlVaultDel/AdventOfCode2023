class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x},{self.y})"

def distance(pos1, pos2):
    return abs(pos1.x-pos2.x)+abs(pos1.y-pos2.y)

class SpaceImage:
    def __init__(self, text):
        self.grid = [[c for c in l] for l in text.split('\n')]
        self.y_max = len(self.grid)
        self.x_max = len(self.grid[0])
    
    def __str__(self):
        return '\n'.join([''.join(r) for r in self.grid])
    
    def _isEmptyRow(self, row):
        return all([c == '.' for c in self.grid[row]])
    
    def _isEmptyCol(self, col):
        return all([c == '.' for c in [row[col] for row in self.grid]])
    
    def _insertEmptyRow(self, row):
        self.grid.insert(row, ['.' for i in range(self.x_max)])
    
    def _insertEmptyCol(self, col):
        for r in self.grid:
            r.insert(col, '.')
    
    def expandSpace(self):
        emptyRows = [i for i in range(self.y_max) if self._isEmptyRow(i)]
        emptyCols = [j for j in range(self.x_max) if self._isEmptyCol(j)]
        for r in sorted(emptyRows,reverse=True):
            self._insertEmptyRow(r)
        for c in sorted(emptyCols,reverse=True):
            self._insertEmptyCol(c)
        self.y_max = len(self.grid)
        self.x_max = len(self.grid[0])
    
    def getGalaxies(self):
        return [Pos(x,y) for x in range(self.x_max) for y in range(self.y_max) if self.grid[y][x] == '#']