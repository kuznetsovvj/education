# https://codeforces.com/contest/1611/problem/B

import sys


def solution(a, b):
    if a == b:
        return a // 2
    a, b = min(a, b), max(a, b)
    n = (b - a) // 2
    if n >= a:
        return a
    else:
        return n + (a - n) // 2

inp = [tuple(map(int, line.strip().split())) for line in sys.stdin]

for i in range(1, len(inp)):
    print(solution(*inp[i]))