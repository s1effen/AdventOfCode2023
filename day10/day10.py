import sys
import time


def rplace(c):
    if c == '|':  # a vertical pipe connecting north and south.
        return '║'
    elif c == '-':  # a horizontal pipe connecting east and west.
        return '═'
    elif c == 'L':  # a 90-degree bend connecting north and east.
        return '╚'
    elif c == 'J':  # a 90-degree bend connecting north and west.
        return '╝'
    elif c == '7':  # a 90-degree bend connecting south and west.
        return '╗'
    elif c == 'F':  # a 90-degree bend connecting south and east.
        return '╔'
    elif c == '.':  # ground; there is no pipe in this tile.
        return '.'
    elif c == 'S':  # the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
        return 'S'
    return c


def measure(plan, start, step):
    go = [['u'], ['d'], ['l'], ['r']]
    pos = [start] * 4
    run = True
    while run:
        step += 1
        for i in range(len(go)):
            if go[i]:
                plan, nextpos, nextgo = direction(plan, pos[i], go[i].pop(0), step)
                go[i].append(nextgo)
                pos[i] = nextpos
        run = False
        for i in range(len(go)):
            if go[i][0]:
                run = True
    max = 0
    for row in plan:
        for p in row:
            if str(p).isdigit() and p > max:
                max = p
    return max

def measure2(plan, start, step):
    go = [['u'], ['d'], ['l'], ['r']]
    pos = [start] * 4
    plan[start[1]][start[0]] = 1
    run = True
    while run:
        for i in range(len(go)):
            if go[i]:
                plan, nextpos, nextgo = direction2(plan, pos[i], go[i].pop(0))
                go[i].append(nextgo)
                pos[i] = nextpos
        run = False
        for i in range(len(go)):
            if go[i][0]:
                run = True
    print("")
    printpipes(plan)
    print("")
    enclosed = 0
    for row in plan:
        inside = False
        for p in row:
            if str(p).isdigit():
                if p != '═':
                    if inside:
                        print(')', end="")
                    else:
                        print('(', end="")
                    inside = not inside
                else:
                    print('(', end="")
            else:
                if inside:
                    enclosed += 1
                    print('I', end="")
                else:
                    print('O', end="")
        print("")
    return enclosed

def direction(plan, pos, dir, step):
    if dir == 'u':
        if pos[1] - 1 >= 0:
            pos = [a + b for a, b in zip(pos, (0, -1))]
            if plan[pos[1]][pos[0]] == '║':
                plan[pos[1]][pos[0]] = step
                return plan, pos, 'u'
            elif plan[pos[1]][pos[0]] == '╔':
                plan[pos[1]][pos[0]] = step
                return plan, pos, 'r'
            elif plan[pos[1]][pos[0]] == '╗':
                plan[pos[1]][pos[0]] = step
                return plan, pos, 'l'
    if dir == 'd':
        if pos[1] + 1 < len(plan):
            pos = [a + b for a, b in zip(pos, (0, 1))]
            if plan[pos[1]][pos[0]] == '║':
                plan[pos[1]][pos[0]] = step
                return plan, pos, 'd'
            elif plan[pos[1]][pos[0]] == '╝':
                plan[pos[1]][pos[0]] = step
                return plan, pos, 'l'
            elif plan[pos[1]][pos[0]] == '╚':
                plan[pos[1]][pos[0]] = step
                return plan, pos, 'r'
    if dir == 'l':
        if pos[0] - 1 >= 0:
            pos = [a + b for a, b in zip(pos, (-1, 0))]
            if plan[pos[1]][pos[0]] == '═':
                plan[pos[1]][pos[0]] = step
                return plan, pos, 'l'
            elif plan[pos[1]][pos[0]] == '╔':
                plan[pos[1]][pos[0]] = step
                return plan, pos, 'd'
            elif plan[pos[1]][pos[0]] == '╚':
                plan[pos[1]][pos[0]] = step
                return plan, pos, 'u'
    if dir == 'r':
        if pos[0] + 1 < len(plan[0]):
            pos = [a + b for a, b in zip(pos, (1, 0))]
            if plan[pos[1]][pos[0]] == '═':
                plan[pos[1]][pos[0]] = step
                return plan, pos, 'r'
            elif plan[pos[1]][pos[0]] == '╝':
                plan[pos[1]][pos[0]] = step
                return plan, pos, 'u'
            elif plan[pos[1]][pos[0]] == '╗':
                plan[pos[1]][pos[0]] = step
                return plan, pos, 'd'
    return plan, pos, ''


def direction2(plan, pos, dir):
    if dir == 'u':
        if pos[1] - 1 >= 0:
            pos = [a + b for a, b in zip(pos, (0, -1))]
            if plan[pos[1]][pos[0]] == '║':
                return plan, pos, 'u'
            elif plan[pos[1]][pos[0]] == '╔':
                return plan, pos, 'r'
            elif plan[pos[1]][pos[0]] == '╗':
                return plan, pos, 'l'
    if dir == 'd':
        if pos[1] + 1 < len(plan):
            pos = [a + b for a, b in zip(pos, (0, 1))]
            if plan[pos[1]][pos[0]] == '║':
                return plan, pos, 'd'
            elif plan[pos[1]][pos[0]] == '╝':
                return plan, pos, 'l'
            elif plan[pos[1]][pos[0]] == '╚':
                return plan, pos, 'r'
    if dir == 'l':
        if pos[0] - 1 >= 0:
            pos = [a + b for a, b in zip(pos, (-1, 0))]
            if plan[pos[1]][pos[0]] == '═':
                plan[pos[1]][pos[0]] = '#'
                return plan, pos, 'l'
            elif plan[pos[1]][pos[0]] == '╔':
                return plan, pos, 'd'
            elif plan[pos[1]][pos[0]] == '╚':
                return plan, pos, 'u'
    if dir == 'r':
        if pos[0] + 1 < len(plan[0]):
            pos = [a + b for a, b in zip(pos, (1, 0))]
            if plan[pos[1]][pos[0]] == '═':
                plan[pos[1]][pos[0]] = '#'
                return plan, pos, 'r'
            elif plan[pos[1]][pos[0]] == '╝':
                return plan, pos, 'u'
            elif plan[pos[1]][pos[0]] == '╗':
                return plan, pos, 'd'
    return plan, pos, ''

def input(f):
    d = []
    start = []
    with open(f, "r") as f:
        for y, line in enumerate(f):
            d.append([] * len(line))
            for x, l in enumerate(line.strip()):
                d[y].append(rplace(l))
                if l == 'S':
                    start = [x, y]
            else:
                False
    return start, d


def printpipes(plan):
    for y, line in enumerate(plan):
        for x, l in enumerate(line):
            print(l, end="")
        print("")


def part1(start, data):
    print("---------------------------\nPart1:\n---------------------------")
    start_time = time.time()
    printpipes(data)
    answer = measure(data, start, 0)
    #printpipes(data)
    end_time = time.time()
    print("Answer: {}".format(answer))
    print("Execution took {} milliseconds".format((end_time - start_time) * 1000))


def part2(start, data):
    print("\n---------------------------\nPart2:\n---------------------------")
    start_time = time.time()
    printpipes(data)
    answer = measure2(data, start, 0)
    end_time = time.time()
    print("Answer: {}".format(answer))
    print("Execution took {} seconds".format((end_time - start_time) * 1000))


def run(day, test=False):
    if test:
        start1, data1 = input("day" + day + "/test1.txt")
        start2, data2 = input("day" + day + "/test2.txt")
        part1(start1, data1)
        part2(start2, data2)
    else:
        start, data = input("day" + day + "/input.txt")
        part1(start, data)
        part2(start, data)
