# https://codeforces.com/contest/1619/problem/A
# Сложность 800
# Попыток 1

import sys


def solution(line):
    if len(line) % 2 != 0:
        return "NO"
    if line[:len(line) // 2] != line[len(line) // 2:]:
        return "NO"
    return "YES"

inp = [line.strip() for line in sys.stdin]

for i in range(1, len(inp)):
    print(solution(inp[i]))