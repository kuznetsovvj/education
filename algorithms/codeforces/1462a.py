# https://codeforces.com/problemset/problem/1462/A

def check(a):
    res, i, c = [], 0, True
    while len(res) < len(a):
        res.append(a[i])
        if c:
            i = (i + 1) * (-1)
        else:
            i = (-1) * i
        c = not c
    return res

for _ in range(int(input())):
    input()
    print(' '.join(map(str, check(tuple(map(int, input().split()))))))