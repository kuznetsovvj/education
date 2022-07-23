# https://codeforces.com/contest/1593/problem/B

import sys

def sol(n):
    n = n[::-1]
    zero, five = set(), set()
    for idx, it in enumerate(n):
        if it == '0':
            if it in zero:
                return idx - 1
            else:
                zero.add(it)
        if it == '5':
            if it not in five:
                five.add(it)
            if '0' in zero:
                return idx - 1
        if it == '2':
            if '5' in five:
                return idx - 1
        if it == '7':
            if '5' in five:
                return idx - 1


inp = [line.strip() for line in sys.stdin]

for i in range(1, len(inp)):
    print(sol(inp[i]))