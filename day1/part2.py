import json
from math import inf 

#load input file
with open("input.txt") as input:
    depths = input.read().split("\n")
    depths = map(int, depths)
    depths = list(depths)

#generate array of windows
windows = []
while True:
    currentWindowCounter = 0
    
    for depth in depths:
        windows.append(depths[currentWindowCounter:currentWindowCounter+3])
        currentWindowCounter += 4
        if len(windows[-1]) == 3:
            break

    del depths[0]
    if len(depths) < 3:
        break

#calculate number of changes that are increased
changes = []
previous = inf
for window in map(sum, windows):
    if window > previous:
        changes.append(True)
    elif window <= previous:
        changes.append(False)
    previous = window

print(sum(changes))