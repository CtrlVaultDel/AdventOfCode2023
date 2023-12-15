def HASH(s):
    cur = 0
    for c in s:
        cur += ord(c)
        cur *= 17
        cur %= 256
    return cur

file = open('Input.txt', 'r')
input = file.read()
seqs = input.split(',')

hashes = []
for s in seqs:
    hashes.append(HASH(s))

print(sum(hashes))