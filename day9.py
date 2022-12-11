from pprint import pprint

X = 0
Y = 1

instructions = []

# Starting points for Head and Tail
head = (0, 0)
tail = (0, 0)

# Points the Tail has visited
headVisits = { head }
tailVisits = { tail }


def updateTailPosition():
    global head, tail

    distance = ((head[X] - tail[X])**2 + (head[Y] - tail[Y])**2)**0.5

    if (distance >= 2):
        # Veritical movement required
        if (head[X] == tail[X]):
            # Up
            if (head[Y] > tail[Y]):
                tail = (tail[X], tail[Y] + 1)
            # Down
            else:
                tail = (tail[X], tail[Y] - 1)
        # Horizontal movement required
        elif (head[Y] == tail[Y]):
            # Left
            if (head[X] > tail[X]):
                tail = (tail[X] + 1, tail[Y])
            # Right
            else:
                tail = (tail[X] - 1, tail[Y])
        # Diagnol movement requirement
        else:
            # Up-right
            if (head[X] > tail[X] and head[Y] > tail[Y]):
                tail = (tail[X] + 1, tail[Y] + 1)
            # Down-right
            elif (head[X] > tail[X] and head[Y] < tail[Y]):
                tail = (tail[X] + 1, tail[Y] - 1)
            # Down-left
            elif (head[X] < tail[X] and head[Y] < tail[Y]):
                tail = (tail[X] - 1, tail[Y] - 1)
            # Up-left
            else:
                tail = (tail[X] - 1, tail[Y] + 1)


def loadData(fileName):
    file = open(fileName, 'r')
    lines = file.readlines()
    for line in lines:
        parts = line.strip().split()
        instructions.append((parts[0], int(parts[1])))

    # pprint(instructions)


def part1():
    global head

    for instruction in instructions:
        direction = instruction[0]
        count = instruction[1]

        # print('====' + str(instruction) + '====')

        for i in range(count):
            # Move the head
            if (direction == 'U'):
                head = (head[X], head[Y] + 1)
            elif (direction == 'D'):
                head = (head[X], head[Y] - 1)
            elif (direction == 'L'):
                head = (head[X] - 1, head[Y])
            else: # direction == 'R'
                head = (head[X] + 1, head[Y])

            # Move the tail (if necessary)
            updateTailPosition()

            # print('move: ' + str(i) + ' - H: ' + str(head) + ', T: ' + str(tail))

            # Update the set of points visited by the tail
            headVisits.add(head)
            tailVisits.add(tail)

    pprint(tailVisits)

    # 9348 - too high
    print("Part 1: " + str(len(tailVisits)))


def part2():
    print("Part 2: " + str(0))


loadData('day9.dat')

part1()
part2()