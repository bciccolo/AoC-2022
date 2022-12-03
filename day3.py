def findBadge(group):
    for letter in group[0]:
        if letter in group[1] and letter in group[2]:
            return letter


def findDuplicate(word1, word2):
    for letter in word1:
        if letter in word2:
            return letter


def getPriority(letter):
    priority = ord(letter)

    if (priority > 96): # lowercase
        priority -= 96
    else:               # uppercase
        priority -= 38

    return priority


def part1():
    sum = 0

    file = open('day3.dat', 'r')
    lines = file.readlines()

    for line in lines:
        line = line.strip()
        half = int(len(line) / 2)
        c1 = line[:half]
        c2 = line[half:]

        letter = findDuplicate(c1, c2)
        sum += getPriority(letter)

    print("Part 1: " + str(sum))


def part2():
    sum = 0

    file = open('day3.dat', 'r')
    lines = file.readlines()

    group = []
    counter = 0
    for line in lines:
        line = line.strip()

        if (counter > 0 and counter % 3 == 0):
            letter = findBadge(group)
            sum += getPriority(letter)
            group.clear()

        group.append(line)
        counter = counter + 1

    # Check the last group
    letter = findBadge(group)
    sum += getPriority(letter)

    print("Part 1: " + str(sum))


part1()
part2()