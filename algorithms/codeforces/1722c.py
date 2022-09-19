# https://codeforces.com/contest/1722/problem/C

from collections import defaultdict


def check(s1, s2, s3):
    wds = defaultdict(int)
    wds = words(wds, s1)
    wds = words(wds, s2)
    wds = words(wds, s3)
    return f"{cnt(wds, s1)} {cnt(wds, s2)} {cnt(wds, s3)}"


def words(wds, s):
    for w in s.split(' '):
        wds[w] += 1
    return wds

def cnt(wds, s):
    res = 0
    for w in s.split(' '):
        if wds[w] == 1:
            res += 3
        if wds[w] == 2:
            res += 1
    return res

t = int(input())
for _ in range(t):
    input()
    s1, s2, s3 = input(), input(), input()
    print(check(s1, s2, s3))