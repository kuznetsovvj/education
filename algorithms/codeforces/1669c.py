# https://codeforces.com/contest/1669/problem/C

import sys


def solution(seq):
    a, b = set(), set()
    for i in range(len(seq)):
        if i % 2 == 0:
            a.add(seq[i] % 2)
        else:
            b.add(seq[i] % 2)
    if len(a) == 1 and len(b) == 1:
        return "YES"
    return "NO"




inp = [list(map(int, line.strip().split())) for line in sys.stdin]
for i in range(2, len(inp), 2):
    print(solution(inp[i]))