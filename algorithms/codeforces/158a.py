# https://codeforces.com/problemset/problem/158/A

n, k = map(int, input().split())
seq = list(map(int, input().split()))
seq.sort()
t = seq[-k]
s = 0
for item in seq:
    if item >= t and item > 0:
        s += 1
print(s)