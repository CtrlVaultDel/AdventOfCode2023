import re

file = open('Input1.txt', 'r')

input = file.read()

lines = input.split('\n')
lineNum = 0;

output = []

for line in lines:
    matches = re.findall(r'[0-9]{1}', line)
    if len(matches) == 0:
        print(f'Error matching input line {line} at {lineNum}')
        exit(-1)
    else:
        output.append(matches[0] + matches[-1])
    lineNum += 1
    
sum = sum(list(map(int, output)))

print(sum)