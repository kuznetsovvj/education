# https://codeforces.com/contest/1839/problem/0

import math


def check(n, k):
    return math.ceil((n-1) / k) + 1

for _ in range(int(input())):
    print(check(*map(int, input().split())))