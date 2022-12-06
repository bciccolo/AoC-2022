moves = []

def getCode():
    code = ''

    for stack in stacks:
        code = code + stack.pop()

    return code


def initializeStacks():
    # Snippet:
    # return [ ['Z', 'N'], ['M', 'C', 'D'], ['P'] ]

    # Full:
    return [ ['S', 'C', 'V', 'N'],
             ['Z', 'M', 'J', 'H', 'N', 'S'],
             ['M', 'C', 'T', 'G', 'J', 'N', 'D'],
             ['T', 'D', 'F', 'J', 'W', 'R', 'M'],
             ['P', 'F', 'H'],
             ['C', 'T', 'Z', 'H', 'J'],
             ['D', 'P', 'R', 'Q', 'F', 'S', 'L', 'Z'],
             ['C', 'S', 'L', 'H', 'D', 'F', 'P', 'W'],
             ['D', 'S', 'M', 'P', 'F', 'N', 'G', 'Z'] ]


def loadData():
    global moves

    file = open('day5.dat', 'r')
    lines = file.readlines()

    instruction = False
    for line in lines:
        line = line.strip()
        if (instruction):
            pieces = line.split()
            moveCount = int(pieces[1])
            moveFrom = int(pieces[3]) - 1
            moveTo = int(pieces[5]) - 1
            moves.append([moveCount, moveFrom, moveTo])
        elif (line == ''):
            instruction = True


def part1():
    count = 0

    for move in moves:
        # print(move)
        moveCount = move[0]
        moveFrom = move[1]
        moveTo = move[2]

        for i in range(moveCount):
            item = stacks[moveFrom].pop()
            stacks[moveTo].append(item)

        count = count + 1
        # showStacks(count)

    print("Part 1: " + getCode())


def part2():
    count = 0

    for move in moves:
        # print(move)
        moveCount = move[0]
        moveFrom = move[1]
        moveTo = move[2]

        stacks[moveTo] = stacks[moveTo] + stacks[moveFrom][-moveCount:]
        del stacks[moveFrom][-moveCount:]

        count = count + 1
        # showStacks(count)

    print("Part 2: " + getCode())


def showStacks(count):
    print("After " + str(count) + " moves:")
    for stack in stacks:
        print(stack)


stacks = initializeStacks()
loadData()
part1()

# Need to reset the stacks before solving part 2
stacks = initializeStacks()
part2()