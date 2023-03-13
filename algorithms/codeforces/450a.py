# https://codeforces.com/problemset/problem/450/A

_, m = map(int, input().split())
seq = tuple(map(int, input().split()))

res, res_idx = 0, 0
for idx, item in enumerate(seq):
    t = item // m + (item % m != 0)
    if t >= res:
        res = t
        res_idx = idx + 1
print(res_idx)
