# https://codeforces.com/contest/1807/problem/E

import sys


def resolv():
    n = int(input())
    seq = tuple(map(int, input().split()))

    l, r = 1, n
    while l != r:
        t = (l + r) // 2
        print(f"? {t - l + 1} {' '.join(map(str, range(l, t+1)))}")
        sys.stdout.flush()
        s = int(input())
        if s != sum(seq[l-1:t]):
            r = t
        else:
            l = t + 1
    print(f"! {l}")
    sys.stdout.flush()


for i in range(int(input())):
    resolv()
