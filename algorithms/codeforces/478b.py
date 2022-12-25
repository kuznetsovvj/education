# https://codeforces.com/problemset/problem/478/B

m, n = map(int, input().split())
mx = (m - n + 1) * (m - n) // 2
if m % n == 0:
    mn = (m // n) * (m // n - 1) // 2 * n
else:
    c = m % n
    mn = (m // n) * (m // n - 1) // 2 * (n - c) + (m // n + 1) * (m // n) // 2 * c
print(f"{mn} {mx}")