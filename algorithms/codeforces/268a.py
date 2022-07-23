# https://codeforces.com/problemset/problem/268/A

import sys
from collections import defaultdict
input = sys.stdin.readline

t = int(input())
d1, d2 = defaultdict(int), defaultdict(int)

for tt in range(t):
    x, y = map(int, input().split())
    d1[x] += 1
    d2[y] += 1

res = 0
for k in d1.keys():
    res += d1[k] * d2[k]

print(res)