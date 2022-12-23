# https://codeforces.com/problemset/problem/149/A


m = int(input())
seq = list(map(int, input().split()))
seq.sort()

cnt = 0
sm = 0
i = len(seq) - 1
while sm < m and i >= 0:
    sm += seq[i]
    i -= 1
    cnt += 1
if sm >= m:
    print(cnt)
else:
    print(-1)