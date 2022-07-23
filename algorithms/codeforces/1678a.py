# https://codeforces.com/problemset/problem/1678/A

from collections import Counter


def sol(seq):
    c = Counter(seq)
    if c[0] > 0:
        return len(seq) - c[0]
    if c.most_common()[0][1] > 1:
        return len(seq)
    return len(seq) + 1

t = int(input())
for tt in range(t):
    input()
    print(sol(tuple(map(int, input().split()))))