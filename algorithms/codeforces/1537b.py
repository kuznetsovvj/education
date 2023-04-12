# https://codeforces.com/problemset/problem/1537/B

def check(n, m, i, j):
    res = []
    if n - i > i - 1:
        res.append(n)
    else:
        res.append(1)
    res.append(j)
    res.append(i)
    if m - j > j - 1:
        res.append(j)
    else:
        res.append(1)
    return " ".join(map(str, res))
        

for _ in range(int(input())):
    print(check(*map(int, input().split())))
    