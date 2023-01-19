# https://codeforces.com/problemset/problem/1373/B

from collections import Counter


def check(s):
    c = Counter(s)
    t = min(c['1'], c['0'])
    if t % 2 == 1:
        return 'DA'
    return 'NET'

for _ in range(int(input())):
    print(check(input().strip()))