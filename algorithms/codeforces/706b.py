# https://codeforces.com/problemset/problem/706/B

import bisect


input()
seq = list(map(int, input().split()))
seq.sort()
t = int(input())
for _ in range(t):
    z = int(input())
    print(bisect.bisect_right(seq, z))