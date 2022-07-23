# https://codeforces.com/problemset/problem/580/A

input()
seq = tuple(map(int, input().split()))
s, m = 1, 1
for i in range(1, len(seq)):
    if seq[i] >= seq[i-1]:
        s += 1
    else:
        m = max(s, m)
        s = 1
m = max(s, m)
print(m)