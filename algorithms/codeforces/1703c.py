# https://codeforces.com/problemset/problem/1703/C

from collections import Counter


def check(seq, codes):
    res = []
    for fn, code in zip(seq, codes):
        res.append((fn + code) % 10)
    return " ".join(map(str, res))


for _ in range(int(input())):
    n = int(input())
    codes = []
    seq = tuple(map(int, input().split()))
    for _ in range(n):
        _, w = input().strip().split()
        wc = Counter(w)
        up, dn = wc['D'], wc['U']
        codes.append(up - dn)
    print(check(seq, codes))