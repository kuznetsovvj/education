# https://codeforces.com/problemset/problem/1358/A

def check(x, y):
    return (x * y // 2) + (x * y % 2)

for _ in range(int(input())):
    print(check(*map(int, input().split())))