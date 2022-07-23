# https://codeforces.com/problemset/problem/4/B
# Количество попыток: 5
# 2 раза ошибся с форматом вывода, 2 раза - логические ошибки в восстановлении ответа

import sys

def solution(sm, seq):
    c_mn, c_mx = 0, 0
    for (mn, mx) in seq:
        c_mn += mn
        c_mx += mx
    if sm < c_mn or sm > c_mx:
        print("NO")
        return
    print("YES")
    df = sm - c_mn
    res = []
    for item in seq:
        if df > 0:
            if df > (item[1] - item[0]):
                res.append(item[1])
                df -= (item[1] - item[0])
            else:
                res.append(item[0] + df)
                df = 0
        else:
            res.append(item[0])
    print(' '.join(map(str, res)))

inp = [list(map(int, line.strip().split())) for line in sys.stdin]

_, n = inp[0]
solution(n, inp[1:])