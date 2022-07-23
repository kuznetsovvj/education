#  https://codeforces.com/contest/1551/problem/B1
#  сложность 800

import sys
from collections import Counter


def solution(s):
    d = Counter(s)
    r = 0
    for k, v in d.items():
        r += min(v, 2)
    return r // 2
    

inp = [line.strip() for line in sys.stdin]

for idx in range(1, len(inp)):
    print(solution(inp[idx]))