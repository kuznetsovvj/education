# https://codeforces.com/problemset/problem/1220/A

from collections import Counter


input()
c = Counter(input())
res = ["1"] * c["n"] + ["0"] * c["z"]
print(" ".join(res))