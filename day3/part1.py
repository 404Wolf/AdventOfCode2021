# load in input.txt as a newline seperated array
entries = open("input.txt").read().split("\n")

# the equivalent of mapping the following function onto each value in entries:
# def rowToList(row):
#     row = tuple(row) / eg: "0101" -> ("0", "1", "0", "1")
#     row = map(int, row) / eg: ("0", "1", "0", "1") -> (0, 1, 0, 1)
#     return row
entries = map(lambda entry: tuple(map(int, tuple(entry))), entries)

# make an itterable of each coloumn of the multidimentional itterable
columns = zip(*entries)  # unpack entries into zip() function

# set gammaRate and epsilonRate to ""
# these empty strings have "0"s and "1"s appended to them,
# and will be used to create binary strings later on
# which in the end will be converted to integers
gammaRate = epsilonRate = ""

# itterate through columns of entries
for column in columns:
    # if there are more occurances of "1"s than there are "0"s:
    # - the gamma rate's binary value gets a 1
    # - the epsilon rate's binary value gets a 0
    if column.count(1) > column.count(0):
        epsilonRate += "0"
        gammaRate += "1"
    # if there are less occurances of "1"s than there are "0"s:
    # - the gamma rate's binary value gets a 0
    # - the epsilon rate's binary value gets a 1
    else:
        epsilonRate += "1"
        gammaRate += "0"

# convert the binary values to decimal values
# int(string, base), and base=2 means the string is in binary
gammaRate = int(gammaRate, 2)
epsilonRate = int(epsilonRate, 2)

# gammaRate * epsilonRate = power consumption
powerConsumption = gammaRate * epsilonRate

# print answer
print(powerConsumption)
