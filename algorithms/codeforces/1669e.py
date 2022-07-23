# https://codeforces.com/contest/1669/problem/E

import sys
from collections import defaultdict


def solution(seq):
    res = 0
    first = defaultdict(int)
    second = defaultdict(int)
    uniq = defaultdict(int)
    for i in seq:
        res += first[i[0]] - uniq[i]
        res += second[i[1]] - uniq[i]
        first[i[0]] += 1
        second[i[1]] += 1
        uniq[i] += 1
    return res


inp = [line.strip() for line in sys.stdin]
i = 1
while i < len(inp):
    cnt = int(inp[i])
    print(solution(inp[i+1:i+cnt+1]))
    i = i + cnt + 1
