# https://codeforces.com/contest/1669/problem/D

import sys


def solution(seq):
    for item in seq:
        if len(item) == 0:
            continue
        if len(item) == 1:
            return 'NO'
        b, r = 0, 0
        for i in item:
            if i == 'R':
                r += 1
            else:
                b += 1
        if b == 0 or r == 0:
            return 'NO'
    return 'YES'


inp = [line.strip().split('W') for line in sys.stdin]
for i in range(2, len(inp), 2):
    print(solution(inp[i]))