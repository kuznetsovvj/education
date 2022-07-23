# https://codeforces.com/contest/1593/problem/A

import sys
from collections import Counter


def sol(seq):
    c = Counter(seq)
    m = max(seq)
    if c[m] > 1:
        mult = True
    else:
        mult = False
    res = []
    for item in seq:
        if item == m:
            if mult:
                res.append(1)
            else:
                res.append(0)
        else:
            res.append(m - item + 1)
    return ' '.join(map(str, res))


inp = [tuple(map(int, line.strip().split())) for line in sys.stdin]

for i in range(1, len(inp)):
    print(sol(inp[i]))