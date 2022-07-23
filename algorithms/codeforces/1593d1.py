# https://codeforces.com/contest/1593/problem/D1

import sys
import itertools
import math
import functools

def sol(seq):
    s = set(seq)
    k = set()
    for (a, b) in itertools.combinations(s, 2):
        k.add(abs(a - b))
    if len(k) == 0:
        return -1
    return functools.reduce(math.gcd, k)

inp = [list(map(int, line.strip().split())) for line in sys.stdin]

for i in range(2, len(inp), 2):
    print(sol(inp[i]))