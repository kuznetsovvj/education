# https://codeforces.com/problemset/problem/34/B

n, m = map(int, input().split())
seq = list(map(int, input().split()))
seq.sort()
cnt = 0
for k in range(m):
    if seq[k] < 0:
        cnt += (-1)*seq[k]
    else:
        break
print(cnt)
