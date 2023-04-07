# https://codeforces.com/contest/1811/problem/B

def check(n, x1, y1, x2, y2):
    return abs(rotate(n, x1, y1) - rotate(n, x2, y2))

def rotate(n, x, y):
    return min([x, y, n+1 - x, n+1 - y])

for _ in range(int(input())):
    print(check(*map(int, input().split())))