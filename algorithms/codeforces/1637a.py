# https://codeforces.com/contest/1637/problem/A

import sys


def solution(seq):
    for i in range(1, len(seq)):
        if seq[i] < seq[i-1]:
            return 'YES'
    return 'NO'


input_ = [list(map(int, line.strip().split())) for line in sys.stdin]

for i in range(2, len(input_), 2):
    print(solution(input_[i]))