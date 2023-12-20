import re
from itertools import product, starmap
from math import prod

def evalWorkflowHelper(part, rules, rule):
    rv = 0

    for step in rules[rule]:
        #autoflow to next step for last rule
        if ':' not in step:
            rv += evalWorkflow(part, rules, step)
            continue
        condition, nextRule = step.split(':')
        attr = condition[0]
        attrVal = part[attr]
        rel = condition[1]
        val = int(condition[2:])

        #determine if the rule applies 100%
        if (rel == '<' and attrVal[0] < val and attrVal[1] < val) or \
        (rel == '>' and attrVal[0] > val and attrVal[1] > val):
            rv += evalWorkflow(part, rules, nextRule)
            break

        #check if the rule doesn't apply at all
        if (rel == '<' and attrVal[0] >= val and attrVal[1] >= val) or \
        (rel == '>' and attrVal[0] <= val and attrVal[1] <= val):
            continue

        #splitting case
        modifiedPart = part.copy()
        if rel == '<':
            modifiedPart[attr] = (attrVal[0], val - 1)
            part[attr] = (val, attrVal[1])
        else: #rel == '>'
            modifiedPart[attr] = (val + 1, attrVal[1])
            part[attr] = (attrVal[0], val)

        rv += evalWorkflow(modifiedPart, rules, nextRule)
    return rv

def evalWorkflow(part, rules, rule):
    match rule:
        case 'A':
            return (part['x'][1]-part['x'][0]+1) * (part['m'][1]-part['m'][0]+1) * \
                (part['a'][1]-part['a'][0]+1) * (part['s'][1]-part['s'][0]+1)
        case 'R':
            return 0
        case _:
            return evalWorkflowHelper(part, rules, rule)

file = open('Input.txt', 'r')
input = file.read()
rulesInput, partsInput = input.split('\n\n')

xmas = {'x': (1,4000), 'm': (1,4000), 'a': (1,4000), 's': (1,4000)}
rules = {rule[:rule.index('{')] : rule[rule.index('{')+1:-1].split(',') for rule in rulesInput.split('\n')}
print(evalWorkflow(xmas,rules,"in"))