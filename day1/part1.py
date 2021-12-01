from math import inf

with open("input.txt") as input:
    depths = input.read().split("\n")
    depths = map(int, depths)
    depths = tuple(depths)

changes = []
previous = inf
for depth in depths:
    if depth > previous:
        changes.append(True)
    elif depth <= previous:
        changes.append(False)
    previous = depth

print(sum(changes))