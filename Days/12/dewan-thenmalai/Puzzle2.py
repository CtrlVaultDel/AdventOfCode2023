# work backwards through string, checking each group
def countArrangements(record, groups):
    # memoization
    table = {}
    def subArrangements(r, g):
        # because the initial inputs are the lengths of the record and groups, the "current" value is actually one less than r and g
        if (r,g) in table:
            return table[(r,g)]
        if r == 0 and g == 0:
        # no remaining chars or groups because whole string was successfully parsed
            return 1
        elif r == 0:
        #no remaining chars, but not all groups fulfilled -> invalid arrangement
            return 0
        elif g == 0:
        # no groups left, so we check that there are no remaining '#' ('?' can be treated as '.' for validity checking)
            return 1*all([c != '#' for c in record[:r]])
        elif record[r-1] == '.':
        # if current char is '.', step back with same group
            result = subArrangements(r-1,g)
        else:
        # current char is '#' or '?' and groups remain
            count = groups[g-1]
            if r < count or any([any(c == '.' for c in record[r-count:r])]):
            # if there are fewer remaining chars than the size of the group or the previous range has something that can't be '#' -> invalid arrangement
                result = 0
            elif r > count and record[r-count-1] == '#':
            # if the char just before a group is a '#' then that group is invalid (only applicable if number of remain chars is greater than the size of the group)
            # because of the previous case we know none of the chars in our range is '.'
                result = 0
            else:
            # jump back over group
                result = subArrangements(max(r-count-1,0),g-1)
            # this section makes the assuption that '?' is treated as '#'
            if record[r-1] == '?':
            # if previous char is '?' then evaluate case where it is '.'
                result += subArrangements(r-1,g)
        table[(r,g)] = result
        return result
    return subArrangements(len(record), len(groups))

file = open('Input.txt', 'r')
input = file.read()
lines = input.split('\n')

arrangements = []
for line in lines:
    springs, countStr = line.split()
    counts = [int(i) for i in countStr.split(',')]
    unfoldedSprings = '?'.join([springs]*5)
    unfoldedCounts = counts*5
    arrangements.append(countArrangements(unfoldedSprings,unfoldedCounts))

print(sum(arrangements))