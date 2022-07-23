# https://codeforces.com/contest/1607/problem/B

import sys


def sol(x, n):
    a = {0: {0:lambda x,i:x, 1:lambda x,i:x-i, 2:lambda x,i:x+1, 3:lambda x,i:x+1+i},
         1: {0:lambda x,i:x, 1:lambda x,i:x+i, 2:lambda x,i:x-1, 3:lambda x,i:x-1-i}}
    return a[x % 2][n % 4](x, n)

inp = [tuple(map(int, line.strip().split())) for line in sys.stdin]

for i in range(1, len(inp)):
    print(sol(*inp[i]))