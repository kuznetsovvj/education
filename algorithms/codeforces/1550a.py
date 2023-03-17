# https://codeforces.com/problemset/problem/1550/A

import math


def check(n):
    return math.ceil(n ** 0.5)

for _ in range(int(input())):
    print(check(int(input())))