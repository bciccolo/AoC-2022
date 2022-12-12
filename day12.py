from pprint import pprint

def loadData(dataFile):
    global heightMap, start, end

    y = 0
    x = 0

    file = open(dataFile, 'r')
    lines = file.readlines()
    for line in lines:
        row = []

        for letter in line.strip():
            height = ord(letter) - ord('a')

            if (letter == 'S'):
                start = (y , x)
                height = 0
            elif (letter == 'E'):
                end = (y, x)
                height = 26

            row.append(height)
            x += 1

        heightMap.append(row)

        y += 1
        x = 0

    # pprint(heightMap)
    # print("Start: " + str(start))
    # print("End: " + str(end))


def part1():
    steps = 0

    print('Part 1: ' + str(steps))


def part2():
    print('Part 2: NOT READY')


heightMap = []
start = (0, 0)
end = (0, 0)
loadData('day12-snippet.dat')

part1()
part2()