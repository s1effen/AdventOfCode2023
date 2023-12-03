import sys

def input(f):
    d = []
    with open(f, "r") as f:
        for index,line in enumerate(f):
            if line.strip():
                d.append(list(line.strip()))
            else:
                False
    return d

def symbol(c):
    return not (c.isdigit() or c == '.')


def isGear(schematic, x, y):
    if x > 0:
        xFrom = x-1
    else:
        xFrom = x
    if y > 0:
        yFrom = y-1
    else:
        yFrom = y

    if x == len(schematic[0])-1:
        xTo = x
    else:
        xTo = x+1
    if y == len(schematic)-1:
        yTo = y
    else:
        yTo = y+1
    num = 0
    line = 0
    for y2 in range(yFrom,yTo+1):
        lin = ''.join(schematic[y2][xFrom:xTo + 1])
        #print(lin)
        #print(" ")
        if line == 0 or line == 2:
            if lin != '...': #num
                if lin[1] != '.': #one num like 777
                    #print("one num")
                    num += 1
                else:
                    if lin[0].isdigit():
                        num += 1
                    if lin[2].isdigit():
                        num += 1
        else: #middle line
            if lin[0].isdigit():
                num += 1
            if lin[2].isdigit():
                num +=1
        #print("Number of parts: {}", format(num))
        line += 1
    #print("Number of parts: {}",format(num))
    return num == 2

def adjacentSymbols(schematic, x,y):
    if x > 0:
        xFrom = x-1
    else:
        xFrom = x
    if y > 0:
        yFrom = y-1
    else:
        yFrom = y

    if x == len(schematic[0])-1:
        xTo = x
    else:
        xTo = x+1
    if y == len(schematic)-1:
        yTo = y
    else:
        yTo = y+1

    for y2 in range(yFrom,yTo+1):
        for x2 in range(xFrom, xTo+1):
            #print(schematic[y2][x2],end="")
            if symbol(schematic[y2][x2]):
                #print("")
                return True
        #print("")
    return False

def part1(data):
    print("---------------------------\nPart1:\n---------------------------")
    answer = 0
    for y in range(0,len(data)):
        number = []
        symbolFound = False
        for x in range(0,len(data[0])):
            print("x:{},y:{} -> {}".format(x,y, data[y][x]))
            if data[y][x].isdigit():
                print("{} is a digit".format(data[y][x]))
                number.append(data[y][x])
                if not symbolFound:
                    symbolFound = adjacentSymbols(data,x,y)
            elif symbolFound:
                if number:
                    print("Number with adj symbol is {}".format(int(''.join(number))))
                    answer += int(''.join(number))
                number = []
                symbolFound = False
            else: #No digit, no adj symbol
                number = []
        if symbolFound and number:
            print("Number with adj symbol is {}".format(int(''.join(number))))
            answer += int(''.join(number))
    print("Answer: {}".format(answer))

def part2(data):
    print("\n---------------------------\nPart2:\n---------------------------")
    answer = 0
    for y in range(0, len(data)):
        number = []
        for x in range(0, len(data[0])):
            if data[y][x] == '*':
                print("x:{},y:{} -> {}".format(x, y, data[y][x]))
                if isGear(data, x, y):
                    data[y][x] = 'G'
                else:
                    data[y][x] = '.'
            elif symbol(data[y][x]):
                data[y][x] = '.'

    numbers = []
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
                    numbers.append(int(''.join(number)))
                    #answer += int(''.join(number))
                number = []
                symbolFound = False
            else:  # No digit, no adj symbol
                number = []
        if symbolFound and number:
            #print("Number with adj symbol is {}".format(int(''.join(number))))
            numbers.append(int(''.join(number)))
            #answer += int(''.join(number))
    print(numbers)
    for i in range(0,int(len(numbers)/2)+1,2):
        answer += numbers[i]*numbers[i+1]
    print("Answer: {}".format(answer))

def run(day,test=False):
    if test:
        data1 = input("day" + day + "/test1.txt")
        data2 = input("day" + day + "/test2.txt")
        part1(data1)
        part2(data2)
    else:
        data = input("day" + day + "/input.txt")
        part1(data)
        part2(data)

