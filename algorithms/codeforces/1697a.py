# https://codeforces.com/problemset/problem/1697/A
 
def check(n, seq):
    crt, res = n, 0
    for i in seq:
        crt -= i
        if crt < 0:
            res += abs(crt - 0)
            crt = 0
    return res
 
for _ in range(int(input())):
    _, n = map(int, input().split())
    seq = tuple(map(int, input().split()))
    print(check(n, seq))