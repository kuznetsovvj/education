# https://codeforces.com/problemset/problem/1684/B

import math


def sol(a, b, c):
    y, z = b, c
    n = math.ceil((z - a) // y) + 1
    x = n * y + a
    return f"{x} {y} {z}"


t = int(input())
for tt in range(t):
    print(sol(*tuple(map(int, input().split()))))