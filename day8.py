from pprint import pprint

# 2D array of all the tree heights read from the data file
heightMap = []

# 2D array of which trees are visible from at least one edge (1 = visible, 0 = hidden);
# each (x,y) position matches to the corresponding element in heightMap
visibilityMap = []


def checkColumn(column):
    size = len(heightMap)

    # Check top-to-bottom
    maxHeight = -1
    for i in range(size):
        currentHeight = heightMap[i][column]
        if (currentHeight > maxHeight):
            visibilityMap[i][column] = 1
            maxHeight = currentHeight

    # Check right-to-left
    maxHeight = -1
    for i in range(size - 1, -1, -1):
        currentHeight = heightMap[i][column]
        if (currentHeight > maxHeight):
            visibilityMap[i][column] = 1
            maxHeight = currentHeight


def checkRow(row):
    size = len(heightMap)

    # Check left-to-right
    maxHeight = -1
    for i in range(size):
        currentHeight = heightMap[row][i]
        if (currentHeight > maxHeight):
            visibilityMap[row][i] = 1
            maxHeight = currentHeight

    # Check right-to-left
    maxHeight = -1
    for i in range(size - 1, -1, -1):
        currentHeight = heightMap[row][i]
        if (currentHeight > maxHeight):
            visibilityMap[row][i] = 1
            maxHeight = currentHeight


def getScenicScore(row, column):
    maxHeight = heightMap[row][column]
    size = len(heightMap)

    # Eastern view
    east = 0
    for x in range(column + 1, size, 1):
        east += 1
        if (heightMap[row][x] >= maxHeight):
            break

    # Western view
    west = 0
    for x in range(column - 1, -1, -1):
        west += 1
        if (heightMap[row][x] >= maxHeight):
            break

    # North view
    north = 0
    for y in range(row - 1, -1, -1):
        north += 1
        if (heightMap[y][column] >= maxHeight):
            break

    # Southern view
    south = 0
    for y in range(row + 1, size, 1):
        south += 1
        if (heightMap[y][column] >= maxHeight):
            break

    return east * west * north * south


def loadData(fileName):
    file = open(fileName, 'r')
    lines = file.readlines()
    for line in lines:
        heightMap.append([int(digit) for digit in [*line.strip()]])
        visibilityMap.append([0 for digit in [*line.strip()]])

    # pprint(visibilityMap)
    # pprint(heightMap)


def part1():
    for i in range(len(heightMap)):
        checkRow(i)
        checkColumn(i)

    count = sum([sum(i) for i in visibilityMap])

    print("Part 1: " + str(count))


def part2():
    maxScore = 0

    size = len(heightMap)
    for row in range(size):
        for column in range(size):
            score = getScenicScore(row, column)
            if (score > maxScore):
                maxScore = score

    print("Part 2: " + str(maxScore))


loadData('day8.dat')

part1()
part2()