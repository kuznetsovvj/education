# https://codeforces.com/problemset/problem/1328/B

import math

def check(n, k):
    # найдем позицию первой "b"
    t = math.ceil(((k*8+1)**0.5 - 1) / 2)
    # позиция t + 1 с конца - это первая b!
    # w[-t-1]
    # найдем позицию второй "b"
    d = t * (t + 1) // 2
    delta = d - k + 1
    # w[-delta] - позиция второй "b"
    res = ['a'] * n
    res[-t-1] = 'b'
    res[-t-1+delta] = 'b'
    return ''.join(res)

for _ in range(int(input())):
    print(check(*map(int, input().split())))