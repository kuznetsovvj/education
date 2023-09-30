# https://codeforces.com/contest/1850/problem/F

from collections import defaultdict


# попробовать решение в лоб 
# не прошло по времени на 10-м тесте (увы)
def check(seq):
    t = len(seq)
    d, onecount = defaultdict(int), 0
    for it in seq:
        if it == 1:
            onecount += 1
        else:
            k = it
            while k <= t:
                d[k] += 1
                k += it
    if len(d) == 0:
        return onecount
    return max(d.values()) + onecount


# реализуем осмысленное решение
def check2(seq):
    mx, t = 0, len(seq)
    b, cnt = [0]*(t + 1), [0]*(t + 1)
    for item in seq:
        if item <= t:
            cnt[item] += 1
    
    for x in range(1, t+1):
        y = x
        while y <= t:
            b[y] += cnt[x]
            mx = max(mx, b[y])
            y += x
    return mx

    

for _ in range(int(input())):
    input()
    seq = tuple(map(int, input().split()))
    print(check2(seq))