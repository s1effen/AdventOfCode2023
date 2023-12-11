
import sys
import time

def input(f,expand=1):
    d = {}
    galaxies = 1
    yexpand = 0
    rows = 0
    columns = set()
    with open(f, "r") as f:
        for y,line in enumerate(f):
            rows += 1
            if line.strip() == '.'*len(line.strip()):
                print("Expand line {}!".format(y))
                yexpand += expand
            for x, o in enumerate(line.strip()):
                if o == '#':
                    columns.add(x)
                    d[galaxies] = [y+yexpand,x]
                    columns.add(x)
                    galaxies += 1
    for i in range(rows-1,-1,-1):
        if i not in columns:
            print("Expand row {}!".format(i))
            for galaxy in d.keys():
                if d[galaxy][1] > i:
                    d[galaxy][1] += expand
    return d

def distance(galaxy1,galaxy2):
    #print("From {} to {}: {}".format(galaxy1,galaxy2, abs(galaxy2[0] - galaxy1[0]) + abs(galaxy2[1] - galaxy1[1])))
    return abs(galaxy2[0] - galaxy1[0]) + abs(galaxy2[1] - galaxy1[1])

def part1(data):
    print("---------------------------\nPart1:\n---------------------------")
    start_time = time.time()
    pairs = [(a, b) for idx, a in enumerate(list(data.values())) for b in list(data.values())[idx + 1:]]
    answer = 0
    for pair in pairs:
        answer += distance(pair[0],pair[1])
    end_time = time.time()
    print("Answer: {}".format(answer))
    print("Execution took {} milliseconds".format((end_time-start_time)* 1000))
def part2(data):
    print("\n---------------------------\nPart2:\n---------------------------")
    start_time = time.time()
    pairs = [(a, b) for idx, a in enumerate(list(data.values())) for b in list(data.values())[idx + 1:]]
    answer = 0
    for pair in pairs:
        answer += distance(pair[0],pair[1])
    end_time = time.time()
    print("Answer: {}".format(answer))
    print("Execution took {} seconds".format((end_time-start_time)* 1000))

def run(day,test=False):
    if test:
        data1 = input("day" + day + "/test1.txt")
        part1(data1)
        data2 = input("day" + day + "/test1.txt", expand=100-1)
        part2(data2)
    else:
        data = input("day" + day + "/input.txt")
        part1(data)
        data = input("day" + day + "/input.txt", expand=1000000-1)
        part2(data)

