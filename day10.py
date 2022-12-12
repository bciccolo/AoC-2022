import math
from pprint import pprint

def checkSignal(cycle, register):
    sample = 0

    if ((cycle - 20) % 40 == 0):
        sample = cycle * register

    return sample


def part1():
    cycle = 0
    registerX = 1
    signalStrength = 0

    file = open(dataFile, 'r')
    lines = file.readlines()
    for line in lines:
        parts = line.strip().split()

        if (parts[0] == 'addx'):
            cycle += 1
            signalStrength += checkSignal(cycle, registerX)

            cycle += 1
            signalStrength += checkSignal(cycle, registerX)

            registerX += int(parts[1])
        else: # 'noop'
            cycle += 1
            signalStrength += checkSignal(cycle, registerX)

    print('Part 1: ' + str(signalStrength))


def part2():
    crt = []
    for i in range(6):
        row = []
        for i in range(40):
            row.append('.')
        crt.append(row)

    cycle = 0
    registerX = 1
    signalStrength = 0

    file = open(dataFile, 'r')
    lines = file.readlines()
    for line in lines:
        parts = line.strip().split()

        if (parts[0] == 'addx'):
            cycle += 1
            signalStrength += checkSignal(cycle, registerX)
            updateCrt(crt, cycle, registerX)

            cycle += 1
            signalStrength += checkSignal(cycle, registerX)
            updateCrt(crt, cycle, registerX)

            registerX += int(parts[1])
        else: # 'noop'
            cycle += 1
            signalStrength += checkSignal(cycle, registerX)
            updateCrt(crt, cycle, registerX)

    print('Part 2:')
    for row in crt:
        print(''.join(row))


def updateCrt(crt, cycle, register):
    cycle -= 1
    row = math.floor(cycle / len(crt[0]))
    # print(str(cycle) + ' is in row ' + str(row))
    column = cycle % len(crt[0])
    if (abs(column - register) < 2):
        crt[row][column] = '#'


dataFile = 'day10.dat'

part1()
part2()