# https://codeforces.com/contest/1851/problem/C

from collections import defaultdict


def check(n, k, seq):
    s, i, cnt = seq[0], 1, 1
    while cnt < k and i != n:
        if seq[i] == s:
            cnt += 1
        i += 1
    if cnt < k:
        return "NO"
    f = seq[-1]
    if s == f:
        return "YES"
    cnt = 0
    while cnt < k and i != n:
        if seq[i] == f:
            cnt += 1
        i += 1
    if cnt < k:
        return "NO"
    return "YES"

for _ in range(int(input())):
    n, k = map(int, input().split())
    seq = tuple(map(int, input().split()))
    print(check(n, k, seq))