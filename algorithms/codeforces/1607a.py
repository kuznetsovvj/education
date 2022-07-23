# https://codeforces.com/contest/1607/problem/A

import sys


def sol(dic, wrd):
    d = dict()
    for idx, item in enumerate(dic):
        d[item] = idx
    res = 0
    for i in range(1, len(wrd)):
        res += abs(d[wrd[i]] - d[wrd[i-1]])
    return res


inp = [line.strip() for line in sys.stdin]

for i in range(1, len(inp), 2):
    print(sol(inp[i], inp[i+1]))