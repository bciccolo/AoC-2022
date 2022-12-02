def part1():
    print("Part 1: " + str(totals[0]))

def part2():
    print("Part 1: " + str(totals[0] + totals[1] + totals[2]))


def loadData():
    global totals

    file = open('day1.dat', 'r')
    lines = file.readlines()

    runningTotal = 0

    for line in lines:
        if (line.strip() == ''):
            totals.append(runningTotal)
            runningTotal = 0
        else:
            number = int(line.strip())
            runningTotal += number

    totals.sort(reverse = True)

totals = []
loadData()
part1()
part2()