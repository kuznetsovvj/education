# https://codeforces.com/contest/1619/problem/B
# Сложность 800
# Попыток 1

import sys


def solution(n):
    i, s = 1, set()
    sq = 1
    while sq <= n:
        s.add(sq)
        i += 1
        sq = i**2
    i, t = 1, 1
    while t <= n:
        s.add(t)
        i += 1
        t = i**3
    return len(s)


inp = [int(line.strip()) for line in sys.stdin]

for i in range(1, len(inp)):
    print(solution(inp[i]))