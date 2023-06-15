# https://codeforces.com/contest/1840/problem/C
 
def check(seq, n, ts):
    crt, res = 0, 0
    for i in seq:
        if i <= ts:
            crt += 1
        else:
            crt = 0
        if crt >= n:
            res += crt + 1 - n
    return res
           
 
for _ in range(int(input())):
    _, n, ts = map(int, input().split())
    seq = tuple(map(int, input().split()))
    print(check(seq, n, ts))