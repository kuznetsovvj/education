# https://codeforces.com/problemset/problem/1658/A

import sys


def solution(line):
    zero, one, add = 0, 0, 0
    for item in line:
        if item == '1':
            one += 1
        else:
            zero += 1
        if zero >= one:
            one += 1
            add += 1
    return add


input_ = [line.strip() for line in sys.stdin]

for i in range(2, len(input_), 2):
    print(solution(input_[i]))