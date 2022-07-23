# https://codeforces.com/problemset/problem/1651/B

import sys


def solution(x):
    if x > 19:
        print("NO")
        return
    else:
        print("YES")
        print(' '.join([str(3**x) for x in range(0, x)]))

input_ = [int(line.strip()) for line in sys.stdin]

for i in range(1, len(input_)):
    solution(input_[i])