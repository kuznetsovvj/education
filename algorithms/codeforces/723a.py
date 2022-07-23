# https://codeforces.com/problemset/problem/723/A

seq = tuple(map(int, input().split()))
r = float('inf')
for i in range(min(seq), max(seq)+1):
    r = min(r, abs(i - seq[0]) + abs(i - seq[1]) + abs(i - seq[2]))
print(r)