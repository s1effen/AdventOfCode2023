import sys
from math import prod


def input(f):
    d = []
    with open(f, "r") as f:
        for index, line in enumerate(f):
            if line.strip():
                d.append(list(line.strip()))
            else:
                False
    return d


def symbol(c):
    return not (c.isdigit() or c == '.')


def getNumber(schematic, x, y):
    # print("get number from {}{}: {}".format(x,y, schematic[x][y]))
    number = [schematic[x][y]]

    # left
    i = 1
    while y - i >= 0 and schematic[x][y - i].isdigit():
        number.insert(0, schematic[x][y - i])
        i += 1

    # right
    j = 1
    while y + j < len(schematic[0]) and schematic[x][y + j].isdigit():
        number.append(schematic[x][y + j])
        j += 1

    return int(''.join(number))


def isGear(schematic, x, y):
    if x > 0:
        xFrom = x - 1
    else:
        xFrom = x
    if y > 0:
        yFrom = y - 1
    else:
        yFrom = y

    if x == len(schematic[0]) - 1:
        xTo = x
    else:
        xTo = x + 1
    if y == len(schematic) - 1:
        yTo = y
    else:
        yTo = y + 1
    nums = []
    line = 0
    for y2 in range(yFrom, yTo + 1):
        lin = ''.join(schematic[y2][xFrom:xTo + 1])
        # print(lin)
        # print(" ")
        if line == 0 or line == 2:
            if lin != '...':  # num
                if lin[1] != '.':  # one num like 777
                    nums.append(getNumber(schematic, y2, xFrom + 1))
                else:
                    if lin[0].isdigit():
                        nums.append(getNumber(schematic, y2, xFrom))
                    if lin[2].isdigit():
                        nums.append(getNumber(schematic, y2, xTo))
        else:  # middle line
            if lin[0].isdigit():
                nums.append(getNumber(schematic, y2, xFrom))
            if lin[2].isdigit():
                nums.append(getNumber(schematic, y2, xTo))
        # print("Number of parts: {}", format(num))
        line += 1
    #print("Number of parts: {}".format(len(nums)))
    if len(nums) == 2:
        #print("Sum {}".format(nums[0] * nums[1]))
        return nums[0] * nums[1]
    return 0


def adjacentSymbols(schematic, x, y):
    if x > 0:
        xFrom = x - 1
    else:
        xFrom = x
    if y > 0:
        yFrom = y - 1
    else:
        yFrom = y

    if x == len(schematic[0]) - 1:
        xTo = x
    else:
        xTo = x + 1
    if y == len(schematic) - 1:
        yTo = y
    else:
        yTo = y + 1

    for y2 in range(yFrom, yTo + 1):
        for x2 in range(xFrom, xTo + 1):
            # print(schematic[y2][x2],end="")
            if symbol(schematic[y2][x2]):
                # print("")
                return True
        # print("")
    return False


def printgrid(data):
    for y in range(0, len(data)):
        for x in range(0, len(data[0])):
            print(data[y][x], end="")
        print("")
    print("")


def part1(data):
    print("---------------------------\nPart1:\n---------------------------")
    answer = 0
    for y in range(0, len(data)):
        number = []
        symbolFound = False
        for x in range(0, len(data[0])):
            #print("x:{},y:{} -> {}".format(x, y, data[y][x]))
            if data[y][x].isdigit():
                #print("{} is a digit".format(data[y][x]))
                number.append(data[y][x])
                if not symbolFound:
                    symbolFound = adjacentSymbols(data, x, y)
            elif symbolFound:
                if number:
                    #print("Number with adj symbol is {}".format(int(''.join(number))))
                    answer += int(''.join(number))
                number = []
                symbolFound = False
            else:  # No digit, no adj symbol
                number = []
        if symbolFound and number:
            #print("Number with adj symbol is {}".format(int(''.join(number))))
            answer += int(''.join(number))
    print("Answer: {}".format(answer))


def part2(data):
    print("\n---------------------------\nPart2:\n---------------------------")
    answer = 0
    numbers = []
    for y in range(0, len(data)):
        number = []
        for x in range(0, len(data[0])):
            if data[y][x] == '*':
                #print("x:{},y:{} -> {}".format(x, y, data[y][x]))
                answer += isGear(data, x, y)
    print("Answer: {}".format(answer))


def run(day, test=False):
    if test:
        data1 = input("day" + day + "/test1.txt")
        data2 = input("day" + day + "/test1.txt")
        part1(data1)
        part2(data2)
    else:
        data = input("day" + day + "/input.txt")
        part1(data)
        part2(data)
