# https://codeforces.com/problemset/problem/337/A

n, m = map(int, input().split())
seq = list(map(int, input().split()))
seq.sort()
mx = float('inf')
for i in range(n-1, m):
    mx = min(mx, seq[i] - seq[i+1-n])
print(mx)