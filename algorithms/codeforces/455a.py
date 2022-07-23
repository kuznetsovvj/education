# https://codeforces.com/problemset/problem/455/A

# not completed
# жадный алгоритм не работает, надо dp
from collections import defaultdict

d = defaultdict(int)

input()
seq = tuple(map(int, input().split()))

for it in seq:
    d[it] += it

res = 0
while len(d) > 0:
    max_key = max(d, key=d.get)
    res += d[max_key]
    del d[max_key]
    if max_key+1 in d:
        del d[max_key+1]
    if max_key-1 in d:
        del d[max_key-1]

print(res)