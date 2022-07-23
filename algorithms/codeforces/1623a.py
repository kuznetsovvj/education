# https://codeforces.com/contest/1624/problem/A
# Сложность: 800
# Попыток: 1

import sys


def solution(seq):
    return max(seq) - min(seq)

inp = [tuple(map(int, line.strip().split())) for line in sys.stdin]

for i in range(2, len(inp), 2):
    print(solution(inp[i]))