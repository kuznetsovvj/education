# https://codeforces.com/problemset/problem/4/C
# Количество попыток: 1
# Сложность 1300

import sys


def solution(names):
    d = {}
    for name in names:
        if name not in d:
            print("OK")
            d[name] = 0
        else:
            d[name] += 1
            print(name + str(d[name]))


inp = [line.strip() for line in sys.stdin]

solution(inp[1:])

