# https://codeforces.com/problemset/problem/427/A

input()
s, cnt = 0, 0
seq = tuple(map(int, input().split()))
for it in seq:
    s += it
    if s < 0:
        cnt += 1
        s = 0
print(cnt)