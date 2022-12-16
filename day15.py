DATA_FILE = 'day15.dat'

X = 0
Y = 1

SENSOR = 0
BEACON = 1
DISTANCE = 2

grid = []

def loadData():
    minX = 1000000
    maxX = -minX
    minY = minX
    maxY = maxX

    groups = []

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

    print('X range: ' + str(minX) + ':' + str(maxX))
    print('Y range: ' + str(minY) + ':' + str(maxY))


loadData()