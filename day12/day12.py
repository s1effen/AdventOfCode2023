import sys

def count(row: list, item):
    return sum(1 for i in row if i == item)

def solve(line):
    print("{} with {} unknown springs and pattern to check {}".format(line[0], count(line[0], '?'), line[1]))





def input(f):
    d = []
    with open(f, "r") as f:
        for index,line in enumerate(f):
            if line.strip():
                d.append(line.strip().split(' '))
                d[-1][1] = list(map(lambda x: int(x), d[-1][1].split(',')))
            else:
                False
    return d

def part1(data):
    print("---------------------------\nPart1:\n---------------------------")
    for d in data:
        solve(d)
    print("Answer: {}".format(42))

def part2(data):
    print("\n---------------------------\nPart2:\n---------------------------")
    for d in data:
        True
    print("Answer: {}".format(42))

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

