from pprint import pprint

X = 0
Y = 1

instructions = []


def follow(leader, current):
    distance = ((leader[X] - current[X])**2 + (leader[Y] - current[Y])**2)**0.5

    if (distance >= 2):
        # Veritical movement required
        if (leader[X] == current[X]):
            # Up
            if (leader[Y] > current[Y]):
                current = (current[X], current[Y] + 1)
            # Down
            else:
                current = (current[X], current[Y] - 1)
        # Horizontal movement required
        elif (leader[Y] == current[Y]):
            # Left
            if (leader[X] > current[X]):
                current = (current[X] + 1, current[Y])
            # Right
            else:
                current = (current[X] - 1, current[Y])
        # Diagnol movement requirement
        else:
            # Up-right
            if (leader[X] > current[X] and leader[Y] > current[Y]):
                current = (current[X] + 1, current[Y] + 1)
            # Down-right
            elif (leader[X] > current[X] and leader[Y] < current[Y]):
                current = (current[X] + 1, current[Y] - 1)
            # Down-left
            elif (leader[X] < current[X] and leader[Y] < current[Y]):
                current = (current[X] - 1, current[Y] - 1)
            # Up-left
            else:
                current = (current[X] - 1, current[Y] + 1)

    return current


def loadData(fileName):
    file = open(fileName, 'r')
    lines = file.readlines()
    for line in lines:
        parts = line.strip().split()
        instructions.append((parts[0], int(parts[1])))

    # pprint(instructions)


def step(head, direction):
    if (direction == 'U'):
        head = (head[X], head[Y] + 1)
    elif (direction == 'D'):
        head = (head[X], head[Y] - 1)
    elif (direction == 'L'):
        head = (head[X] - 1, head[Y])
    else: # direction == 'R'
        head = (head[X] + 1, head[Y])

    return head


def part1():
    # Starting points for Head and Tail
    head = (0, 0)
    tail = (0, 0)

    # Points the Tail has visited
    tailVisits = { tail }

    for instruction in instructions:
        direction = instruction[0]
        count = instruction[1]

        # print('====' + str(instruction) + '====')

        for i in range(count):
            # Move the Head and the Tail follows
            head = step(head, direction)
            tail = follow(head, tail)

            # print('move: ' + str(i) + ' - H: ' + str(head) + ', T: ' + str(tail))

            # Update the set of points visited by the Tail
            tailVisits.add(tail)

    # pprint(tailVisits)

    print("Part 1: " + str(len(tailVisits)))


def part2():
    # Starting points for Head and Tail
    head = (0, 0)
    tailKnots = []
    for i in range(9):
        tailKnots.append((0, 0))

    # Points the Tail has visited
    tailVisits = { (0, 0) }

    for instruction in instructions:
        direction = instruction[0]
        count = instruction[1]

        # print('====' + str(instruction) + '====')

        for i in range(count):
            # Move the Head and the Tail follows
            head = step(head, direction)

            leader = head
            for i in range(len(tailKnots)):
                next = tailKnots[i]
                replacement = follow(leader, next)
                tailKnots[i] = replacement
                leader = replacement

            # print('move: ' + str(i) + ' - H: ' + str(head) + ', T: ' + str(tail))

            # Update the set of points visited by the Tail
            tailVisits.add(tailKnots[len(tailKnots) - 1])

    # pprint(tailVisits)

    print("Part 2: " + str(len(tailVisits)))


loadData('day9.dat')

part1()
part2()