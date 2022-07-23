# https://codeforces.com/problemset/problem/1642/A

import sys

def solution(t1, t2, t3):
    if t1[1] == t2[1] and t3[1] < t2[1]:
        return abs(t2[0] - t1[0])
    if t2[1] == t3[1] and t1[1] < t2[1]:
        return abs(t3[0] - t2[0])
    if t1[1] == t3[1] and t2[1] < t1[1]:
        return abs(t3[0] - t1[0])
    return 0


input_ = [list(map(int, line.strip().split())) for line in sys.stdin]

for i in range(1, len(input_), 3):
    print(solution(input_[i], input_[i+1], input_[i+2]))