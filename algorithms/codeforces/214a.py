# https://codeforces.com/problemset/problem/214/A

n, m = map(int, input().split())
res = 0
for i in range(n+1):
    b = n - i**2
    if b >= 0 and b**2 + i == m:
        res += 1
print(res)