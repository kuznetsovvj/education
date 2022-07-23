# https://codeforces.com/problemset/problem/1660/C

import sys
from collections import defaultdict

def solution(s):
    u = defaultdict(bool)
    res = 0
    for item in s:
        if u[item]:
            res += 2
            u.clear()
        else:
            u[item] = True
    return len(s) - res


input_ = [line.strip() for line in sys.stdin]
for i in range(1, len(input_)):
    print(solution(input_[i]))