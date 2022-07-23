# https://codeforces.com/contest/1607/problem/C

import sys

def sol(seq):
    seq.sort()
    res, dlt, mn = seq[0], 0, seq[0]
    for i in range(1, len(seq)):
        dlt += mn
        mn = seq[i] - dlt
        res = max(res, mn)
    return res

inp = [list(map(int, line.strip().split())) for line in sys.stdin]

for i in range(2, len(inp), 2):
    print(sol(inp[i]))