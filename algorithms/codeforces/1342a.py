# https://codeforces.com/problemset/problem/1342/A

def check(a, b, x, y):
    if a >= 2*b:
        return b * (x + y)
    else:
        return a * min(x, y) + b * (max(x, y) - min(x, y))

for _ in range(int(input())):
    x, y = map(int, input().split())
    a, b = map(int, input().split())
    print(check(b, a, x, y))