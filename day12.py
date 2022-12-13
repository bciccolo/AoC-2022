from pprint import pprint


def loadData(dataFile):
    global heightGrid, distanceGrid, start, end

    y = 0
    x = 0

    file = open(dataFile, 'r')
    lines = file.readlines()
    for line in lines:
        heights = []
        distances = []

        for letter in line.strip():
            # 'a' = 0, 'z' = 25
            height = ord(letter) - ord('a')
            distance = 999

            if (letter == 'S'):
                start = (y , x)
                # start height = 'a'
                height = 0
            elif (letter == 'E'):
                end = (y, x)
                # end height = 'z'
                height = 25
                distance = 0

            heights.append(height)
            distances.append(distance)

            x += 1

        heightGrid.append(heights)
        distanceGrid.append(distances)

        y += 1
        x = 0

    # pprint(heightGrid)
    # pprint(distanceGrid)
    # print("Start: " + str(start))
    # print("End: " + str(end))


def updateDistanceGrid():
    global heightGrid, distanceGrid

    maxRow = len(distanceGrid)
    maxCol = len(distanceGrid[0])

    distance = 0
    moreToCheck = True
    while (moreToCheck):
        moreToCheck = False

        for row in range(maxRow):
            for col in range(maxCol):
                if (distanceGrid[row][col] == distance):
                    # Check and mark neighbors
                    height = heightGrid[row][col]

                    # Up/North
                    if (row > 0 and height - heightGrid[row - 1][col] <= 1 and distanceGrid[row - 1][col] == 999):
                        distanceGrid[row - 1][col] = distance + 1
                        moreToCheck = True

                    # Down/South
                    if (row < maxRow - 1 and height - heightGrid[row + 1][col] <= 1 and distanceGrid[row + 1][col] == 999):
                        distanceGrid[row + 1][col] = distance + 1
                        moreToCheck = True

                    # Right/East
                    if (col < maxCol - 1 and height - heightGrid[row][col + 1] <= 1 and distanceGrid[row][col + 1] == 999):
                        distanceGrid[row][col + 1] = distance + 1
                        moreToCheck = True

                    # Left/West
                    if (col > 0 and height - heightGrid[row][col - 1] <= 1 and distanceGrid[row][col - 1] == 999):
                        distanceGrid[row][col - 1] = distance + 1
                        moreToCheck = True

        distance += 1

    # for distances in distanceGrid:
    #     print(''.join([ '.' if num == 999 else str(num) for num in distances]))


def part1():
    print('Part 1: ' + str(distanceGrid[start[0]][start[1]]))


def part2():
    minDistance = 999

    for row in range(len(distanceGrid)):
        for col in range(len(distanceGrid[0])):
            if (heightGrid[row][col] == 0):
                distance = distanceGrid[row][col]
                if (distance < minDistance):
                    minDistance = distance

    print('Part 2: ' + str(minDistance))


heightGrid = []
distanceGrid = []
start = (0, 0)
end = (0, 0)
paths = []
loadData('day12-snippet.dat')
updateDistanceGrid()

part1()
part2()