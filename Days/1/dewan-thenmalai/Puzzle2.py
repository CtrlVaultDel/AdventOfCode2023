import re

file = open('Input1.txt', 'r')

input = file.read()

lines = input.split('\n')
lineNum = 0;

output = []

stringToInt = {
    "0": '0',
    "1": '1',
    "2": '2',
    "3": '3',
    "4": '4',
    "5": '5',
    "6": '6',
    "7": '7',
    "8": '8',
    "9": '9',
    "zero": '0',
    "one": '1',
    "two": '2',
    "three": '3',
    "four": '4',
    "five": '5',
    "six": '6',
    "seven": '7',
    "eight": '8',
    "nine": '9'
}

regex = r'(?=([0-9]|one|two|three|four|five|six|seven|eight|nine|zero))'

for line in lines:
    matches = re.findall(regex, line)
    if len(matches) == 0:
        print(f'Error matching input line {line} at {lineNum}')
        exit(-1)
    else:
        output.append(stringToInt[matches[0]] + stringToInt[matches[-1]])
    lineNum += 1
    
sum = sum(list(map(int, output)))

print(sum)