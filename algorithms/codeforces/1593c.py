# https://codeforces.com/contest/1593/problem/C

import sys


def sol(n, seq):
    dst = [n - item for item in seq]
    dst.sort(reverse=True)
    sm, t = 0, 0
    while sm < n:
        if len(dst) > 0:
            v = dst.pop()
            if sm + v < n:
                sm += v
                t += 1
            else:
                break
        else:
            break
    return t


inp = [list(map(int, line.strip().split())) for line in sys.stdin]

for i in range(1, len(inp), 2):
    n, _ = inp[i]
    seq = inp[i+1]
    print(sol(n, seq))