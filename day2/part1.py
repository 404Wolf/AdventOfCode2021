# load input file
inputs = open("input.txt").read().split("\n")

depth = 0
forwardness = 0

for movement in inputs:
  movement = movement.split(" ")
  movement[1] = int(movement[1])
  
  if movement[0] == "forward":
    forwardness += movement[1]
  elif movement[0] == "down":
    depth += movement[1]
  elif movement[0] == "up":
    depth -= movement[1]

print(depth*forwardness)