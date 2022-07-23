# https://codeforces.com/problemset/problem/1311/A

def check(a, b):
    if a == b:
        return 0
    if b > a and (b - a) % 2 == 1:
        return 1
    if a > b and (a - b) % 2 == 0:
        return 1
    return 2

t = int(input())
for _ in range(t):
    print(check(*map(int, input().split())))