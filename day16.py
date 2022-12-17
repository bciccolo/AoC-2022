from collections import namedtuple
from pprint import pprint

DATA_FILE = 'day16-snippet.dat'

Valve = namedtuple('Valve', ['name', 'flowRate', 'tunnels'])
valves= []

def loadData():
    file = open(DATA_FILE, 'r')
    lines = file.readlines()
    for line in lines:
        line = line.strip()

        # Sample line of input: Valve AA has flow rate=0; tunnels lead to valves DD, II, BB

        name = line[6:8]

        flowRate = int(line[line.find('=') + 1: line.find(';')])

        tunnelIndex = line.find(' valves ')
        if tunnelIndex > -1:
            tunnelIndex += 9
        else:
            tunnelIndex = line.find(' valve ') + 8
        tunnels = line[tunnelIndex:].split(', ')

        valves.append(Valve(name, flowRate, tunnels))

    pprint(valves)


def part1():
    pass


loadData()
part1()