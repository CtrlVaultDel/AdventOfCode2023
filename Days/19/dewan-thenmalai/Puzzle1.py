import re

class Rule:
    def __init__(self, comp, dest):
        self.comp = comp
        self.dest = dest
    
    def __str__(self):
        return f"{self.comp}:{self.dest}"

file = open('Input.txt', 'r')
input = file.read()
rulesInput, partsInput = input.split('\n\n')

ratingsRegex = re.compile(r"{x=(\d+),m=(\d+),a=(\d+),s=(\d+)}")
parts = [{'x':int(x),'m':int(m),'a':int(a),'s':int(s)} for x,m,a,s in [ratingsRegex.match(l).groups() for l in partsInput.split('\n')]]

ruleNameRegex = re.compile(r"(\w+){") #extract group(0)
branchesRegex = re.compile(r"((x|m|a|s)(<|>)(\d+)):(\w+),") #use findall and get group(0) and group(4) for each match
finalRegex = re.compile(r"(\w+)}") #extarct group(0)
rules = {ruleNameRegex.match(r).group(1): [Rule(m[0],m[4]) for m in branchesRegex.findall(r)] + [Rule(None,finalRegex.search(r).group(1))] for r in rulesInput.split('\n')}

approved = []
for p in parts:
    x,m,a,s = p.values()
    rule = "in"
    while rule != "A" and rule != "R":
        for b in rules[rule]:
            if b.comp is None or eval(b.comp):
                rule = b.dest
                break
    if rule == "A":
        approved.append(sum([x,m,a,s]))

print(sum(approved))