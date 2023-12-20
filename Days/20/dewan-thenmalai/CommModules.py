from enum import Enum

class Pulse(Enum):
    LOW = 0
    HIGH = 1

class Broadcaster:
    def __init__(self, name, outs):
        self.name = name
        self.outs = outs
        self.state = True
    
    def applyPulse(self, src, val):
        return [(self.name, o, Pulse.LOW) for o in self.outs]

class FlipFlop:
    def __init__(self, name, outs):
        self.name = name
        self.outs = outs
        self.state = False
    
    def applyPulse(self, src, val):
        if val == Pulse.LOW:
            self.state = not self.state
            if self.state: #on state
                return [(self.name, o, Pulse.HIGH) for o in self.outs]
            else: #off state
                return [(self.name, o, Pulse.LOW) for o in self.outs]
        else: #Pulse.HIGH
            return []

class Conjunction:
    def __init__(self, name, outs):
        self.name = name
        self.outs = outs
        self.state = {}
    
    def addInput(self, src):
        self.state[src] = Pulse.LOW
    
    def applyPulse(self, src, val):
        self.state[src] = val
        if all(i == Pulse.HIGH for i in self.state.values()):
            return [(self.name, o, Pulse.LOW) for o in self.outs]
        else:
            return [(self.name, o, Pulse.HIGH) for o in self.outs]