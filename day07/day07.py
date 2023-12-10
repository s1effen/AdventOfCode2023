import sys
import time


def input(f):
    d = []
    with open(f, "r") as f:
        for index, line in enumerate(f):
            if line.strip():
                d.append({"hand": list(line.strip().split(' ')[0]), "bid": int(line.strip().split(' ')[1])})
            else:
                False
    return d


def count(iterable):
    return sum(1 for _ in iterable)


def getstrenght(hand,debug=False):
    strength = 0
    check = set(hand)
    if len(check) == 1:  # 5 of a kind: 1
        if debug:
            print("{} is 5 of a kind.".format(''.join(str(x) for x in hand)))
        return 7
    elif len(list(check)) == 2:  # 4 of a kind or  Full House
        if hand.count(list(check)[0]) == 4 or hand.count(list(check)[1]) == 4:  # 4 of a kind
            if debug:
                print("{} is 4 of a kind.".format(''.join(str(x) for x in hand)))
            return 6
        else:  # Full House
            if debug:
                print("{} is Full House.".format(''.join(str(x) for x in hand)))
            return 5
    elif len(check) == 3:
        if hand.count(list(check)[0]) == 2 or hand.count(list(check)[1]) == 2:  # two pair
            if debug:
                print("{} is two pair.".format(''.join(str(x) for x in hand)))
            return 3
        else:  # 3 of a kind
            if debug:
                print("{} is 3 of a kind.".format(''.join(str(x) for x in hand)))
            return 4
    elif len(check) == 4:  # one pair
        if debug:
            print("{} is one pair.".format(''.join(str(x) for x in hand)))
        return 2
    elif len(check) == 5:  # High card
        if debug:
            print("{} is high card.".format(''.join(str(x) for x in hand)))
        return 1
    return strength


def getjokerstrenght(hand):
    s = getstrenght(hand,debug=False)
    for card in set(hand):
        if card != 1: #joker
            temp = getstrenght(numtocard(list(map(lambda x: card if x == 1 else x, hand)),joker=True),debug=False)
            if temp > s:
                s = temp
    return s


def cardtonum(hand, joker=False):
    rep = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10}
    if joker:
        rep['J'] = 1
    for c, card in enumerate(hand):
        if card in rep.keys():
            hand[c] = rep[card]
        else:
            hand[c] = int(card)
    return hand


def numtocard(hand, joker=False):
    rep = {14: 'A', 13: 'K', 12: 'Q', 11: 'J', 10: 'T'}
    if joker:
        rep[1] = 'J'
    for c, card in enumerate(hand):
        if card in rep.keys():
            hand[c] = rep[card]
        else:
            hand[c] = int(card)
    return hand


def rank(hands, joker=False):
    for hand in hands:
        hand['hand'] = cardtonum(hand['hand'], joker=joker)
    if joker:
        hands = sorted(hands, key=lambda x: (
        getjokerstrenght(x['hand']), x['hand'][0], x['hand'][1], x['hand'][2], x['hand'][3], x['hand'][4]))
    else:
        hands = sorted(hands, key=lambda x: (
        getstrenght(x['hand']), x['hand'][0], x['hand'][1], x['hand'][2], x['hand'][3], x['hand'][4]))
    for hand in hands:
        hand['hand'] = numtocard(hand['hand'], joker=joker)
    return hands


def part1(data):
    print("---------------------------\nPart1:\n---------------------------")
    start_time = time.time()
    answer = 0
    data = rank(data)
    for i, hand in enumerate(data):
        answer += (i + 1) * hand['bid']
    end_time = time.time()
    print("Answer: {}".format(answer))
    print("Execution took {} milliseconds".format((end_time - start_time) * 1000))

def part2(data):
    print("\n---------------------------\nPart2:\n---------------------------")
    start_time = time.time()
    answer = 0
    data = rank(data, joker=True)
    for i, hand in enumerate(data):
        answer += (i + 1) * hand['bid']
    end_time = time.time()
    print("Answer: {}".format(answer))
    print("Execution took {} seconds".format((end_time - start_time) * 1000))


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
