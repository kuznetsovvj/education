# https://codeforces.com/problemset/problem/1462/C

def check(n):
    t = {i for i in range(1, 10)}
    res = []
    while n != 0:
        if not t:
            return -1
        m = max(t)
        if n < m:
            res.append(n)
            break
        else:
            res.append(m)
            t.remove(m)
            n -= m
    return ''.join(map(str, res[::-1]))


for _ in range(int(input())):
    print(check(int(input())))