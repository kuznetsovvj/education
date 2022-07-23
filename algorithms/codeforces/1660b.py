# https://codeforces.com/contest/1660/problem/B

import sys


def solution(seq):
    if len(seq) == 1:
        return seq[0] == 1
    seq.sort(reverse=True)
    return (seq[0] - seq[1] <= 1)


input_ = [list(map(int, line.strip().split())) for line in sys.stdin]

for i in range(2, len(input_), 2):
    if solution(input_[i]):
        print("YES")
    else:
        print("NO")