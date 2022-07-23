# https://codeforces.com/problemset/problem/1642/B

import sys


def solution(seq):
    cnt = len(set(seq))
    res = []
    for k in range(1, len(seq)+1):
        res.append(max(k, cnt))
    return ' '.join(map(str, res))


input_ = [list(map(int, line.strip().split())) for line in sys.stdin]

for i in range(2, len(input_), 2):
    print(solution(input_[i]))
