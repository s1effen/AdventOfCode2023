import sys
import time

def puzzleinput(f):
    instructions = ""
    network = {}
    with open(f, "r") as f:
        for index,line in enumerate(f):
            if line.strip():
                if index == 0:
                    instructions = line.strip()
                else:
                    line = line.strip().replace("= (",'').replace(',','').replace(')','').split(' ')
                    network[line[0]] = [line[1],line[2]]
            else:
                False
    return instructions, network

def loopcheck(start, locations, step, loops):
    print("Loopcheck start:{}, locations:{}, step:{}, loops:{}".format(start, locations, step, loops))
    if step > 1:
        for i, location in enumerate(locations):
            if step not in loops:
                if location == start[i]:
                    loops[i] = step
                    print("Loop len for {} is {}".format(i, step))
    return True
def part1(instructions, network):
    print("---------------------------\nPart1:\n---------------------------")
    start_time = time.time()
    location = "AAA"
    step = 0
    print("started at {}".format(location))
    while location != "ZZZ":
        if instructions[step % len(instructions)] == 'R':
            location = network[location][1]
        elif instructions[step % len(instructions)] == 'L':
            location = network[location][0]
        step += 1
        print("went to {}".format(location))
    print("arrived at {} with {} steps".format("ZZZ",step))
    end_time = time.time()
    print("Answer: {}".format(step))
    print("Execution took {} milliseconds".format((end_time-start_time)* 1000))
def part2(instructions, network):
    print("\n---------------------------\nPart2:\n---------------------------")
    start_time = time.time()
    locations = []
    for location in network.keys():
        if location[2] == "A":
            locations.append(location)
    step = 0
    loops = [] * len(locations)
    start = []
    print("started at {}".format(locations))
    while loopcheck(start, locations, step, loops):
        if instructions[step % len(instructions)] == 'R':
            for i in range(len(locations)):
                locations[i] = network[locations[i]][1]
        elif instructions[step % len(instructions)] == 'L':
            for i in range(len(locations)):
                locations[i] = network[locations[i]][0]
        if step == 0:
            start = locations
        step += 1
        if step % 1000000 == 0:
            print("step {} on {}".format(step, locations))
    end_time = time.time()
    print("Answer: {}".format(42))
    print("Execution took {} seconds".format((end_time-start_time)* 1000))

def run(day,test=False):
    if test:
        instructions, network = puzzleinput("day" + day + "/test1.txt")
        instructions2, network2 = puzzleinput("day" + day + "/test2.txt")
        part1(instructions, network)
        part2(instructions2, network2)
    else:
        instructions, network = puzzleinput("day" + day + "/input.txt")
        part1(instructions, network)
        part2(instructions, network)