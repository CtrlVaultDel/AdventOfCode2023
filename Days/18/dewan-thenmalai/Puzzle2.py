import re
import numpy as np

file = open('Input.txt', 'r')
input = file.read()
lines = input.split('\n')

def det(mat):
    #had a minor issue with onverflow, so I'm hard converting to python ints, which have arbitrary precision
    return int(mat[0][0])*int(mat[1][1]) - int(mat[0][1])*int(mat[1][0])

#Gauss' theorem allows you to calculate the area of a polygon using the coordinates of consecutive vertices by summing the terms (u1v2-u2v1)/2. This is done by stacking the vertices as a 2x2 matrix and taking the determinant.
def area(vertices):
    triangle = []
    for i in range(len(vertices)-1):
        mat = np.column_stack(vertices[i:i+2])
        triangle.append(det(mat)/2)
    return sum(triangle)

dirs = {
        '3': np.asarray([0,-1]),
        '1': np.asarray([0,1]),
        '2': np.asarray([-1,0]),
        '0': np.asarray([1,0])
       }

current = np.asarray([0,0])
verts = [current]
dists = []

regEx = re.compile(r"(U|D|L|R) (\d+) \(#([0-9a-f]{6})\)")

for line in lines:
    _, _, hex = regEx.match(line).groups()
    dist = int(hex[0:5],16)
    dir = hex[5]
    dists.append(int(dist))
    current = current+(int(dist)*dirs[dir])
    verts.append(current)

if (current != np.asarray([0,0])).all():
    print("Invalid polygon")
    exit(-1)

#Unfortunately, the area formula doesn't quite work, because the coordinate system is defined by the centers of the edge squares. This requires us to add a correction term. It turns out that half the sum of the distances of each segment is one less than the term, which can be demonstrated by showing that positively winding corners undercount by 1/4 and negatively winding corners overcount by 1/4, then showing that there must be 4 more positively winding corners than negatively winding ones.
print(area(verts)+(sum(dists)/2)+1)