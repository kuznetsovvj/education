# https://codeforces.com/contest/1506/problem/A

import math


def sol(n, m, x):
    row = x % n
    if not row:
        row = n
    col = math.ceil(x / n)
    return (row - 1) * m + col

t = int(input())
for tt in range(t):
    n, m, x = map(int, input().strip().split())
    print(sol(n, m, x))