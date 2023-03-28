# https://codeforces.com/contest/1807/problem/F

def check(n, m, i1, j1, i2, j2, d):
    # приведение к божескому виду
    n = int(n)
    m = int(m)
    i1 = int(i1)
    j1 = int(j1)
    i2 = int(i2)
    j2 = int(j2)
    up = d[0] == 'U'
    left = d[1] == 'L'

    if up:
        up = -1
    else:
        up = 1
    if left:
        left = -1
    else:
        left = 1

    up_st = up
    left_st = left

    ic, jc = i1, j1
    res = 0

    while True:

        if ic == i2 and jc == j2:
            return res
        
        ch = False
        if ic + up == 0:
            ch = True
            up = 1
        elif ic + up == n + 1:
            ch = True
            up = -1
        if jc + left == 0:
            ch = True
            left = 1
        elif jc + left == m + 1:
            ch = True
            left = -1

        res += ch
        ic += up
        jc += left

        if ic == i1 and jc == j1 and (up == up_st or ic == 1 or ic == n) and\
            (left == left_st or jc == 1 or jc == m):
            return -1


for _ in range(int(input())):
    print(check(*input().split()))
