# https://codeforces.com/problemset/problem/1657/A

import sys


def solution(x, y):
    if x == 0 and y == 0:
        return 0
    if (x**2 + y**2)**0.5 % 1 == 0:
        return 1
    return 2


input_ = [list(map(int, line.strip().split())) for line in sys.stdin]

for i in range(1, len(input_)):
    print(solution(*input_[i]))
