# https://codeforces.com/problemset/problem/677/A

n, h = map(int, input().split())
seq = tuple(map(int, input().split()))
s = 0
for item in seq:
    s += 1
    if item > h:
        s += 1
print(s)