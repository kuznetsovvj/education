# https://codeforces.com/problemset/problem/339/B

n, _ = map(int, input().split())
seq = tuple(map(int, input().split()))
s = 0
prev = 1
for i in range(len(seq)):
    if seq[i] >= prev:
        s += seq[i] - prev
    else:
        s += n - prev + seq[i]
    prev = seq[i]
print(s)