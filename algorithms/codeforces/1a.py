# https://codeforces.com/problemset/problem/1/A

import math


def solution(n, m, a):
    return math.ceil(n / a) * math.ceil(m / a)


print(solution(*map(int, input().strip().split())))