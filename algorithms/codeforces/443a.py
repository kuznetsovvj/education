# https://codeforces.com/problemset/problem/443/A

a = input()[1:-1].split(', ')
res = set()
for item in a:
    if item:
        res.add(item)
print(len(res))