# https://codeforces.com/problemset/problem/160/A

input()
seq = list(map(int, input().split()))
seq.sort()
s = sum(seq)
t, cnt = 0, 0
i = len(seq) - 1
while t <= s:
    t += seq[i]
    s -= seq[i]
    i -= 1
    cnt += 1
print(cnt)