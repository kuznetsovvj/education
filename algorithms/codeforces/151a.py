# https://codeforces.com/problemset/problem/151/A

n, k, l, c, d, p, nl, np = map(int, input().split())
a1 = k * l // nl
a2 = c * d
a3 = p // np
res = min(a1, a2, a3) // n
print(res)