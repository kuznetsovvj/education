# https://adventofcode.com/2024/day/2

from copy import deepcopy

def check(seq):
    if seq[1] > seq[0]:
        up = True
    elif seq[1] < seq[0]:
        up = False
    else:
        return False
    for i in range(1, len(seq)):
        if abs(seq[i] - seq[i-1]) > 3 or seq[i] == seq[i-1]:
            return False
        if up:
            if seq[i] - seq[i-1] < 0:
                return False
        else:
            if seq[i] - seq[i-1] > 0:
                return False
    return True

with open(r'input\02.txt', 'r') as file:
    r = 0
    for line in file.readlines():
        seq = list(map(int, line.strip().split(' ')))
        if check(seq):
            r += 1
        else:
            t = deepcopy(seq)
            del t[0]
            if check(t):
                r += 1
                continue
            t = deepcopy(seq)
            del t[1]
            if check(t):
                r += 1
                continue
            t = deepcopy(seq)
            del t[2]
            if check(t):
                r += 1
                continue
            t = deepcopy(seq)
            del t[3]
            if check(t):
                r += 1
                continue
            t = deepcopy(seq)
            del t[4]
            if check(t):
                r += 1
                continue


print("result: ", r)



