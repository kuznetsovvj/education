# https://codeforces.com/contest/1512/problem/A
# Diff: 800

import sys


def solution(items):
    if items[0] != items[1] and items[1] == items[2]:
        return 1
    for k in range(1, len(items)):
        if items[k] != items[k - 1]:
            return k + 1


assert solution([11, 13, 11, 11]) == 2
assert solution([1, 4, 4, 4, 4]) == 1
assert solution([3, 3, 3, 10, 3, 3, 3]) == 4
assert solution([10, 10, 20]) == 3


input_ = list([tuple(map(int, line.strip().split())) for line in sys.stdin])
for j in range(2, len(input_), 2):
    print(solution(input_[j]))