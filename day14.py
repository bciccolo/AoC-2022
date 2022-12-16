# Analysis of data file:
# 490 <= x <= 570
#   0 <= y <= 200


# Approx. dimensions of full data (stretched horizontally to account for the floor in part 2, based on actual height of 162)
DATA_FILE = 'day14.dat'
MIN_X = 250
MAX_X = 750
MIN_Y = 0
MAX_Y = 200

# Approx. dimensions of snippet data (stretched horizontally to account for the floor in part 2, based on actual height of 11)
# DATA_FILE = 'day14-snippet.dat'
# MIN_X = 480
# MAX_X = 515
# MIN_Y = 0
# MAX_Y = 13

grid = []
trueMaxY = 0

def dropGrain(useFloor):
    x = 500 - MIN_X
    y = 0

    while (grid[y][x] == '.'):
        if (grid[y + 1][x] == '.'):
            y += 1
        elif (grid[y + 1][x - 1] == '.'):
            y += 1
            x -= 1
        elif (grid[y + 1][x + 1] == '.'):
            y += 1
            x += 1
        else:
            grid[y][x] = 'o'

        if (not useFloor and y > trueMaxY):
            break

    return y


def loadData():
    global grid, trueMaxY

    grid.clear()

    for y in range(MAX_Y - (MIN_Y - 1)):
        grid.append(['.' for i in range(MAX_X - (MIN_X - 1))])

    # printGrid()

    file = open(DATA_FILE, 'r')
    lines = file.readlines()
    for line in lines:
        points = [[int(number) for number in chunk.split(',')] for chunk in line.strip().split(' -> ')]

        lastPoint = None
        for point in points:
            if (point[1] > trueMaxY):
                trueMaxY = point[1]

            if (lastPoint != None):
                # Vertical line
                if (point[0] == lastPoint[0]):
                    x = point[0]
                    y1 = point[1]
                    y2 = lastPoint[1]
                    for y in range(min(y1, y2), max(y1, y2) + 1):
                        grid[y - MIN_Y][x - MIN_X] = '#'

                # Horizontal line
                else:
                    y = point[1]
                    x1 = point[0]
                    x2 = lastPoint[0]
                    for x in range(min(x1, x2), max(x1, x2) + 1):
                        grid[y - MIN_Y][x - MIN_X] = '#'

            lastPoint = point

    # print('True max Y: ' + str(trueMaxY))

    # Draw the floor
    for x in range(MAX_X - (MIN_X - 1)):
        grid[trueMaxY + 2][x] = '#'

    # printGrid()


def part1():
    count = 0

    while (dropGrain(False) <= trueMaxY):
        count += 1

    # printGrid()

    print("Part 1: " + str(count))


def part2():
    count = 0

    while (dropGrain(True) > 0):
        count += 1

    count += 1 # Add the last grain for the top of the pile

    # printGrid()

    print("Part 2: " + str(count))


def printGrid():
    for row in grid:
        print(''.join(row))


loadData()
part1()
loadData() # Reset the grid between parts
part2()