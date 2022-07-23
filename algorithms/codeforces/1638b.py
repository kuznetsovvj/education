# https://codeforces.com/problemset/problem/1638/B

import sys


def solution(seq):
    odd = [item for item in seq if item % 2 == 1]
    even = [item for item in seq if item % 2 == 0]
    if len(odd) > 1:
        for i in range(1, len(odd)):
            if odd[i] < odd[i-1]:
                return 'NO'
    if len(even) > 1:
        for i in range(1, len(even)):
            if even[i] < even[i-1]:
                return 'NO'
    return 'YES'

input_ = [list(map(int, line.strip().split())) for line in sys.stdin]

for i in range(2, len(input_), 2):
    print(solution(input_[i]))