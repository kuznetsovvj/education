# https://codeforces.com/problemset/problem/1368/A

def check(a, b, n):
    a, b  = min(a, b), max(a, b)
    res = 0
    while b <= n:
        res += 1
        a, b = b, a + b
    return res

for _ in range(int(input())):
    print(check(*map(int, input().split())))