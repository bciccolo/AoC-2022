from pprint import pprint
from queue import Queue
import itertools

DATA_FILE = 'day16-snippet.dat'

class Valve:
    def __init__(self, name, flowRate, tunnels, open):
        self.name = name
        self.flowRate = flowRate
        self.tunnels = tunnels
        self.open = open

valves = []

# Cache for distances between two valves
distanceMaps = {}

def chooseNextValve(startValve):
    nextValve = None
    nextSteps = 0

    for valve in valves:
        if not valve.open and valve.flowRate > 0:
            steps = distanceMaps[startValve.name][valve.name]

            nextPerformance = 0 if nextValve is None else nextValve.flowRate
            thisPerformance = valve.flowRate
            if steps < nextSteps:
                thisPerformance += (nextSteps - steps) * valve.flowRate
            elif nextSteps < steps and nextPerformance > 0:
                nextPerformance += (steps - nextSteps) * nextValve.flowRate

            if nextValve is None or thisPerformance > nextPerformance:
                nextValve = valve
                nextSteps = steps

    return nextValve


# This version of a Breadth-First Search algorithm was created by AskPython.com
# (https://www.askpython.com/python/examples/distance-between-nodes-unweighted-graph)
def leastDistance(graph, source):
    Q = Queue()
    # create a dictionary with large distance(infinity) of each vertex from source
    distance = {k: 9999999 for k in graph.keys()}
    visited_vertices = set()
    Q.put(source)
    visited_vertices.update({0})
    while not Q.empty():
        vertex = Q.get()
        if vertex == source:
            distance[vertex] = 0
        for u in graph[vertex]:
            if u not in visited_vertices:
                # update the distance
                if distance[u] > distance[vertex] + 1:
                    distance[u] = distance[vertex] + 1
                Q.put(u)
                visited_vertices.update({u})
    return distance


def loadData():
    graph = {}

    file = open(DATA_FILE, 'r')
    lines = file.readlines()
    for line in lines:
        line = line.strip()

        # Sample line of input:
        # Valve AA has flow rate=0; tunnels lead to valves DD, II, BB

        name = line[6:8]

        flowRate = int(line[line.find('=') + 1: line.find(';')])

        tunnelIndex = line.find(' valves ')
        if tunnelIndex > -1:
            tunnelIndex += 8
        else:
            tunnelIndex = line.find(' valve ') + 7
        tunnels = line[tunnelIndex:].split(', ')

        valves.append(Valve(name, flowRate, tunnels, False))

        graph[name] = tunnels

    for valve in valves:
        distanceMaps[valve.name] = leastDistance(graph, valve.name)


def part1():
    timer = 30
    totalPressure = 0
    currentValve = valves[0]

    while timer > 0 and currentValve:
        valve = chooseNextValve(currentValve)

        if valve:
            steps = distanceMaps[currentValve.name][valve.name]

            timer -= steps  # Time to reach valve
            timer -= 1      # Time to open valve

            totalPressure += timer * valve.flowRate

            print('Opening valve ' + valve.name + ' at minute ' + str(30 - timer) + ' with flow rate ' + str(valve.flowRate) + ', net release ' + str(timer * valve.flowRate))

            valve.open = True

        currentValve = valve

    print('Part 1: ' + str(totalPressure))


loadData()
part1()