# https://codeforces.com/problemset/problem/115/A


import sys
from collections import defaultdict


inp = tuple(int(line) for line in sys.stdin)
childs = defaultdict(set)

for i in range(1, len(inp)):
    childs[inp[i]].add(i)

lvl = 1
current = childs[-1]
while current:
    nxt = set()
    for i in current:
        nxt.update(childs[i])
    if nxt:
        lvl += 1
        current = nxt
    else:
        break

print(lvl)