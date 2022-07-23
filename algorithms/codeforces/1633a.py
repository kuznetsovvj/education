# https://codeforces.com/problemset/problem/1633/A

import sys

# тупой брутфорс
def solution(n):
    if n % 7 == 0:
        return n
    s, d, e = n // 100, n // 10 % 10, n % 10
    for k in range(10):
        if (n - e + k) % 7 == 0:
                return n - e + k
    t = 1
    if n // 10 > 0:
        t = 0
    for k in range(t, 10):
        if (n - d * 10 + k * 10) % 7 == 0:
            return n - d * 10 + k * 10
    for k in range(1, 10):
        if k * 100 + d * 10 + e % 7 == 0:
            return k * 100 + d * 10 + e



inp = [int(line.strip()) for line in sys.stdin]
for i in range(1, len(inp)):
    print(solution(inp[i]))