# https://codeforces.com/problemset/problem/519/B

from collections import Counter

input()
a = Counter(map(int, input().split()))
b = Counter(map(int, input().split()))
c = Counter(map(int, input().split()))
print((a - b).most_common()[0][0])
print((b - c).most_common()[0][0])