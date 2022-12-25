# https://codeforces.com/problemset/problem/1520/D

from collections import defaultdict


def check(seq):
    d = defaultdict(int)
    res = 0
    for idx, item in enumerate(seq):
        d[item - idx] += 1
    for v in d.values():
        res += v * (v - 1) // 2
    return res


for _ in range(int(input())):
    input()
    seq = tuple(map(int, input().split()))
    print(check(seq))