# https://codeforces.com/problemset/problem/584/A

n, m = map(int, input().split())
k = ((10**(n-1) // m) + 1) * m
if k >= 10**n:
    print(-1)
else:
    print(k)
