# https://codeforces.com/contest/1669/problem/F

import operator
from itertools import accumulate
import sys
import math


def solution(seq):
    max_ = math.floor(sum(seq) / 2)
    alice = [item for item in list(accumulate(seq, operator.add)) if item <= max_]
    bob = [item for item in list(accumulate(seq[::-1], operator.add)) if item <= max_]
    k, j = len(alice) - 1, len(bob) - 1
    while k >= 0 and j >= 0:
        if alice[k] == bob[j] and k + j < len(seq):
            return k + j + 2
        else:
            if k + j >= len(seq):
                k -= 1
                j -= 1
                continue
            if alice[k] > bob[j]:
                k -= 1
            else:
                j -= 1
    return 0


inp = [list(map(int, line.strip().split())) for line in sys.stdin]
for i in range(2, len(inp), 2):
    print(solution(inp[i]))