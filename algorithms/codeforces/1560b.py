#  https://codeforces.com/contest/1560/problem/B
#  сложность 800

import sys


def solution(a, b, c):
    size = abs(b - a) * 2
    if max(a, b, c) > size:
        return -1
    res = c + (size // 2)
    if res > size:
        res = res - size
    return res

inp = [tuple(map(int, line.split(' '))) for line in sys.stdin]

for idx in range(1, len(inp)):
    print(solution(*inp[idx]))


assert solution(6, 2, 4) == 8
assert solution(2, 3, 1) == -1
assert solution(2, 4, 10) == -1
assert solution(5, 3, 4) == -1
assert solution(1, 3, 2) == 4
assert solution(2, 5, 4) == 1
assert solution(4, 3, 2) == -1