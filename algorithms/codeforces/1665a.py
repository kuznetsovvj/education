# https://codeforces.com/problemset/problem/1665/A

import sys

def sol(x):
    return f'{x-3} {1} {1} {1}'


inp = [int(line.strip()) for line in sys.stdin]

for i in range(1, len(inp)):
    print(sol(inp[i]))