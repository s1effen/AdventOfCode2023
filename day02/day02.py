import sys

def input(f):
    d = []
    with open(f, "r") as f:
        for index,line in enumerate(f):
            if line.strip():
                game = []
                g = line.strip().split(':')[1].split(';')
                for h in g:
                    h = h.split(',')
                    hand = {}
                    for c in h:
                        hand[ c.split(' ')[2]] = int(c.split(' ')[1])
                        game.append(hand)
                d.append(game)
            else:
                False
    return d

def possible(game, bag):
    for hand in game:
        for color in hand.keys():
            if hand[color] > bag[color]:
                return False
    return True

def minimum(game):
    minimum = {}
    for hand in game:
        for color in hand.keys():
            if color in minimum:
                if hand[color] > minimum[color]:
                    minimum[color] = hand[color]
            else:
                minimum[color] = hand[color]
    return minimum

def part1(data):
    print("---------------------------\nPart1:\n---------------------------")
    bag = {"red":12, "green":13,"blue":14}
    answer = 0
    for id,game in enumerate(data):
        if possible(game, bag):
            answer += id +1


    print("Answer: {}".format(answer))
def part2(data):
    print("\n---------------------------\nPart2:\n---------------------------")
    answer = 0
    for id, game in enumerate(data):
        m = minimum(game)
        answer += m["red"] * m["green"] * m["blue"]
    print("Answer: {}".format(answer))

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

