# https://codeforces.com/problemset/problem/1335/C

from collections import Counter


def check(seq):
    mx = max(seq.values())
    ks = len(seq.keys())
    if mx < ks:
        return mx
    if mx == ks:
        return ks - 1
    return ks

for _ in range(int(input())):
    input()
    seq = Counter(map(int, input().split()))
    print(check(seq))