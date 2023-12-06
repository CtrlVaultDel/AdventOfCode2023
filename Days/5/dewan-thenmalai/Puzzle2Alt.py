import re

def mapInput(inStr, maps):
    input = int(inStr)
    for map in maps:
        elements = [int(x) for x in  map.split(' ')]
        if input >= elements[1] and input < elements[1]+elements[2]:
            retVal = elements[0] + (input - elements[1])
            return str(retVal)
    return inStr

def getSetsFromMaps(maps):
    output = []
    for map in maps:
        vals = map.split(' ')
        output.append([vals[1], vals[2]])
    return output

def getBoundariesFromSets(boundaries, sets):
    for each in sets:
        end = int(each[0]) + int(each[1])
        boundaries.append(each[0])
        boundaries.append(str(end))

def reverseMap(inStr, maps):
    input = int(inStr)
    for map in maps:
        elements = [int(x) for x in  map.split(' ')]
        if input >= elements[0] and input < elements[0]+elements[2]:
            retVal = elements[1] + (input - elements[0])
            return str(retVal)
    return inStr

def getSeedFromLocation(inStr, maps):
    humidity = reverseMap(inStr, maps["humidity-to-location map:"])
    temperature = reverseMap(humidity, maps["temperature-to-humidity map:"])
    light = reverseMap(temperature, maps["light-to-temperature map:"])
    water = reverseMap(light, maps["water-to-light map:"])
    fertilizer = reverseMap(water, maps["fertilizer-to-water map:"])
    soil = reverseMap(fertilizer, maps["soil-to-fertilizer map:"])
    seed = reverseMap(soil, maps["seed-to-soil map:"])
    return seed

def getLocationFromSeed(seed, maps):
    soil = mapInput(seed, maps["seed-to-soil map:"])
    fertilizer = mapInput(soil, maps["soil-to-fertilizer map:"])
    water = mapInput(fertilizer, maps["fertilizer-to-water map:"])
    light = mapInput(water, maps["water-to-light map:"])
    temperature = mapInput(light, maps["light-to-temperature map:"])
    humidity = mapInput(temperature, maps["temperature-to-humidity map:"])
    location = mapInput(humidity, maps["humidity-to-location map:"])
    return location

def inSet(inStr, sets):
    val = int(inStr)
    for set in sets:
        if val >= int(set[0]) and val < int(set[0])+int(set[1]):
            return True
    return False

file = open('Input.txt', 'r')

input = file.read()

lines = input.split('\n')

seedLine = lines[0]
seedRanges = seedLine.split(':')[1].strip().split(' ')
seedSets = [seedRanges[i:i+2] for i in range(0, len(seedRanges), 2)]

numberRegex = r"(?:\n\d+(?:\s+\d+){2})+"

mapLabels = ["seed-to-soil map:",
             "soil-to-fertilizer map:",
             "fertilizer-to-water map:",
             "water-to-light map:",
             "light-to-temperature map:",
             "temperature-to-humidity map:",
             "humidity-to-location map:"]
             
mapRegexes = [label+numberRegex for label in mapLabels]
matches = [re.findall(regex, input) for regex in mapRegexes]
maps = {}

for match in matches:
    lines = match[0].split('\n')
    maps[lines[0]] = lines[1:]

boundaries = []

getBoundariesFromSets(boundaries, seedSets)

soilSets = getSetsFromMaps(maps["seed-to-soil map:"])
getBoundariesFromSets(boundaries, soilSets)
boundaries = [mapInput(x, maps["seed-to-soil map:"]) for x in boundaries]

fertilizerSets = getSetsFromMaps(maps["soil-to-fertilizer map:"])
getBoundariesFromSets(boundaries, fertilizerSets)
boundaries = [mapInput(x, maps["soil-to-fertilizer map:"]) for x in boundaries]

waterSets = getSetsFromMaps(maps["fertilizer-to-water map:"])
getBoundariesFromSets(boundaries, waterSets)
boundaries = [mapInput(x, maps["fertilizer-to-water map:"]) for x in boundaries]

lightSets = getSetsFromMaps(maps["water-to-light map:"])
getBoundariesFromSets(boundaries, lightSets)
boundaries = [mapInput(x, maps["water-to-light map:"]) for x in boundaries]

temperatureSets = getSetsFromMaps(maps["light-to-temperature map:"])
getBoundariesFromSets(boundaries, temperatureSets)
boundaries = [mapInput(x, maps["light-to-temperature map:"]) for x in boundaries]

humiditySets = getSetsFromMaps(maps["temperature-to-humidity map:"])
getBoundariesFromSets(boundaries, humiditySets)
boundaries = [mapInput(x, maps["temperature-to-humidity map:"]) for x in boundaries]

locationSets = getSetsFromMaps(maps["humidity-to-location map:"])
getBoundariesFromSets(boundaries, locationSets)
boundaries = [mapInput(x, maps["humidity-to-location map:"]) for x in boundaries]

seedValues = [getSeedFromLocation(x, maps) for x in boundaries]
validSeeds = list(filter(lambda x: inSet(x, seedSets), seedValues))
validLocations = [int(getLocationFromSeed(x, maps)) for x in validSeeds]
print(min(validLocations))

answerLocation = '56931769'
answerSeed = getSeedFromLocation(answerLocation, maps)