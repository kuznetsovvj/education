# https://codeforces.com/problemset/problem/1366/A

def check(a, b):
    return min(a, b, (a+b) // 3)


for _ in range(int(input())):
    print(check(*map(int, input().split())))
