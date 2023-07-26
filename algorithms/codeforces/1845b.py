# https://codeforces.com/contest/1845/problem/B

def check(a, b, c):
    res = 0
    if (b[0] - a[0]) * (c[0] - a[0]) > 0:
        res = min(abs(b[0] - a[0]), abs(c[0] - a[0])) + 1
    else:
        res = 0
    if (b[1] - a[1]) * (c[1] - a[1]) > 0:
        if res > 0:
            res += min(abs(b[1] - a[1]), abs(c[1] - a[1]))
        else:
            res += min(abs(b[1] - a[1]), abs(c[1] - a[1])) + 1
    else:
        res += 0
    if not res:
        res = 1
    return res

for _ in range(int(input())):
    a = tuple(map(int, input().split()))
    b = tuple(map(int, input().split()))
    c = tuple(map(int, input().split()))
    print(check(a, b, c))