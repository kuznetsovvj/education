# https://codeforces.com/problemset/problem/1478/A

from collections import Counter


def check(seq):
    c = Counter(seq)
    return max(c.values())

for _ in range(int(input())):
    input()
    print(check(tuple(map(int, input().split()))))