# https://codeforces.com/contest/1669/problem/B

import sys
from collections import Counter


def solution(seq):
    c = Counter(seq)
    t = c.most_common(1)
    if t[0][1] >= 3:
        return t[0][0]
    return -1



inp = [list(map(int, line.strip().split())) for line in sys.stdin]
for i in range(2, len(inp), 2):
    print(solution(inp[i]))