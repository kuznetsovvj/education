# https://codeforces.com/problemset/problem/1646/C

import sys
import itertools

fac = [87178291200, 6227020800, 479001600, 39916800, 3628800, 362880, 40320, 5040, 720, 120, 24, 6]

def cnt(num):
    return bin(num).count('1')

def solution(num):
    pos = 0
    res = cnt(num)
    if res == 1:
        return 1
    while pos < 12 and num < fac[pos]:
        pos += 1
    if pos == 12:
        return res
    for comb in itertools.product((1, 0), repeat=12 - pos):
        tmp = num
        c = 0
        for idx, item in enumerate(comb):
            if item:
                tmp -= fac[pos + idx]
                c += 1
        if tmp < 0:
            continue
        res = min(res, cnt(tmp) + c)
    
    return res


input_ = [int(line.strip()) for line in sys.stdin]
for pos in range(1, len(input_)):
    print(solution(input_[pos]))

