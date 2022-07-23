# https://codeforces.com/problemset/problem/155/A

input()
seq = tuple(map(int, input().split()))
mx, mn = seq[0], seq[0]
cnt = 0
for it in seq:
    if it > mx:
        mx = it
        cnt += 1
        continue
    if it < mn:
        mn = it
        cnt += 1
print(cnt)