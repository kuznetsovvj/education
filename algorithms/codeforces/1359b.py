# https://codeforces.com/problemset/problem/1359/B

def check(x, y, line):
    res = 0
    if 2*x <= y:
        for i in line:
            if i == '.':
                res += x
    else:
        s = 0
        for i in line:
            if i == '.':
                s += 1
                if s == 2:
                    res += y
                    s = 0
            else:
                if s == 1:
                    res += x
                    s = 0
        if s == 1:
            res += x
    return res


for _ in range(int(input())):
    res = 0
    n, m, x, y = map(int, input().split())
    for _ in range(n):
        res += check(x, y, input())
    print(res)

