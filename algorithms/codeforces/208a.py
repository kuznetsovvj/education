# https://codeforces.com/problemset/problem/208/A

a = input().split('WUB')
res = []
for item in a:
    if item:
        res.append(item)
print(' '.join(res))