# https://codeforces.com/problemset/problem/1535/B

import math


def check(seq):
    r1, r2 = [], []
    for item in seq:
        if item % 2 == 0:
            r1.append(item)
        else:
            r2.append(item)
    r = 0
    seq = r1 + r2
    for i in range(len(seq)):
        for j in range(i+1, len(seq)):
            if seq[i] % 2 == 0 and seq[j] % 2 == 0:
                r += 1
            else:
                if math.gcd(seq[i], 2*seq[j]) > 1:
                    r += 1
    return r

for _ in range(int(input())):
    input()
    print(check(tuple(map(int, input().split()))))