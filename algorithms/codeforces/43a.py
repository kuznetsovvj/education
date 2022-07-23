# https://codeforces.com/problemset/problem/43/A

from collections import defaultdict


t = int(input())
s = defaultdict(int)
for _ in range(t):
    s[input()] += 1
print(max(s, key=s.get))