# https://codeforces.com/contest/1840/problem/D
 
import bisect
 
 
def incheck(seq, m):
    l = bisect.bisect_right(seq, seq[0] + 2*m)
    r = bisect.bisect_left(seq, seq[-1] - 2*m)
    return (r == 0) or (l == len(seq)) or (seq[r-1] - seq[l] <= 2*m)
 
def check(seq):
    seq.sort()
    l, r = 0, (seq[-1] + seq[0] + 2) // 3
    while l < r:
        m = (l + r) // 2
        if incheck(seq, m):
            r = m
        else:
            l = m + 1
    return r
 
 
for _ in range(int(input())):
    input()
    print(check(list(map(int, input().split()))))