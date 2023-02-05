# https://codeforces.com/contest/1791/problem/D

from collections import defaultdict

def check(seq):
    c1, c2 = defaultdict(int), defaultdict(int)
    c1[seq[0]] += 1
    for i in range(1, len(seq)):
        c2[seq[i]] += 1
    res = len(c1.keys()) + len(c2.keys())
    for i in range(1, len(seq) - 1):
        c1[seq[i]] += 1
        c2[seq[i]] -= 1
        if c2[seq[i]] == 0:
            del c2[seq[i]]
        res = max(res, len(c1.keys()) + len(c2.keys()))
    return res

for _ in range(int(input())):
    input()
    print(check(input().strip()))