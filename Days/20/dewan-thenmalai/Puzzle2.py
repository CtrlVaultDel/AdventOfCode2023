from collections import defaultdict
from math import lcm
from CommModules import *

#Through analysis of the input, we can see that the only component providing a signal to "rx" is a conjunction. This means we just need to find the state where all inputs are HIGH. This might take forever, so we find the minimum number of presses it takes to make each input HIGH, then take their least common multiple to get when they align
def getRXCount(modules):
    rxPred, *_ = [k for k,v in modules.items() if "rx" in v.outs]
    lowRXState = {k: 0 for k in modules[rxPred].state.keys()} #storage for button press count per conjunction input
    lowRX = False
    presses = 0
    while not lowRX:
        #check if we found everything
        if all(v > 0 for v in lowRXState.values()):
            break
        
        presses += 1
        inputs = [("button", "broadcaster", Pulse.LOW)]
        while inputs:
            src, dst, val = inputs.pop(0)
            
            if src in modules[rxPred].state and val == Pulse.HIGH:
                lowRXState[src] = presses
            
            #Some ouputs aren't known components, so we skip checking them
            if dst in modules.keys():
                inputs.extend(modules[dst].applyPulse(src, val))
    
    return lcm(*lowRXState.values())

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

print(getRXCount(modules))