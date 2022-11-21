# https://codeforces.com/problemset/problem/474/B

# Двоичный поиск

from itertools import accumulate
from bisect import bisect_left

def check(seq, reqs):
    result = tuple(accumulate(seq))
    for req in reqs:
        print(bisect_left(result, req) + 1)

input()
seq = tuple(map(int, input().split()))
input()
reqs = tuple(map(int, input().split()))
check(seq, reqs)