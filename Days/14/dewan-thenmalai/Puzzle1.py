from Platform import Platform, Dir

file = open('Input.txt', 'r')
input = file.read()

plat = Platform(input)
plat.tiltPlatform(Dir.NORTH)
print(plat.calcLoad(Dir.NORTH))