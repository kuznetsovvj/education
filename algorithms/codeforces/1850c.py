# https://codeforces.com/contest/1850/problem/C

import sys


def check(mx):
    flag = False
    for i in range(8):
        if flag:
            i -= 1
            break
        for j in range(8):
            if mx[i][j] != '.':
                flag = True
                break
    res = []
    while i < 8:
        if mx[i][j] != '.':
            res.append(mx[i][j])
            i += 1
        else:
            break
    return ''.join(res)


inp = [line.strip() for line in sys.stdin]
for i in range(int(inp[0])):
    print(check(inp[8*i + 1: 8 * i + 9]))

