inputs = open("input.txt").read().split("\n")

freq = []
for index in range(len(inputs[0])):
    freq.append(sum(map(lambda x: int(x[index]), inputs)))

print(freq)

gamma = "".join(tuple(map(lambda x: "1" if x > len(inputs) / 2 else "0", freq)))
epsilon = "".join(tuple(map(lambda x: "0" if x > len(inputs) / 2 else "1", freq)))

def convBin(binary):
    return sum(
        list(
            map(
                lambda x: int(x[1]) * (2 ** (len(binary) - x[0] - 1)), enumerate(binary)
            )
        )
    )

print(convBin(gamma) * convBin(epsilon))
