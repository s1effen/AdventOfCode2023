import sys
import time

def input(f):
    d = []
    with open(f, "r") as f:
        for index,line in enumerate(f):
            if line.strip():
                d.append(list(map(lambda x: int(x), line.strip().split(' '))))
            else:
                False
    return d

def difference(row):
    new = [' ']*(len(row)-1)
    while ' ' in new:
        for i in range(len(row)-1):
            new[i] = row[i+1] - row[i]
    #print("Difference for {} is {}".format(row, new))
    return new
def extrapolate(history, backwards=False):
    for i in range(len(history)-2,-1,-1):
        if backwards:
            history[i].insert(0,history[i][0] - history[i+1][0])
        else:
            history[i].append(history[i][-1] + history[i+1][-1])
    return history[0][0]

def part1(data):
    print("---------------------------\nPart1:\n---------------------------")
    start_time = time.time()
    answer = 0
    for d in data:
        history = [d]
        go = True
        while go:
            new = difference(history[-1])
            if len(set(new)) != 1:
                history.append(new)
            else:
                history.append(new)
                history[-1].append(history[-1][-1])
                answer += extrapolate(history)
                go = False
    end_time = time.time()
    print("Answer: {}".format(answer))
    print("Execution took {} milliseconds".format((end_time-start_time)* 1000))
def part2(data):
    print("\n---------------------------\nPart2:\n---------------------------")
    start_time = time.time()
    answer = 0
    for d in data:
        history = [d]
        go = True
        while go:
            new = difference(history[-1])
            if len(set(new)) != 1:
                history.append(new)
            else:
                history.append(new)
                history[-1].insert(0,history[-1][-1])
                answer += extrapolate(history,backwards=True)
                go = False
    end_time = time.time()
    print("Answer: {}".format(answer))
    print("Execution took {} seconds".format((end_time-start_time)* 1000))

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

