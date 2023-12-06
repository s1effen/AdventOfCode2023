import sys
import threading
import time

locations = []


def input(f):
    d = {'categories': []}
    newcategory = False
    with open(f, "r") as f:
        for index, line in enumerate(f):
            if "seeds: " in line:
                d["seeds"] = [int(i) for i in line.strip()[7:].split()]
            elif line.strip() == "":
                newcategory = True
            elif newcategory:
                d["categories"].append(line.strip().split(' ')[0])
                d[d["categories"][-1]] = []
                newcategory = False
            else:
                nums = line.strip().split(' ')
                nums = [int(i) for i in nums]
                # print("Add numbers: {}".format(nums))
                d[d["categories"][-1]].append(nums)
    return d


def almanac(categories, seed):
    for category in categories["categories"]:
        start = seed
        for line in categories[category]:
            #print("From {} to {} maps {} to {}".format(line[1], line[1] + line[2] - 1, line[0], line[0] + line[2] - 1))
            if line[1] <= seed < (line[1] + line[2]):
                offset = seed - line[1]
                #print("{} -> {} ({})".format(seed, line[0] + offset, category))
                seed = line[0] + offset
                break
        #print("{} -> {} ({})".format(start, seed, category))
    return seed

def part1(data):
    print("---------------------------\nPart1:\n---------------------------")
    start_time = time.time()
    locations = []
    for seed in data['seeds']:
        locations.append(almanac(data, seed))
        #print("{} maps to {}".format(seed, locations[-1]))
        #print("")
    end_time = time.time()
    print("Answer: {}".format(min(locations)))
    print("Execution took {} milliseconds".format((end_time-start_time)* 1000))

def seedbatch(threadname, begin, end, data):
    minlocation = sys.maxsize
    for s in range(begin,end):
        if ((s - begin) % 1000000) == 0:
            print("{} Processed {:,} seeds.".format(threadname,s - begin))
        location = almanac(data, s)
        if location < minlocation:
            minlocation = location
    print("{} Processed {:,} seeds.".format(threadname, end - begin))
    locations.append(minlocation)
def part2(data):
    print("\n---------------------------\nPart2:\n---------------------------")
    start_time = time.time()
    minlocation = sys.maxsize
    for i in range(0,len(data['seeds']),2):
        print("\n---------------> Next seed from {:,} to {:,} ({:,})\n".format(data['seeds'][i],data['seeds'][i]+data['seeds'][i+1],data['seeds'][i]+data['seeds'][i+1]-data['seeds'][i]))
        numthreads = 16
        threads = []
        windowsize = int((data['seeds'][i]+data['seeds'][i+1]-data['seeds'][i]) /numthreads)
        #print("Windowsize is {}",format(windowsize))
        for n in range(numthreads):
            begin = data['seeds'][i] + n * windowsize
            if n == numthreads-1:
                end = data['seeds'][i]+data['seeds'][i+1]
            else:
                end = (data['seeds'][i] + n * windowsize) + windowsize
            print("Start Thread {} with {:,} to {:,} ({:,})".format(n+1,begin,end,end-begin))
            threads.append(threading.Thread(target=seedbatch, args=("Thread " + str(n+1),begin, end, data)))
            threads[-1].start()
        for thread in threads:
            thread.join()
    end_time = time.time()
    print("Answer: {}".format(min(locations)))
    print("Execution took {:,} seconds".format((end_time-start_time)))

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
