# https://codeforces.com/problemset/problem/1649/B


import sys


def solution(seq):
    s = sum(seq)
    if s == 0:
        return 0
    if max(seq) * 2 <= s:
        return 1
    return max(seq) * 2 - s

input_ = [list(map(int, line.strip().split())) for line in sys.stdin]
for pos in range(2, len(input_), 2):
    print(solution(input_[pos]))