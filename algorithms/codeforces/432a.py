# https://codeforces.com/problemset/problem/432/A

_, k = map(int, input().split())
seq = tuple(map(int, input().split()))
s = 0
for i in seq:
    if i <= 5 - k:
        s += 1
print(s // 3)