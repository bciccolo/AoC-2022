class Monkey:
    def __init__(self, items, operator, operand, divisor, truePass, falsePass):
        self.inspectCount = 0
        self.items = items
        self.operator = operator
        self.operand = operand
        self.divisor = divisor
        self.truePass = truePass
        self.falsePass = falsePass

    def inspectAndThrow(self, monkeys, reduceWorry):
        for worry in self.items:
            self.inspectCount += 1

            match self.operator:
                case '+':
                    worry += self.operand
                case '*':
                    worry *= self.operand
                case '^':
                    worry = worry ** self.operand

            if (reduceWorry):
                worry = int(worry / 3)

            if worry % self.divisor == 0:
                monkeys[self.truePass].items.append(worry)
            else:
                monkeys[self.falsePass].items.append(worry)

            self.items = self.items[1:]

def part1():
    # print('Before:')
    # for monkey in monkeys:
    #     print(monkey.items)

    for i in range(20):
        for monkey in monkeys:
            monkey.inspectAndThrow(monkeys, True)

    # print('After:')
    # for monkey in monkeys:
    #     print(monkey.items)

    inspections = []
    for monkey in monkeys:
        inspections.append(monkey.inspectCount)

    inspections.sort(reverse=True)
    product = inspections[0] * inspections[1]

    print("Part 1: " + str(product))


# Test data
# monkeys = [
#     Monkey([79, 98],         '*', 19, 23, 2, 3),
#     Monkey([54, 65, 75, 74], '+', 6,  19, 2, 0),
#     Monkey([79, 60, 97],     '^', 2,  13, 1, 3),
#     Monkey([74],             '+', 3,  17, 0, 1)
# ]

# Full data
monkeys = [
    Monkey([77, 69, 76, 77, 50, 58],         '*', 11, 5, 1, 5),
    Monkey([75, 70, 82, 83, 96, 64, 62],     '+', 8, 17, 5, 6),
    Monkey([53],                             '*', 3, 2,  0, 7),
    Monkey([85, 64, 93, 64, 99],             '+', 4, 7,  7, 2),
    Monkey([61, 92, 71],                     '^', 2, 3,  2, 3),
    Monkey([79, 73, 50, 90],                 '+', 2, 11, 4, 6),
    Monkey([50, 89],                         '+', 3, 13, 4, 3),
    Monkey([83, 56, 64, 58, 93, 91, 56, 65], '+', 5, 19, 1, 0)
]

part1()
