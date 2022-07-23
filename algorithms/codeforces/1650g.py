# https://codeforces.com/problemset/problem/1650/G

import sys


def solution():
    pass


input_ = [list(map(int, line.strip().split())) for line in sys.stdin]
for pos in range(2, len(input_), 3):
    _, n = input_[pos]
    seq = input_[pos + 1]
    print(solution(n, seq))