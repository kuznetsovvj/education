# https://codeforces.com/problemset/problem/119/A

import math


a, b, n = map(int, input().split())
sem = True

while 1: 
    if sem:
        m = math.gcd(a, n)
        if m > n:
            print("1")
            break
        else:
            n -= m
            sem = not sem
    else:
        m = math.gcd(b, n)
        if m > n:
            print('0')
            break
        else:
            n -= m
            sem = not sem

