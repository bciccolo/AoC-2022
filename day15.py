DATA_FILE = 'day15.dat'
SEARCH_ROW_INDEX = 2000000

SENSOR = 0
BEACON = 1
DISTANCE = 2

X = 0
Y = 1

groups = []

minX = 0
maxX = 0
minY = 0
maxY = 0

def loadData():
    global groups, minX, maxX, minY, maxY

    file = open(DATA_FILE, 'r')
    lines = file.readlines()
    for line in lines:
        # Now that's what I call parsing!
        sensor, beacon = [[int(x[2:]) for x in device.split(', ')] for device in line.strip()[10:].split(': closest beacon is at ')]

        distance = abs(sensor[X] - beacon[X]) + abs(sensor[Y] - beacon[Y])

        groups.append((sensor, beacon, distance))

    minX = min([min((group[SENSOR][X], group[BEACON][X])) for group in groups])
    maxX = max([max((group[SENSOR][X], group[BEACON][X])) for group in groups])

    minY = min([min((group[SENSOR][Y], group[BEACON][Y])) for group in groups])
    maxY = max([max((group[SENSOR][Y], group[BEACON][Y])) for group in groups])

    # Extend X range in both directions by the largest distance
    maxDistance = max([group[DISTANCE] for group in groups])
    minX -= maxDistance
    maxX += maxDistance

    # print('X range: ' + str(minX) + ':' + str(maxX))
    # print('Y range: ' + str(minY) + ':' + str(maxY))


def part1():
    searchRow = [0 for i in range(maxX - minX + 1)]

    # Step 1: Mark all spaces that can be reached by at least one sensor
    for group in groups:
        sensor = group[SENSOR]
        maxDistance = group[DISTANCE]

        requiredRange = abs(sensor[Y] - SEARCH_ROW_INDEX)

        if (maxDistance >= requiredRange):
            searchRow[sensor[X] - minX] = 1

            xRange = maxDistance - requiredRange
            xRangeMin = sensor[X] - xRange
            xRangeMax = sensor[X] + xRange
            for x in range(xRangeMin, xRangeMax + 1):
                searchRow[x - minX] = 1

    # Step 2: Clear any spaces that contain a known beacon
    for group in groups:
        beacon = group[BEACON]
        if (beacon[Y] == SEARCH_ROW_INDEX):
            searchRow[beacon[X] - minX] = 0

    # print(searchRow)

    print("Part 1: " + str(sum(searchRow)))

loadData()
part1()