def part1():
    score = 0

    rounds = loadData(1)
    for round in rounds:
        opponent = round[0]
        me = round[1]

        # Points for result
        if (opponent == me):
            # Draw
            score += 3
        elif ((opponent == 'R' and me == 'P') or
              (opponent == 'P' and me == 'S') or
              (opponent == 'S' and me == 'R')):
            # Win
            score += 6

        # Points for throw
        if (me == 'R'):
            score += 1
        elif (me == 'P'):
            score += 2
        else:
            score += 3

    print("Part 1: " + str(score))


def part2():
    score = 0

    rounds = loadData(2)
    for round in rounds:
        opponent = round[0]
        result = round[1]
        me = ''

        # Points for result
        if (result == 'Y'):
            # Draw
            score += 3
            me = opponent
        elif (result == 'Z'):
            # Win
            score += 6
            if (opponent == 'R'):
                me = 'P'
            elif (opponent == 'P'):
                me = 'S'
            else:
                me = 'R'
        else:
            # Lose
            if (opponent == 'R'):
                me = 'S'
            elif (opponent == 'P'):
                me = 'R'
            else:
                me = 'P'

        # Points for throw
        if (me == 'R'):
            score += 1
        elif (me == 'P'):
            score += 2
        else:
            score += 3

    print("Part 2: " + str(score))


def loadData(part):
    rounds = []

    file = open('day2.dat', 'r')
    lines = file.readlines()

    for line in lines:
        throws = line.strip().split(' ')

        # Standardize throws:
        #   1. Convert A, B, or C to R, P, or S
        #   2. Convert X, Y, or Z to R, P, or S (part 1 only)
        if (throws[0] == 'A'):
            throws[0] = 'R'
        elif (throws[0] == 'B'):
            throws[0] = 'P'
        else:
            throws[0] = 'S'

        if (part == 1):
            if (throws[1] == 'X'):
                throws[1] = 'R'
            elif (throws[1] == 'Y'):
                throws[1] = 'P'
            else:
                throws[1] = 'S'

        # print(throws)
        rounds.append(throws)

    return rounds


part1()
part2()