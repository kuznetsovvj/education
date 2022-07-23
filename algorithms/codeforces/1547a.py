# https://codeforces.com/contest/1547/problem/A

import sys


def sol(a, b, f):
    if a[0] == b[0] and a[0] == f[0] and f[1] < max(a[1], b[1]) and f[1] > min(a[1], b[1]):
        return abs(a[1] - b[1]) + 2
    if a[1] == b[1] and a[1] == f[1] and f[0] < max(a[0], b[0]) and f[0] > min(a[0], b[0]):
        return abs(a[0] - b[0]) + 2
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


t = int(input())
for tt in range(t):
    input()
    a = tuple(map(int, input().strip().split()))
    b = tuple(map(int, input().strip().split()))
    f = tuple(map(int, input().strip().split()))
    print(sol(a, b, f))