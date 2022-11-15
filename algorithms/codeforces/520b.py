# https://codeforces.com/problemset/problem/520/B

n, m = map(int, input().split())

i, res = {n}, 0
while m not in i:
    t = set()
    for it in i:
        if it < m:
            t.add(it*2)
        if it > 1:
            t.add(it-1)
    i = t
    res += 1
print(res)