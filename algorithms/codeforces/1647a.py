# https://codeforces.com/problemset/problem/1647/A

import sys

def solution(n):
    res, s = [], 0
    next2 = (n % 3 != 1)
    while s < n:
        s += 1 + next2
        res.append(1 + next2)
        next2 = not next2
    return ''.join(map(str, res))


input_ = [int(line.strip()) for line in sys.stdin]
for i in range(1, len(input_)):
    print(solution(input_[i]))