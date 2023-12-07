import functools
import operator
from collections import defaultdict

def checkFiveOfAKind(hand):
    counts = defaultdict(lambda: 0)
    wild = 0
    for card in hand:
        if card == 'J':
            wild += 1
        else:
            counts[card] += 1
    maxKey = max(counts, key=lambda k: counts[k])
    counts[maxKey] += wild
    if sorted(counts.values()) == [5]:
        return True
    return False

def checkFourOfAKind(hand):
    counts = defaultdict(lambda: 0)
    wild = 0
    for card in hand:
        if card == 'J':
            wild += 1
        else:
            counts[card] += 1
    maxKey = max(counts, key=lambda k: counts[k])
    counts[maxKey] += wild
    if sorted(counts.values()) == [1,4]:
        return True
    return False

def checkFullHouse(hand):
    counts = defaultdict(lambda: 0)
    wild = 0
    for card in hand:
        if card == 'J':
            wild += 1
        else:
            counts[card] += 1
    maxKey = max(counts, key=lambda k: counts[k])
    counts[maxKey] += wild
    if sorted(counts.values()) == [2,3]:
        return True
    return False

def checkThreeOfAKind(hand):
    counts = defaultdict(lambda: 0)
    wild = 0
    for card in hand:
        if card == 'J':
            wild += 1
        else:
            counts[card] += 1
    maxKey = max(counts, key=lambda k: counts[k])
    counts[maxKey] += wild
    if sorted(counts.values()) == [1,1,3]:
        return True
    return False

def checkTwoPair(hand):
    counts = defaultdict(lambda: 0)
    wild = 0
    for card in hand:
        if card == 'J':
            wild += 1
        else:
            counts[card] += 1
    maxKey = max(counts, key=lambda k: counts[k])
    counts[maxKey] += wild
    if sorted(counts.values()) == [1,2,2]:
        return True
    return False

def checkOnePair(hand):
    counts = defaultdict(lambda: 0)
    wild = 0
    for card in hand:
        if card == 'J':
            wild += 1
        else:
            counts[card] += 1
    maxKey = max(counts, key=lambda k: counts[k])
    counts[maxKey] += wild
    if sorted(counts.values()) == [1,1,1,2]:
        return True
    return False

def evalHand(hand):
    if hand == "JJJJJ":
        return "Five"
    if checkFiveOfAKind(hand):
        return "Five"
    if checkFourOfAKind(hand):
        return "Four"
    if checkFullHouse(hand):
        return "House"
    if checkThreeOfAKind(hand):
        return "Three"
    if checkTwoPair(hand):
        return "TwoPair"
    if checkOnePair(hand):
        return "Pair"
    return "High"

def sortRank(hand1, hand2):
    cardStrengths = [c for c in "J23456789TQKA"]
    hand1List = [c for c in hand1[0]]
    hand2List = [c for c in hand2[0]]
    for c1, c2 in zip(hand1List, hand2List):
        if cardStrengths.index(c1) > cardStrengths.index(c2):
            return 1
        elif cardStrengths.index(c1) < cardStrengths.index(c2):
            return -1
    return 0
    

file = open('Input.txt', 'r')
input = file.read()
lines = input.split('\n')

keys = ["Five", "Four", "House", "Three", "TwoPair", "Pair", "High"]
groups = {key: [] for key in keys}

for line in lines:
    elems = line.split()
    groups[evalHand(elems[0])].append(elems)

for k, v in groups.items():
    v.sort(key=functools.cmp_to_key(sortRank))

ranked = groups["High"] + groups["Pair"] + groups["TwoPair"] + groups["Three"] + groups["House"] + groups["Four"] + groups["Five"]
total = 0
for i, hand in enumerate(ranked, start=1):
    total += int(hand[1])*i

print(total)