# https://codeforces.com/problemset/problem/363/B

_, k = map(int, input().split())
seq = tuple(map(int, input().split()))

s = 0
for i in range(k):
    s += seq[i]
mn, st = s, 0
for z in range(1, len(seq)-k+1):
    s -= seq[z-1]
    s += seq[z+k-1]
    if s < mn:
        mn = s
        st = z
print(st + 1)