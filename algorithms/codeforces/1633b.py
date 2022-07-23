# https://codeforces.com/problemset/problem/1633/B

import sys
from collections import Counter


def solution(seq):
    c = Counter(seq)
    if c['1'] > c['0']:
        return c['0']
    if c['0'] > c['1']:
        return c['1']
    else:
        return c['0'] - 1


inp = [line.strip() for line in sys.stdin]
for i in range(1, len(inp)):
    print(solution(inp[i]))