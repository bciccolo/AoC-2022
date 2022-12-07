from pprint import pprint


def calculateSize(file):
    size = file['size']

    for child in file['listing']:
        size += calculateSize(child)

    file['size'] = size

    return size


def createFile(name, size, listing, parent):
    file = {
        'name': name,
        'size': size,
        'listing': listing,
        'parent': parent
    }

    return file


def findCandidates(file, candidates, minSize):
    if (file['size'] >= minSize and len(file['listing']) > 0):
        candidates.append(file['size'])

    for child in file['listing']:
        findCandidates(child, candidates, minSize)


def loadData(dataFile):
    global root

    file = open(dataFile, 'r')
    lines = file.readlines()

    currentDirectory = root

    first = True

    for line in lines:
        # Skip the first line, we've already created the root directory
        if (first):
            first = False
            continue

        line = line.strip()

        # Instructions: either 'cd' or 'ls'
        if (line[0:1] == '$'):
            # cd: either move update a level in the hierarchy or create a new folder
            if (line[2:4] == 'cd'):
                name = line[5:]
                if (name == '..'):
                    currentDirectory = currentDirectory['parent']
                else:
                    file = createFile(name, 0, [], currentDirectory)
                    currentDirectory['listing'].append(file)
                    currentDirectory = file

                # print(currentDirectory['name'])

            # ls: nothing to do with this command (it's handled on the subsequent lines), just skip it
            else:
                pass
                # print('show contents of ' + currentDirectory['name'])

        # Directory listing (output of 'ls')
        else:
            output = line.split()
            # Skip directories because those are handled by the 'cd' command
            if (output[0] != 'dir'):
                file = createFile(output[1], int(output[0]), [], currentDirectory)
                currentDirectory['listing'].append(file)

    calculateSize(root)
    # pprint(root)


def part1():
    print("Part 1: " + str(sumSmallDirectories(root)))


def part2():
    spaceNeeded = 30000000 - (70000000 - root['size'])

    candidates = []
    findCandidates(root, candidates, spaceNeeded)

    candidates.sort()

    print("Part 2: " + str(candidates[0]))


def sumSmallDirectories(file):
    sum = 0

    if (file['size'] <= 100000 and len(file['listing']) > 0):
        # print('Adding directory ' + file['name'])
        sum += file['size']

    for child in file['listing']:
        sum += sumSmallDirectories(child)

    return sum


root = createFile('/', 0, [], None)
loadData('day7.dat')

part1()
part2()