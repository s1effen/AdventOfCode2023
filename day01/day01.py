import sys

data = []


def input(f):
    d = []
    with open(f, "r") as f:
        for index, line in enumerate(f):
            if line.strip():
                d.append(line.strip())
            else:
                False
    return d


def part1(data):
    print("---------------------------\nPart1:\n---------------------------")
    calibration = 0
    for d in data:
        first = -1
        last = -1
        for i in range(1, int(len(d)) + 1):
            if first == -1 and d[i - 1].isdigit():
                # print(d[i-1])
                first = d[i - 1]
            if last == -1 and d[-i].isdigit():
                # print(d[-i])
                last = d[-i]
            if first != -1 and last != -1:
                print("Calibration value is {}{}".format(first, last))
                calibration += int("{}{}".format(first, last))
                break
    print("Answer: {}".format(calibration))

def part2(data):
    print("\n---------------------------\nPart2:\n---------------------------")
    calibration = 0
    digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for d in data:
        first = -1
        last = -1
        #print(d)
        for i in range(1, int(len(d)) + 1):
            val = str(d[0:i])
            #print("val from left {}".format(val))
            if first == -1:
                if val[-1].isdigit():
                    first = d[i - 1]
                    #print("set first to {}".format(first))
                else:
                    for idx,n in enumerate(digits):
                        if val.find(n) != -1:
                            first = idx +1

            val = str(d[-i:])
            #print("val from right {}".format(val))
            if last == -1:
                if val[0].isdigit():
                    last = d[-i]
                    #print("set last to {}".format(first))
                else:
                    for idx,n in enumerate(digits): #Reverse
                        if val.rfind(n) != -1:
                            last = idx +1
            if first != -1 and last != -1:
                print("Calibration value is {}{}".format(first, last))
                calibration += int("{}{}".format(first, last))
                break
    print("Answer: {}".format(calibration))

def run(day, test=False):
    if test:
        data1 = input("day" + day + "/test1.txt")
        data2 = input("day" + day + "/test2.txt")
        part1(data1)
        part2(data2)
    else:
        data = input("day" + day + "/input.txt")
        part1(data)
        part2(data)
