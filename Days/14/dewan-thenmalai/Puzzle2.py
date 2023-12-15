from Platform import Platform, Dir

file = open('Input.txt', 'r')
input = file.read()

CYCLES = 1000000000

seenList = []
cycleLoop = []
plat = Platform(input)
for currentCycle in range(1,CYCLES):
    plat.tiltPlatform(Dir.NORTH)
    plat.tiltPlatform(Dir.WEST)
    plat.tiltPlatform(Dir.SOUTH)
    plat.tiltPlatform(Dir.EAST)
    if str(plat) in seenList:
        i = seenList.index(str(plat))
        cycleLoop = seenList[i:]
        remainingCycles = CYCLES - currentCycle
        index = remainingCycles % len(cycleLoop)
        plat = Platform(cycleLoop[index])
        break
    seenList.append(str(plat))

print(plat.calcLoad(Dir.NORTH))