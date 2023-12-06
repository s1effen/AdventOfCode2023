import sys

def input(f):
    d = []
    times = []
    distances = []
    with open(f, "r") as f:
        for index,line in enumerate(f):
            if "Time" in line.strip():
                if line.strip():
                    times = list(filter(None, line.strip().split(' ')))[1:]
            elif "Distance" in line.strip():
                if line.strip():
                    distances = list(filter(None, line.strip().split(' ')))[1:]
            else:
                False
    for i in range(len(times)):
        d.append({"time":int(times[i]), "distance":int(distances[i])})

    return d

def input2(f):
    d = {}
    with open(f, "r") as f:
        for index,line in enumerate(f):
            if "Time" in line.strip():
                if line.strip():
                    d["time"] = int(line.strip().replace(' ','').split(':')[1])
            elif "Distance" in line.strip():
                if line.strip():
                    d["distance"] = int(line.strip().replace(' ','').split(':')[1])
            else:
                False
    return d

def race(speed,racetime):
    return speed * (racetime-speed)

def checkoptions(racedata):
    strategies = 0
    for i in range(racedata['time']):
        #print("The boat will race with {}, traveeling in total {} millimeters.".format(i, race(i,racedata['time'])))
        if race(i,racedata['time']) > racedata['distance']:
            strategies += 1
    return strategies



def part1(data):
    print("---------------------------\nPart1:\n---------------------------")
    answer = 1
    for d in data:
        answer *= checkoptions(d)
    print("Answer: {}".format(answer))

def part2(data):
    print("\n---------------------------\nPart2:\n---------------------------")
    print("Answer: {}".format(checkoptions(data)))

def run(day,test=False):
    if test:
        data1 = input("day" + day + "/test1.txt")
        data2 = input2("day" + day + "/test2.txt")
        part1(data1)
        part2(data2)
    else:
        data = input("day" + day + "/input.txt")
        data2 = input2("day" + day + "/input.txt")
        part1(data)
        part2(data2)