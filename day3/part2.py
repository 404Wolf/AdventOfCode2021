entries = open("input.txt").read().split("\n")

# find oxygen generator rating
for entry in entries:
    mostCommon = 1
    if entry.count("1") < entry.count("0"):
        mostCommon = 0
    print(entry,mostCommon)

# find co2 scrubber rating