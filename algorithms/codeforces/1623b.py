# https://codeforces.com/contest/1624/problem/B
# Сложность: 900
# Попыток: 1

import sys


def solution(a, b, c):
    if 2 * b - c > 0:
        m = (2 * b - c) // a
        if a * m == 2 * b - c:
            return "YES"
    
    m = (a + c) // (2 * b)
    if 2 * b * m == a + c:
        return "YES"
    
    if 2 * b - a > 0:
        m = (2 * b - a) // c
        if c * m == 2 * b - a:
            return "YES"
    
    return "NO"


inp = [tuple(map(int, line.strip().split())) for line in sys.stdin]

for i in range(1, len(inp)):
    print(solution(*inp[i]))