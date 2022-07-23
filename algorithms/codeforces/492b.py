# https://codeforces.com/problemset/problem/492/B

import math


_, l = map(int, input().split())
seq = list(map(int, input().split()))

seq.sort()
m = seq[0]
for i in range(1, len(seq)):
    m = max(m, (seq[i] - seq[i-1]) / 2)
m = max(m, l - seq[-1])
print(m)