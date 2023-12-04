import re 

file = open('Input.txt', 'r')

input = file.read()

lines = input.split('\n')

numberRegex = r'[0-9]+'
numExp = re.compile(numberRegex)

gearRegex = r'\*'
gearExp = re.compile(gearRegex)

numMatches = []
gearMatches = []

gearRatios = []

for i, line in enumerate(lines):
    numIterator = numExp.finditer(line)
    numMatches.append([(m.group(0), i, m.span()) for m in numIterator])
    gearIterator = gearExp.finditer(line)
    gearMatches.append([m.start() for m in gearIterator])

for i in range(len(lines)):
    for idx in gearMatches[i]:
        gearConnections = []
        curLine = list(filter(lambda x: (idx >= x[2][0] - 1 and idx <= x[2][1]), numMatches[i]))
        prevLine = []
        nextLine = []
        if(idx > 0):
            prevLine = list(filter(lambda x: (idx >= x[2][0] - 1 and idx <= x[2][1]), numMatches[i-1]))
        if idx < len(lines) - 1:
            nextLine = list(filter(lambda x: (idx >= x[2][0] - 1 and idx <= x[2][1]), numMatches[i+1]))
        gearConnections.append(prevLine)
        gearConnections.append(curLine)
        gearConnections.append(nextLine)
        flatGearConnections = [item for sublist in gearConnections for item in sublist]
        if(len(flatGearConnections) == 2):
            gearRatios.append(int(flatGearConnections[0][0])*int(flatGearConnections[1][0]))
            #print(flatGearConnections)

print(sum(gearRatios))