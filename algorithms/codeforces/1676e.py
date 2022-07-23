from itertools import accumulate
from bisect import bisect_left

def sol(seq, w):
    seq.sort(reverse=True)
    res = list(accumulate(seq))
    for i in w:
        ans = bisect_left(res, i) + 1
        if ans > len(seq):
            print(-1)
        else:
            print(ans)              

t = int(input().strip())
for tt in range(t):
    n, q = map(int, input().split())
    seq = list(map(int, input().split()))
    w = []
    for qq in range(q):
        w.append(int(input()))
    sol(seq, w)
