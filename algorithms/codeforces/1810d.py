# https://codeforces.com/contest/1810/problem/D

import math


def check(seq):
    # диапазон значений по умолчанию
    h_min, h_max = 1, 10**18
    res = []
    for cmd in seq:
        if cmd[0] == 1:
            a, b, n = cmd[1:]
            if n == 1:
                c_min = 1
            else:
                c_min = a * (n - 1) - b * (n - 2) + 1
            c_max = n * a - (n - 1) * b
            if h_max < c_min or c_max < h_min or c_min > c_max:
                res.append(0)
            else:
                h_min = max(c_min, h_min)
                h_max = min(c_max, h_max)
                res.append(1)
        else:
            a, b = cmd[1:]
            n_min = max(1, (h_min - b + (a - b) - 1) // (a - b))
            n_max = max(1, (h_max - b + (a - b) - 1) // (a - b))
            if n_min == n_max:
                res.append(n_min)
            else:
                res.append(-1)
    return " ".join(map(str, res))

for _ in range(int(input())):
    q = int(input())
    input_ = []
    for t in range(q):
        seq = tuple(map(int, input().split()))
        input_.append(seq)
    print(check(input_))