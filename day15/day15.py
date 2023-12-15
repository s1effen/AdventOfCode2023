import sys


def input(f):
    d = []
    with open(f, "r") as f:
        for index, line in enumerate(f):
            if line.strip():
                d = line.strip().split(',')
            else:
                False
    return d


def hashit(s: str):
    val = 0
    for c in s:
        val += ord(c)
        val *= 17
        val %= 256
    # print("{} -> {}".format(s,val))
    return val


def printboxes(boxes):
    if boxes:
        for i, box in enumerate(boxes):
            if box:
                print("Box {}: {}".format(i, box))


def processstep(boxes: list, step: str):
    #print("Step ", step)
    if '=' in step:
        label, focal = step.split('=')
        boxnum = hashit(label)
        for lensnum, lens in enumerate(boxes[boxnum]):
            if label in lens:
                boxes[boxnum][lensnum] = step.replace('=', ' ')
                return boxes
        boxes[boxnum].append(step.replace('=', ' '))
        return boxes
    elif '-' in step:
        label = step.split('-')[0]
        boxnum = hashit(label)
        if boxes[boxnum]:
            for pos, lens in enumerate(boxes[boxnum]):
                if label in lens:
                    boxes[boxnum].pop(pos)
                    return boxes
        return boxes

def focuspower(boxes):
    power = 0
    for boxnum, box in enumerate(boxes):
        for lensnum, lens in enumerate(box):
            power += (1 + boxnum) * (lensnum +1) * int(lens.split(' ')[1])
    return power
def part1(data):
    print("---------------------------\nPart1:\n---------------------------")
    answer = 0
    for d in data:
        answer += hashit(d)
    print("Answer: {}".format(answer))


def part2(data):
    print("\n---------------------------\nPart2:\n---------------------------")
    boxes = []
    for i in range(256):
        boxes.append([])
    for d in data:
        boxes = processstep(boxes, d)
        #printboxes(boxes)
    print("Answer: {}".format(focuspower(boxes)))


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
