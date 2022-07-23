# https://codeforces.com/problemset/problem/1646/A

import sys


def solution(n, s):
    t = s - (n + 1) * (n - 1)
    if t <= 0:
        return 0
    if t % (n**2) == 0:
        return t // (n**2)
    else:
        return (t // (n**2)) + 1

input_ = [list(map(int, line.strip().split())) for line in sys.stdin]
for pos in range(1, len(input_)):
    print(solution(*input_[pos]))