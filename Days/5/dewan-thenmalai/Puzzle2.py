import re
import concurrent.futures

def reverseMap(inStr, maps):
    input = int(inStr)
    for map in maps:
        elements = [int(x) for x in  map.split(' ')]
        if input >= elements[0] and input < elements[0]+elements[2]:
            retVal = elements[1] + (input - elements[0])
            return str(retVal)
    return inStr

file = open('Input.txt', 'r')

input = file.read()

lines = input.split('\n')

max_threads = 4

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

locations = []

for match in matches:
    lines = match[0].split('\n')
    maps[lines[0]] = lines[1:]

i = 0
while(True):
    print(f"Checking location {i}")
    humidity = reverseMap(str(i), maps["humidity-to-location map:"])
    temperature = reverseMap(humidity, maps["temperature-to-humidity map:"])
    light = reverseMap(temperature, maps["light-to-temperature map:"])
    water = reverseMap(light, maps["water-to-light map:"])
    fertilizer = reverseMap(water, maps["fertilizer-to-water map:"])
    soil = reverseMap(fertilizer, maps["soil-to-fertilizer map:"])
    seed = reverseMap(fertilizer, maps["seed-to-soil map:"])
    
    seedInt = int(seed)
    for set in seedSets:
        if seedInt >= int(set[0]) and seedInt < int(set[0])+int(set[1]):
            print(f"Smallest location is {i}")
            exit(0)
    
    i += 1