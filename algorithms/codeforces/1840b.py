# https://codeforces.com/contest/1840/problem/B

def check(n, k):
    t = bin(k)
    z = len(t) - 3
    if z >= n:
        return 2**n
    b = 0
    if len(t) == 3:
        b = 1
    for idx, j in enumerate(t[3:]):
        if j == '1':
            b = 2**(z-idx)
            break
    return 2**z + b

for _ in range(int(input())):
    print(check(*map(int, input().split())))