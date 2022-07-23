# https://codeforces.com/contest/1669/problem/G

import sys


def solution(seq):
    for item in seq:
        if len(item) == 0:
            continue
        if len(item) == 1:
            return 'NO'
        b, r = 0, 0
        for i in item:
            if i == 'R':
                r += 1
            else:
                b += 1
        if b == 0 or r == 0:
            return 'NO'
    return 'YES'


inp = [line.strip() for line in sys.stdin]
i = 1
while i < len(inp):
    cnt, _ = map(int, inp[i].split())
    print(solution(inp[i+1:i+cnt+1]))
    i = i + cnt + 1