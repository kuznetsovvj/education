# https://codeforces.com/contest/1742/problem/E

import bisect


def check(seq, req):
    res = [seq[0]]
    high = [seq[0]]
    for k in range(1, len(seq)):
        if seq[k] > res[-1]:
            res.append(seq[k])
            high.append(high[-1] + seq[k])
        else:
            high[-1] += seq[k]
    ans = []
    for rq in req:
        r = bisect.bisect_right(res, rq)
        if r == 0:
            ans.append(0)
        else:
            ans.append(high[r-1])
    return ans


t = int(input())
for _ in range(t):
    input()
    seq = tuple(map(int, input().split()))
    req = tuple(map(int, input().split()))
    print(' '.join(map(str, check(seq, req))))