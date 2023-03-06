# https://codeforces.com/problemset/problem/116/A


t = int(input())
s, m = 0, 0
for tt in range(t):
    a, b = map(int, input().split())
    s -= a
    s += b
    m = max(m, s)
print(m)