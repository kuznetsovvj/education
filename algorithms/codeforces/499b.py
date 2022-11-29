# https://codeforces.com/problemset/problem/499/B

import sys


s = tuple(line for line in sys.stdin)
d = {}
for item in s[1:-1]:
    a, b = item.strip().split()
    d[a] = b
r = []
for item in s[-1].split():
    if len(item) <= len(d[item]):
        r.append(item)
    else:
        r.append(d[item])
print(' '.join(r))
