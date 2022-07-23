# https://codeforces.com/problemset/problem/472/A

import math


def check(n):
    for k in range(2, math.ceil(n**0.5) + 2):
        if n % k == 0:
            return True
    return False

n = int(input())
if n % 2 == 0 and check(n//2):
    print(f"{n // 2} {n // 2}")
else:
    if check(n-4):
        print(f"{n-4} 4")
    elif check(n-6):
        print(f"{n-6} 6")
    elif check(n-8):
        print(f"{n-8} 8")