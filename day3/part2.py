# load in input.txt as a newline seperated array
entries = open("input.txt").read().split("\n")

# the equivalent of mapping the following function onto each value in entries:
# def rowToList(row):
#     row = list(row) / eg: "0101" -> ("0", "1", "0", "1")
#     row = map(int, row) / eg: ("0", "1", "0", "1") -> (0, 1, 0, 1)
#     return row
entries = map(lambda entry: list(map(int, list(entry))), entries)

# make an itterable of each coloumn of the multidimentional itterable
columns = zip(*entries)  # unpack entries into zip() function

def mostCommon(itterable):
  """Returns most common element in itterable"""
  if itterable.count("0") > itterable.count("1"):
    return 0
  else:
    return 1
    
goodEntries = []

while len(goodEntries) != 1:
  for entry in entries:
    for bitIndex, bit in enumerate(entry):
      # We are getting the value of the column, but using the index of the entry
      success = True
      if mostCommon(columns[bitIndex]) != bit:
        success = False

    if success:
      goodEntries.append(entry)
      
  entries = goodEntries
  
print(goodEntries)
# # newBit = int(newBit, 2)
# # print(newBit)