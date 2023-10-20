def findSignal(length):
    file = open('day6.dat', 'r')
    line = file.readline().strip()

    for i in range(len(line) - (length - 1)):
        chunk = line[i:i + length]

        unique_count = len(set([c for c in chunk]))
        if (unique_count == length):
            return i + length


print("Part 1: " + str(findSignal(4)))
print("Part 2: " + str(findSignal(14)))