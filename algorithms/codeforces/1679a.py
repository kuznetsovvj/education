# https://codeforces.com/problemset/problem/1679/A

import math


def sol(n):
    if n % 2 == 1 or n < 4:
        return -1
    if n % 6 != 0:
        mn = n // 6 + 1
    else:
        mn = n // 6
    return f"{mn} {n // 4}"

t = int(input())
for tt in range(t):
    print(sol(int(input())))