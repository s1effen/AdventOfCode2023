import sys


def input(f):
    # Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
    d = {}
    with open(f, "r") as f:
        for index, line in enumerate(f):
            if line.strip():
                card = line.strip().split(': ')[1].split(' | ')
                card = list(map(lambda x: x.split(' '), card))
                card[0] = list(filter(lambda a: a != '', card[0]))
                card[1] = list(filter(lambda a: a != '', card[1]))
                d[int(line.strip().split(': ')[0].replace('Card ', ''))] = [1, card]
            else:
                False
    return d


def part1(data):
    print("---------------------------\nPart1:\n---------------------------")
    answer = 0
    for d in data.values():
        points = 0
        for n in d[1][1]:
            if n in d[1][0]:
                if points == 0:
                    points = 1
                else:
                    points = points * 2
        answer += points
    print("Answer: {}".format(answer))


def part2(data):
    print("\n---------------------------\nPart2:\n---------------------------")
    answer = 0
    # iterate over cards by number
    for i in range(1, len(data)):
        #print("Card {}".format(i))
        matches = 0
        for num in data[i][1][1]:
            if num in data[i][1][0]:
                matches += 1
        for m in range(i + 1, i + 1 + matches):
            data[m][0] += data[i][0]  # copy card
    for card in data.values():
        answer += card[0]
    print("Answer: {}".format(answer))


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
