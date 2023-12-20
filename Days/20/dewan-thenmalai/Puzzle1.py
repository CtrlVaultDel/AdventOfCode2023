from collections import defaultdict
from CommModules import *

#applies a button push to the components
#this is expressed by manually provisioning a special button instruction that kickstartsthe process
def pushButton(modules):
    inputs = [("button", "broadcaster", Pulse.LOW)]
    pulses = []
    while inputs:
        src, dst, val = inputs.pop(0)
        pulses.append(val)
        #Some ouputs aren't known components, so we skip checking them
        if dst in modules.keys():
            inputs.extend(modules[dst].applyPulse(src, val))
    return pulses

file = open('Input.txt', 'r')
input = file.read()
lines = input.split('\n')

modules = {}

#define modules
for line in lines:
    src, dests = [s.strip() for s in line.split("->")]
    destList = [s.strip() for s in dests.split(',')]
    if src == "broadcaster":
        modules[src] = Broadcaster(src, destList)
    else:
        match src[0]:
            case '%':
                modules[src[1:]] = FlipFlop(src[1:], destList)
            case '&':
                modules[src[1:]] = Conjunction(src[1:],destList)

#back-fill inputs of conjunction modules
for k,v in modules.items():
    for o in v.outs:
        #Some ouputs aren't known components, so we skip checking them
        if o in modules.keys() and type(modules[o]) is Conjunction:
            modules[o].addInput(k)

vals = []
for _ in range(1000):
    pulses = pushButton(modules)
    vals.append((pulses.count(Pulse.LOW), pulses.count(Pulse.HIGH)))

lows = sum([v[0] for v in vals])
highs = sum([v[1] for v in vals])
print(lows*highs)