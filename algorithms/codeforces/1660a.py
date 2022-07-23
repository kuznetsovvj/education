# https://codeforces.com/problemset/problem/1660/A

import sys


def solution(x, y):
    if x != 0:
        return 2*y + x + 1
    return 1


input_ = [list(map(int, line.strip().split())) for line in sys.stdin]

for i in range(1, len(input_)):
    print(solution(*input_[i]))