# https://codeforces.com/problemset/problem/228/A

seq = tuple(map(int, input().split()))
print(4 - len(set(seq)))