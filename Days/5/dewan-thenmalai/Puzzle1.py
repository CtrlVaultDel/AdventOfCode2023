import math
import re

def mapInput(inStr, maps):
    input = int(inStr)
    for map in maps:
        elements = [int(x) for x in  map.split(' ')]
        if input in range(elements[1], elements[1]+elements[2]):
            retVal = elements[0] + (input - elements[1])
            return str(retVal)
    return inStr

file = open('Input.txt', 'r')

input = file.read()

lines = input.split('\n')

seedLine = lines[0]
seeds = seedLine.split(':')[1].strip().split(' ')

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

for seed in seeds:
    soil = mapInput(seed, maps["seed-to-soil map:"])
    fertilizer = mapInput(soil, maps["soil-to-fertilizer map:"])
    water = mapInput(fertilizer, maps["fertilizer-to-water map:"])
    light = mapInput(water, maps["water-to-light map:"])
    temperature = mapInput(light, maps["light-to-temperature map:"])
    humidity = mapInput(temperature, maps["temperature-to-humidity map:"])
    location = mapInput(humidity, maps["humidity-to-location map:"])
    locations.append(int(location))

print(min(locations))