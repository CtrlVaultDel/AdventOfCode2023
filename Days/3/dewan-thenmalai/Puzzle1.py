import re 

file = open('Input.txt', 'r')

input = file.read()

lines = input.split('\n')

numberRegex = r'[0-9]+'
numExp = re.compile(numberRegex)

symbolRegex = r'[^0-9.\n]'
symExp = re.compile(symbolRegex)

numMatches = []
symMatches = []

partNos = []

for i, line in enumerate(lines):
    numIterator = numExp.finditer(line)
    numMatches.append([(m.group(0), i, m.span()) for m in numIterator])
    symIterator = symExp.finditer(line)
    symMatches.append([m.start() for m in symIterator])

partNoMatches = []
for i in range(len(lines)):
    for idx in symMatches[i]:
        curLine = list(filter(lambda x: (idx >= x[2][0] - 1 and idx <= x[2][1]), numMatches[i]))
        prevLine = []
        nextLine = []
        if(idx > 0):
            prevLine = list(filter(lambda x: (idx >= x[2][0] - 1 and idx <= x[2][1]), numMatches[i-1]))
        if idx < len(lines) - 1:
            nextLine = list(filter(lambda x: (idx >= x[2][0] - 1 and idx <= x[2][1]), numMatches[i+1]))
        partNoMatches.append(prevLine)
        partNoMatches.append(curLine)
        partNoMatches.append(nextLine)
    #print(partNoMatches)

flatPartNoMatches = [item for sublist in partNoMatches for item in sublist]
#print(flatPartNoMatches)
partNos = [int(x[0]) for x in flatPartNoMatches]

#print(partNos)
output = sum(partNos)
print(output)