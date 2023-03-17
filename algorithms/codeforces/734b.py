# https://codeforces.com/problemset/problem/734/B

a2, a3, a5, a6 = map(int, input().split())

res = 0
a256 = min(a2, a5, a6)
res = a256 * 256
if a2 - a256 > 0:
    res += min(a2 - a256, a3) * 32
print(res)