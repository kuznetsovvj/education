# https://codeforces.com/problemset/problem/230/B

import math

def check(n):
    if n == 1:
        return 'NO'
    s = math.floor(n**0.5)
    if s**2 != n:
        return 'NO'

    for i in range(2, math.floor(s**0.5)+2):
        if s % i == 0 and i != s:
            return 'NO'
    return 'YES'

input()
seq = tuple(map(int, input().split()))
for item in seq:
    print(check(item))