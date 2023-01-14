# https://codeforces.com/problemset/problem/1527/A

import math


def check(n):
    z = int(math.log(n, 2))
    return 2**z - 1

for _ in range(int(input())):
    print(check(int(input())))