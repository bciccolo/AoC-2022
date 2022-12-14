from ast import literal_eval
from pprint import pprint
from functools import cmp_to_key

CORRECT = 1
INCORRECT = -1
UNKNOWN = 0

def checkOrder(left, right):
    if (len(left) > 0 and len(right) > 0):
        i = 0
        while (i < len(left) and i < len(right)):
            nextLeft = left[i]
            nextRight = right[i]

            # Case 1: Two integers
            if (isinstance(nextLeft, int) and isinstance(nextRight, int)):
                # Left integer is bigger: INCORRECT order
                if (nextLeft > nextRight):
                    # print("case 1")
                    return INCORRECT
                # Left integer is smaller: correct order
                elif (nextLeft < nextRight):
                    # print("case 2")
                    return CORRECT

            # Case 2: Two lists
            elif (isinstance(nextLeft, list) and isinstance(nextRight, list)):
                result = checkOrder(nextLeft, nextRight)
                if (result != UNKNOWN):
                    # print("case 3")
                    return result

            # Case 3: One integer, one list
            else:
                if (isinstance(nextLeft, int)):
                    nextLeft = [nextLeft]
                else:
                    nextRight = [nextRight]

                result = checkOrder(nextLeft, nextRight)
                if (result != UNKNOWN):
                    # print("case 4")
                    return result

            i += 1

        # Left ran out of values: correct order
        if (len(left) < len(right)):
            # print("case 5")
            return CORRECT

        # Right ran out of values: INCORRECT order
        elif (len(left) > len(right)):
            # print("case 6")
            return INCORRECT

        # Ran out at the same time: unknown (let the caller figure it out)
        else:
            # print("case 7")
            return UNKNOWN

    # Both sides are empty: correct order
    elif (len(left) == 0 and len(right) == 0):
        # print("case 8 *******************") # HERE IN FULL, NOT IN SNIPPET
        return UNKNOWN

    # Left side is smaller: correct order
    elif (len(left) == 0 and len(right) > 0):
        # print("case 9")
        return CORRECT

    # Right side is smaller: INCORRECT order
    else:
        # print("case 10")
        return INCORRECT


def loadData(dataFile):
    global pairs

    file = open(dataFile, 'r')
    lines = file.readlines()

    packet1 = ''
    for line in lines:
        line = line.strip()
        if (packet1 != ''):
            pairs.append((literal_eval(packet1), literal_eval(line)))
            packet1 = ''
        else:
            packet1 = line

    # pprint(pairs)


def part1():
    sum = 0

    pairIndex = 1
    for pair in pairs:
        if (checkOrder(pair[0], pair[1]) == CORRECT):
            # print(pairIndex)
            # print(pair[0])
            # print(pair[1])
            sum += pairIndex

        pairIndex += 1

    print("Part 1: " + str(sum))


def part2():
    allPackets = [ item for pair in pairs for item in pair]
    allPackets.append([[2]])
    allPackets.append([[6]])

    # print("Original")
    # pprint(allPackets)
    allPackets.sort(key=cmp_to_key(checkOrder), reverse=True)
    # print("Sorted")
    # pprint(allPackets)

    index2 = allPackets.index([[2]]) + 1
    index6 = allPackets.index([[6]]) + 1

    print("Part 2: " + str(index2 * index6))


pairs = []
loadData('day13.dat')

part1()
part2()