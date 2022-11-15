# https://codeforces.com/problemset/problem/455/A

from collections import defaultdict

d, res = defaultdict(int), defaultdict(int)

input()
seq = tuple(map(int, input().split()))

for it in seq:
    d[it] += it

# это жадное решение, оно не прокатывает
"""res = 0
while len(d) > 0:
    max_key = max(d, key=d.get)
    res += d[max_key]
    del d[max_key]
    if max_key+1 in d:
        del d[max_key+1]
    if max_key-1 in d:
        del d[max_key-1]

print(res)"""

# dp решение
res[0] = 0
res[1] = d[1]
for key in range(max(d.keys())+1):
    if key > 1:
        res[key] = max(res[key-1], res[key-2] + d[key])
       
print(res[max(d.keys())])