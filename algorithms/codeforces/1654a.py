# https://codeforces.com/problemset/problem/1654/A


import sys

def solution(seq):
    res1, res2 = float('-inf'), float('-inf')
    for item in seq:
        if item > res1:
            res2 = res1
            res1 = item
        else:
            if item > res2:
                res2 = item
    return res1 + res2

input_ = [list(map(int, line.strip().split())) for line in sys.stdin]

for i in range(2, len(input_), 2):
    print(solution(input_[i]))
