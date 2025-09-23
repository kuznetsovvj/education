# https://adventofcode.com/2024/day/2

from copy import copy

def check(seq):
    if seq[1] > seq[0]:
        up = True
    else:
        up = False
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


print("result: ", r)



