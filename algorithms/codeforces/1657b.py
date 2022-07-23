# https://codeforces.com/problemset/problem/1657/B

import sys


def solution(n, B, x, y):
    crt, res = 0, 0
    for _ in range(n):
        if crt + x <= B:
            crt += x
        else:
            crt -= y
        res += crt
    return res


input_ = [list(map(int, line.strip().split())) for line in sys.stdin]

for i in range(1, len(input_)):
    print(solution(*input_[i]))