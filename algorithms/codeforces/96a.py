# https://codeforces.com/problemset/problem/96/A

a = input()
cnt, prev = 1, a[0]
cnt_max = float('-inf')
for i in range(1, len(a)):
    if a[i] == prev:
        cnt += 1
    else:
        cnt_max = max(cnt_max, cnt)
        prev = a[i]
        cnt = 1
cnt_max = max(cnt_max, cnt)
if cnt_max >= 7:
    print("YES")
else:
    print("NO")