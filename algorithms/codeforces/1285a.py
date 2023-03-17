# https://codeforces.com/problemset/problem/1285/A

from collections import Counter


input()
c = Counter(input())
print(1 + c["L"] + c["R"])