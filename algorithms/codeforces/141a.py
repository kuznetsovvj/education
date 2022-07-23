# https://codeforces.com/problemset/problem/141/A

from collections import defaultdict

d = defaultdict(int)
a = input()
b = input()
c = input()
for i in range(len(a)):
    d[a[i]] += 1
for i in range(len(b)):
    d[b[i]] += 1
for i in range(len(c)):
    d[c[i]] -= 1
fl = True
for v in d.values():
    if v != 0:
        fl = False
        break
if fl:
    print('YES')
else:
    print('NO')