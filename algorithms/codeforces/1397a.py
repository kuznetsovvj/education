# https://codeforces.com/problemset/problem/1397/A

from collections import defaultdict

def check(words):
    x = defaultdict(int)
    for w in words:
        for i in w:
            x[i] += 1
    res = True
    for v in x.values():
        if v % len(words) != 0:
            res = False
    if res:
        return "YES"
    return "NO"

for _ in range(int(input())):
    seq = []
    for _ in range(int(input())):
        seq.append(input())
    print(check(seq))
