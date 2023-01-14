# https://codeforces.com/problemset/problem/1702/A

import math


def check(n):
    b = int(math.log(n, 10))
    return n - 10**b

for _ in range(int(input())):
    print(check(int(input())))