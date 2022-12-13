from pprint import pprint

def findPathsToEnd(row, column, steps, depth):
    global heightMap, end, paths, attempts

    point = (row, column)

    if (point not in steps):
        # print('Point ' + str(point) + " @ depth " + str(depth))
        steps.append(point)

        currentHeight = heightMap[row][column]

        if (row == end[0] and column == end[1]):
            paths.append(steps)
        else:
            # West
            if (column > 0 and heightMap[row][column - 1] - currentHeight <= 1):
                attempt = (row, column, '<')
                if (attempt not in attempts or len(steps) < attempts[attempt]):
                    attempts[attempt] = len(steps)
                    findPathsToEnd(row, column - 1, steps.copy(), depth + 1)

            # East
            if (column < len(heightMap[0]) - 1 and heightMap[row][column + 1] - currentHeight <= 1):
                attempt = (row, column, '>')
                if (attempt not in attempts or len(steps) < attempts[attempt]):
                    attempts[attempt] = len(steps)
                    findPathsToEnd(row, column + 1, steps.copy(), depth + 1)

            # South
            if (row < len(heightMap) - 1 and heightMap[row + 1][column] - currentHeight <= 1):
                attempt = (row, column, 'v')
                if (attempt not in attempts or len(steps) < attempts[attempt]):
                    attempts[attempt] = len(steps)
                    findPathsToEnd(row + 1, column, steps.copy(), depth + 1)

            # North
            if (row > 0 and heightMap[row - 1][column] - currentHeight <= 1):
                attempt = (row, column, '^')
                if (attempt not in attempts or len(steps) < attempts[attempt]):
                    attempts[attempt] = len(steps)
                    findPathsToEnd(row - 1, column, steps.copy(), depth + 1)


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
                height = 25

            row.append(height)
            x += 1

        heightMap.append(row)

        y += 1
        x = 0

    # pprint(heightMap)
    # print("Start: " + str(start))
    # print("End: " + str(end))


def part1():
    global paths

    findPathsToEnd(start[0], start[1], [], 0)

    minSteps = len(paths[0])
    for path in paths:
        if (len(path) < minSteps):
            minSteps = len(path)
        # pprint(len(path))

    print('Part 1: ' + str(minSteps - 1)) # Subtract 1 to ignore start point


def part2():
    print('Part 2: NOT READY')


heightMap = []
start = (0, 0)
end = (0, 0)
paths = []
attempts = {}
loadData('day12.dat')

part1()
part2()