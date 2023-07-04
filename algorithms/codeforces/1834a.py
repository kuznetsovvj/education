# https://codeforces.com/contest/1834/problem/A

import math


def check(seq):
    p, n = 0, 0
    for i in seq:
        if i == -1:
            n += 1
        else:
            p += 1
    if p >= n:
        if n % 2 == 0:
            return 0
        return 1
    d = math.ceil((n - p) / 2)
    if (n - d) % 2 == 0:
        return d
    return d + 1   


for _ in range(int(input())):
    input()
    print(check(tuple(map(int, input().split()))))


assert check([1]) == 0
assert check([1, 1, -1]) == 1
assert check([1, 1, 1, -1, -1]) == 0
assert check([-1, -1]) == 2
assert check([-1, -1, -1]) == 3
assert check([-1, -1, -1, 1]) == 1
