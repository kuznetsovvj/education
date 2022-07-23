# https://codeforces.com/contest/1660/problem/D
# TLE: Переписать на C++?

import sys


def solution(seq):
    tpl = []
    l = -1
    fuz, luz = -1, -1
    for idx, item in enumerate(seq):
        if item == 0:
            if l != -1:
                tpl.append((l, idx - 1)) # добавляем в список проверок отрезок
            if fuz != -1:
                tpl.append((fuz + 1, idx - 1)) # до первого отрицательного
            if luz != -1:
                tpl.append((l, luz - 1)) # до последнего отрицательного
            l, fuz, luz = -1, -1, -1
        else:
            if l == -1:
                l = idx
            if item < 0:
                if fuz == -1:
                    fuz = idx
                luz = idx
    if l != -1:
        tpl.append((l, len(seq) - 1))
    if fuz != -1:
        tpl.append((fuz + 1, len(seq) - 1))
    if luz != -1:
        tpl.append((l, luz - 1))
    
    res = float('-inf')
    max_l, max_r = -1, -1
    for l, r in tpl:
        crt = 1
        for i in range(l, r+1):
            crt *= seq[i]
        if crt > res:
            res = crt
            max_l = l
            max_r = r
    if res < 1:
        return f"{len(seq)} 0"
    
    return f"{max_l} {len(seq) - max_r - 1}"


input_ = [list(map(int, line.strip().split())) for line in sys.stdin]

for i in range(2, len(input_), 2):
    print(solution(input_[i]))
