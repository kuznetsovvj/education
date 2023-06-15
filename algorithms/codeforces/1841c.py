# https://codeforces.com/contest/1841/problem/C

from itertools import chain

def check(w):
    mx = calc(w)
    first = {}
    last = {}
    for i in range(len(w)):
        if w[i] not in first:
            first[w[i]] = i
        if len(first.keys()) == 5:
            break
    for i in range(len(w)-1, -1, -1):
        if w[i] not in last:
            last[w[i]] = i
        if len(last.keys()) == 5:
            break
    for j in chain(first.values(), last.values()):
        for i in ["A", "B", "C", "D", "E"]:
            mx = max(mx, calc(w[:j]+f"{i}"+w[j+1:]))
    return mx


def calc(w):
    s = {"A":1, "B":10, "C":100, "D":1000, "E":10000}
    res = 0
    current = ord("A") - 1
    for i in range(len(w)-1,-1,-1):
        if ord(w[i]) >= current:
            res += s[w[i]]
            current = ord(w[i])
        else:
            res -= s[w[i]]
    return res

assert calc("EBCDEEDCBA") == 30001
assert calc("DAAABDCA") == 2088


for _ in range(int(input())):
    print(check(input()))