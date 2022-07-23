# https://codeforces.com/problemset/problem/707/A

c = {'C', 'M', 'Y'}

x, _ = map(int, input().split())
res = ''
for _ in range(x):
    seq = tuple(input().split())
    for it in seq:
        if it in c:
            res = '#Color'
            break
    if res:
        break
if not res:
    res = '#Black&White'
print(res)