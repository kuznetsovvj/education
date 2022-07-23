# https://codeforces.com/contest/1538/problem/A

import sys


def solution(items):
    s = sum(items)
    l = len(items)
    if s % l != 0:
        return -1
    m = s // l
    res = 0
    for i in items:
        if i > m:
            res += 1
    return res



assert solution(list(map(int, "4 5 2 5".split()))) == 2
assert solution(list(map(int, "0 4".split()))) == 1
assert solution(list(map(int, "10 8 5 1 4".split()))) == -1
assert solution(list(map(int, "10000".split()))) == 0
assert solution(list(map(int, "1 1 1 1 1 1 1".split()))) == 0

"""
input_ = list([tuple(map(int, line.strip().split())) for line in sys.stdin])
for j in range(2, len(input_), 2):
    print(solution(input_[j]))"""

