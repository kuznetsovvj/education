# https://codeforces.com/problemset/problem/935/A

t = int(input())
cnt = 0
for i in range(1, t // 2 + 1):
    if (t - i) % i == 0:
        cnt += 1
print(cnt)
