# https://codeforces.com/problemset/problem/1154/A

seq = list(map(int, input().split()))
seq.sort()
print(seq[3] - seq[0], seq[3] - seq[1], seq[3] - seq[2])