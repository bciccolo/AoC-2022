def findMarker(count):
    file = open('day6-snippet.dat', 'r')
    line = file.readline().strip()

    for i in range(len(line) - (count - 1)):
        chunk = line[i:i + count]

        unique = set([c for c in chunk])
        if (len(unique) == count):
            print(i + count)
            break


findMarker(4)
findMarker(14)