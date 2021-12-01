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
        windows.append(depths[currentWindowCounter:currentWindowCounter+3]) #windows consist of three entries
        #continue moving forward in depths until the window consists of three entires (a full window is three entries)
        currentWindowCounter += 4
        if len(windows[-1]) == 3:
            break #break the loop and remove the first depth

    del depths[0]
    # if there are less than three depths left, a full window is not able to be created
    if len(depths) < 3:
        break

#calculate for each change vs it's respective previous
#if it's a positive change (True) or is the same/is less (False)
changes = []
previous = inf
for window in map(sum, windows): #the sum of each window
    if window > previous:
        changes.append(True)
    elif window <= previous:
        changes.append(False)
    previous = window

#output the number of positive changes
print(sum(changes))