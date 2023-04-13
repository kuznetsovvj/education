# https://codeforces.com/problemset/problem/1335/D

def up(t):
    z = int(t)
    if z != 9:
        return str(z+1)
    return '1'

def check(m):
    z = ((0, 0), (1, 3), (2, 6), (3, 1), (4, 4), (5, 7), (6, 2), (7, 5), (8, 8))
    for x, y in z:
        m[x][y] = up(m[x][y])
    for row in m:
        print(''.join(row))



for _ in range(int(input())):
    m = []
    for _ in range(9):
        m.append(list(input()))
    check(m)
