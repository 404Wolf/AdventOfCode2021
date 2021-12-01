from math import inf

#load input file
with open("input.txt") as input:
    depths = input.read().split("\n")
    depths = map(int, depths)
    depths = tuple(depths)

#calculate for each change vs it's respective previous
#if it's a positive change (True) or is the same/is less (False)
changes = []
previous = inf
for depth in depths:
    if depth > previous:
        changes.append(True)
    elif depth <= previous:
        changes.append(False)
    previous = depth

#output the number of positive changes
print(sum(changes))