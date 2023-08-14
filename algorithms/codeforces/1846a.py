# https://codeforces.com/contest/1846/problem/A

import sys


inp = [line.strip() for line in sys.stdin]
r = 1
for _ in range(int(inp[0])):
    rows = int(inp[r])
    res = 0
    r += 1
    for i in range(rows):
        t1, t2 = map(int, inp[r].split())
        if t1 > t2:
            res += 1
        r += 1
    print(res)
