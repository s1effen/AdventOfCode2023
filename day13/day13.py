import sys
import numpy as np

def input(f):
    d = []
    temp = []
    with open(f, "r") as f:
        for index,line in enumerate(f):
            if line.strip() != "":
                temp.append(list(line.strip()))
            else:
                d.append(np.array(temp))
                temp = []
    d.append(np.array(temp))
    return d

def smudge(field):
    unchanged = checkmirror(field, 'h'), checkmirror(field, 'v')
    for x in range(field.shape[1]):
        for y in range(field.shape[0]):
            fieldcopy = field.copy()
            if field[y][x] == '#':
                fieldcopy[y][x] = '.'
            else:
                fieldcopy[y][x] = '#'
            changed = checkmirror(fieldcopy, 'h'), checkmirror(fieldcopy, 'v')
            if changed[0] > 0 and changed[0] != unchanged[0]:
                print("Old: {} New: {}".format(unchanged, changed))
                print(max(changed))
                return changed[0]*100
            if changed[1] > 0 and changed[1] != unchanged[1]:
                print("Old: {} New: {}".format(unchanged, changed))
                print(max(changed))
                return changed[1]
    print("No new reflection found")
    return 0

def checkmirror(field,direction='v'):
    if direction == 'v':
        for i in range(1,field.shape[1]):
            if i < field.shape[1]/2:
                l = i
            else:
                l = field.shape[1] - i
            #print("Left with mirror at {} position {} with size {}:\n {}".format(i,direction,l,field[:, i-l:i]))
            #print("Right with mirror at {} position {} with size {}:\n {}".format(i,direction ,l,np.flip(field[:, i:i+l],1)))
            if np.array_equal(field[:, i-l:i],np.flip(field[:, i:i+l],1)):
                #print("Vertical reflection between {} and {}".format(i,i+1))
                return i
    if direction == 'h':
        for i in range(1, field.shape[0]):
            if i < field.shape[0] / 2:
                l = i
            else:
                l = field.shape[0] - i
            #print("Top with mirror at {} position {} with size {}:\n {}".format(i,direction,l,field[i-l:i,:]))
            #print("Bottom with mirror at {} position {} with size {}:\n {}".format(i,direction ,l,np.flip(field[i:i+l,:],0)))
            if np.array_equal(field[i - l:i, :], np.flip(field[i:i + l,:], 0)):
                #print("Horizontal reflection between {} and {}".format(i, i + 1))
                return i
    return 0

def part1(data):
    print("---------------------------\nPart1:\n---------------------------")
    answer = 0
    for d in data:
        answer += checkmirror(d,direction='v')
        answer += checkmirror(d,direction='h')*100
    print("Answer: {}".format(answer))

def part2(data):
    print("\n---------------------------\nPart2:\n---------------------------")
    answer = 0
    for d in data:
       answer += smudge(d)
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

