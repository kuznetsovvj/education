# https://codeforces.com/problemset/problem/1473/B

import math


def check(w1, w2):
    l = (len(w1) * len(w2)) // math.gcd(len(w1), len(w2))
    for i in range(l):
        if w1[i % len(w1)] != w2[i % len(w2)]:
            return -1
    return w1 * (l // len(w1))

for _ in range(int(input())):
    w1, w2 = input().strip(), input().strip()
    print(check(w1, w2))