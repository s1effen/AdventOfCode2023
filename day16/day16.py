import sys
from operator import add

def input(f):
    d = []
    with open(f, "r") as f:
        for index,line in enumerate(f):
            if line.strip():
                d.append(list(line.strip()))
            else:
                False
    return d

dirs = [0,1,2,3]
def direction(contraption, beams):
    for beam in beams:
        if beam["pos"][0] == len(contraption) or beam["pos"][0] < 0 or beam["pos"][1] == len(contraption[0]) or beam["pos"][1] < 0:
            beams.remove(beam)
            continue
        if contraption[beam["pos"][0]][beam["pos"][1]] == '.':
            beam["dir"] = beam["dir"]
            beam = move(beam)
        elif contraption[beam["pos"][0]][beam["pos"][1]] == '/':
            if beam["dir"] == 1 or beam["dir"] == 2:
                beam["dir"] = (beam["dir"] - 1) % 4
            else:
                if beam["dir"] == 0 or beam["dir"] == 3:
                    beam["dir"] = (beam["dir"] + 1) % 4
            beam = move(beam)
        elif contraption[beam["pos"][0]][beam["pos"][1]] == '\\':
            if beam["dir"] == 1 or beam["dir"] == 2:
                beam["dir"] = (beam["dir"] + 1) % 4
            else:
                if beam["dir"] == 0 or beam["dir"] == 3:
                    beam["dir"] = (beam["dir"] - 1) % 4
            beam = move(beam)
        elif contraption[beam["pos"][0]][beam["pos"][1]] == '-':
            if beam["dir"] == 1 or beam["dir"] == 3:
                beam["dir"] = beam["dir"]
                beam = move(beam)
            else:
                beam["dir"] = dirs[(beam["dir"] + 1) % 4]
                print("New dir {}".format(beam["dir"]))
                beam = move(beam)
                beams.insert(0, {"dir":dirs[(beam["dir"] - 2) % 4],"pos":beam["pos"]})
                beams[0] = move(beams[0])
        elif contraption[beam["pos"][0]][beam["pos"][1]] == '|':
            if beam["dir"] == 0 or beam["dir"] == 2:
                beam["dir"] = beam["dir"]
                beam = move(beam)
            else:
                beam["dir"] = dirs[(beam["dir"] + 1) % 4]
                beam = move(beam)
                beams.insert(0, {"dir":dirs[(beam["dir"] -2) % 4],"pos":beam["pos"]})
                beams[0] = move(beams[0])
    return beams

def printcontraption(contraption, beams):
    for y,l in enumerate(contraption):
        for x,c in enumerate(l):
            for beam in beams:
                here = False
                if beam["pos"] == [y,x]:
                    here = True
                    break
            if here:
                print('*', end="")
            else:
                print(c, end="")
        print("")
    print("")
def move(beam):
    if dirs[beam["dir"]] == 1:
        beam["pos"] =  list(map(add, beam["pos"], [0, 1]))
    elif dirs[beam["dir"]] == 3:
        beam["pos"] = list(map(add, beam["pos"], [0, -1]))
    elif dirs[beam["dir"]] == 2:
        beam["pos"] = list(map(add, beam["pos"], [1, 0]))
    elif dirs[beam["dir"]] == 0:
        beam["pos"] = list(map(add, beam["pos"], [-1, 0]))
    return beam
def beam(contraption, beams):
   for i in range(100):
        print(beams)
        printcontraption(contraption, beams)
        beams = direction(contraption, beams)

beams = [{"dir":1,"pos":[0,0]}]
def part1(data):
    print("---------------------------\nPart1:\n---------------------------")
    beam(data,beams)
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

