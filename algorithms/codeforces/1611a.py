# https://codeforces.com/contest/1611/problem/A

import sys


def solution(x):
    if int(x[-1]) % 2 == 0:
        return 0
    if int(x[0]) % 2 == 0:
        return 1
    for item in x:
        if int(item) % 2 == 0:
            return 2
    return -1

inp = [line.strip() for line in sys.stdin]
for i in range(1, len(inp)):
    print(solution(inp[i]))