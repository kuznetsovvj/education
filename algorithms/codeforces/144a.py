# https://codeforces.com/problemset/problem/144/A

input()
seq = tuple(map(int, input().split()))

a = seq.index(max(seq))
b = seq[::-1].index(min(seq))
if a + b >= len(seq):
    res = a + b - 1
else:
    res = a + b

print(res)