# https://codeforces.com/contest/1618/problem/A
# Сложность 800
# Попыток 1

import sys


def solution(seq):
    seq.sort()
    if seq[2] == seq[1] + seq[0]:
        return f"{seq[0]} {seq[1]} {seq[3]}"
    return f"{seq[0]} {seq[1]} {seq[2]}"


inp = [list(map(int, line.strip().split())) for line in sys.stdin]

for i in range(1, len(inp)):
    print(solution(inp[i]))