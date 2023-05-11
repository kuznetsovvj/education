# https://codeforces.com/contest/1829/problem/F

import sys
from collections import defaultdict


def check(n, vertex):
    d = defaultdict(int)
    for v in vertex:
        d[v[0]] += 1
        d[v[1]] += 1
    zero = 0
    for key, value in d.items():
        if value == 1:
            zero += 1
    x = n - zero - 1
    y = zero // x
    return f"{x} {y}"


input_ = tuple(tuple(map(int, line.strip().split())) for line in sys.stdin)
z = input_[0][0]
t, i = 1, 1 # номер набора входных данных, номер текущей строки
while t <= z:
    n, m = input_[i] # количество вершин, количество ребер
    i += 1
    print(check(n, input_[i:i+m]))
    i += m
    t += 1
