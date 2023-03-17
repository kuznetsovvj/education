# https://codeforces.com/problemset/problem/1234/A

import math


def check(seq):
    return math.ceil(sum(seq) / len(seq))

for _ in range(int(input())):
    input()
    print(check(tuple(map(int, input().split()))))
