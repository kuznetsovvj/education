# https://codeforces.com/contest/1579/problem/B

import sys


def sol(seq):
    s = 0
    res = []
    while s < len(seq):
        l = seq.index(min(seq[s:]), s)
        if l != s:
            res.append((s + 1, l + 1, l - s))
            seq = seq[:s] + [seq[l]] + seq[s:l] + seq[l+1:]
        s += 1
    print(len(res))
    for item in res:
        print(f"{item[0]} {item[1]} {item[2]}")


inp = [list(map(int, line.strip().split())) for line in sys.stdin]

for i in range(2, len(inp), 2):
    sol(inp[i])