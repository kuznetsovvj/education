# https://codeforces.com/contest/1669/problem/A

import sys


def solution(x):
    if x >= 1900:
        return "Division 1"
    if x >= 1600:
        return "Division 2"
    if x >= 1400:
        return "Division 3"
    return "Division 4"



inp = [int(line.strip()) for line in sys.stdin]
for i in range(1, len(inp)):
    print(solution(inp[i]))