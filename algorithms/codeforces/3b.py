# https://codeforces.com/problemset/problem/3/B

import sys


def solution(n, bd, kt):
    res_s, res = 0, []
    while n:
        # есть место и для катамарана, и для байдарки
        if n >= 2:
            # кончились плавсредства
            if len(bd) == 0 and len(kt) == 0:
                break
            # кончились байдарки
            if len(bd) == 0:
                kts = kt.pop()
                res_s += kts[0]
                res.append(kts[1])
                n -= 2
                continue
            # кончились катамараны
            if len(kt) == 0:
                bds = bd.pop()
                res_s += bds[0]
                res.append(bds[1])
                n -= 1
                continue
            # и байдарки, и катамараны есть
            if n > 2 and n % 2 == 1:
                if bd[-1][0] > (kt[-1][0] / 2):
                    bd1 = bd.pop()
                    res_s += bd1[0]
                    res.append(bd1[1])
                    n -= 1
                else:
                    kts = kt.pop()
                    res_s += kts[0]
                    res.append(kts[1])
                    n -= 2
                continue
            if n >= 2:
                if len(bd) >= 2:
                    if kt[-1][0] > bd[-1][0] + bd[-2][0]:
                        # берем катамаран
                        kts = kt.pop()
                        res_s += kts[0]
                        res.append(kts[1])
                        n -= 2
                    else:
                        # берем две байдарки
                        bd1 = bd.pop()
                        bd2 = bd.pop()
                        res_s += bd1[0] + bd2[0]
                        res.append(bd1[1])
                        res.append(bd2[1])
                        n -= 2
                else:
                    if kt[-1][0] > bd[-1][0]:
                        kts = kt.pop()
                        res_s += kts[0]
                        res.append(kts[1])
                        n -= 2
                    else:
                        bd1 = bd.pop()
                        res_s += bd1[0]
                        res.append(bd1[1])
                        n -= 1
                continue
        # место только для байдарки
        if n == 1:
            if len(bd) > 0:
                bds = bd.pop()
                res_s += bds[0]
                res.append(bds[1])
                
            n -= 1
    print(res_s)
    print(' '.join(map(str, res)))

inp = [tuple(map(int, line.strip().split())) for line in sys.stdin]

_, n = inp[0]
bd, kt = [], []
for i in range(1, len(inp)):
    if inp[i][0] == 1:
        bd.append((inp[i][1], i))
    else:
        kt.append((inp[i][1], i))
bd.sort(key=lambda x:x[0])
kt.sort(key=lambda x:x[0])
solution(n, bd, kt)

