def findSignal(length):
    count = 0

    file = open('day6.dat', 'r')
    lines = file.readlines()
    buffer = lines[0]

    signal = ''
    for letter in buffer:
        count = count + 1

        if (letter in signal):
            # Remove as much of the signal as necessary to remove the duplicated letter
            index = signal.index(letter)
            # print("Removing from " + str(index) + ": " + signal[index+1:])
            signal = signal[index + 1:]

            # Add the letter
            signal = signal + letter
        elif (len(signal) == length - 1):
            break
        else:
            signal = signal + letter

        # print(signal + ': ' + str(count))

    return count


def part1():
    print("Part 1: " + str(findSignal(4)))


def part2():
    print("Part 1: " + str(findSignal(14)))


part1()
part2()