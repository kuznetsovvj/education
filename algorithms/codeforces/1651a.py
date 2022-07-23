# https://codeforces.com/problemset/problem/1651/A

import sys

def solution(n):
    return 2**n - 1


input_ = [int(line) for line in sys.stdin]

for i in range(1, len(input_)):
    print(solution(input_[i]))