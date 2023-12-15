from collections import OrderedDict

def HASH(s):
    #return sum([(ord(c)*17)%256 for c in s])
    cur = 0
    for c in s:
        cur += ord(c)
        cur *= 17
        cur %= 256
    return cur

def HASHMAP(s, boxes):
    if '=' in s:
        label, flen = s.split('=')
        box = HASH(label)
        boxes[box][label] = flen
    elif '-' in s:
        label = s.split('-')[0]
        box = HASH(label)
        boxes[box].pop(label, None)

file = open('Input.txt', 'r')
input = file.read()
seqs = input.split(',')

boxes = [OrderedDict() for i in range(256)]
for s in seqs:
    HASHMAP(s,boxes)

print(sum([sum([(n+1)*(i+1)*int(b[l]) for i,l in enumerate(b)]) for n,b in enumerate(boxes)]))
