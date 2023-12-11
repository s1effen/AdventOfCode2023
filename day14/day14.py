import sys
import time

def input(f):
    d = []
    with open(f, "r") as f:
        for index,line in enumerate(f):
            if line.strip():
                d.append(line.strip())
            else:
                False
    return d

def part1(data):
    print("---------------------------\nPart1:\n---------------------------")
    start_time = time.time()
    for d in data:
        True
    end_time = time.time()
    print("Answer: {}".format(42))
    print("Execution took {} milliseconds".format((end_time-start_time)* 1000))
def part2(data):
    print("\n---------------------------\nPart2:\n---------------------------")
    start_time = time.time()
    for d in data:
        True
    end_time = time.time()
    print("Answer: {}".format(42))
    print("Execution took {} seconds".format((end_time-start_time)* 1000))

def run(day,test=False):
    if test:
        data1 = input("day" + day + "/test1.txt")
        data2 = input("day" + day + "/test1.txt")
        part1(data1)
        part2(data2)
    else:
        data = input("day" + day + "/input.txt")
        part1(data)
        part2(data)

