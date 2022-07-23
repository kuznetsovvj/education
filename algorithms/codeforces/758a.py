# https://codeforces.com/problemset/problem/758/A

input()
seq = tuple(map(int, input().split()))
m, s = max(seq), 0
for i in seq:
    s += m - i
print(s)