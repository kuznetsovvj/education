#  https://codeforces.com/contest/1560/problem/C
#  сложность 800

import sys
import math


def solution(k):
    r = math.ceil(k**0.5)
    l = ((r-1)**2 + 1 + r**2) // 2
    if k == l:
        return (r, r)
    if k > l:
        row = r
        column = r**2 - k + 1
    else:
        column = r
        row = k - (r-1)**2
    return (row, column)

inp = [int(line) for line in sys.stdin]

for idx in range(1, len(inp)):
    print(' '.join(map(str, solution(inp[idx]))))



assert solution(11) == (2, 4)
assert solution(14) == (4, 3)
assert solution(5) == (1, 3)
assert solution(4) == (2, 1)
assert solution(1) == (1, 1)
assert solution(2) == (1, 2)
assert solution(1000000000) == (31623, 14130)