LOW = 0
HIGH = 1

pairs = []

def loadData():
    file = open('day4.dat', 'r')
    lines = file.readlines()

    for line in lines:
        assignments = line.strip().split(',')
        elf1 = [int(numString) for numString in assignments[0].split('-')]
        elf2 = [int(numString) for numString in assignments[1].split('-')]

        pairs.append([elf1, elf2])


def part1():
    count = 0

    for pair in pairs:
        elf1 = pair[0]
        elf2 = pair[1]

        if ((elf1[LOW] >= elf2[LOW] and elf1[HIGH] <= elf2[HIGH]) or
            (elf2[LOW] >= elf1[LOW] and elf2[HIGH] <= elf1[HIGH])):
            count = count + 1

    print("Part 1: " + str(count))


def part2():
    count = 0

    for pair in pairs:
        elf1 = pair[0]
        elf2 = pair[1]

        if (not (elf1[LOW] > elf2[HIGH] or elf1[HIGH] < elf2[LOW])):
            count = count + 1

    print("Part 2: " + str(count))


loadData()
part1()
part2()