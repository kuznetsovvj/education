# https://codeforces.com/problemset/problem/1692/C

import sys


def check(mat):
    for idx, line in enumerate(mat):
        for i2, item in enumerate(line):
            if item == '#' and i2 + 2 < len(line) and line[i2 + 2] == '#':
                return f"{idx+2} {i2 + 2}"
                

i = tuple(line.strip() for line in sys.stdin)
k = int(i[0])

for s in range(k):
    print(check(i[s*9 + 2:s*9 + 10]))