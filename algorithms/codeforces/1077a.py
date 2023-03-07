# https://codeforces.com/problemset/problem/1077/A

def check(a, b, n):
    if n % 2 == 0:
        return (a - b) * (n // 2)
    return (a - b) * (n // 2) + a

for _ in range(int(input())):
    print(check(*map(int, input().split())))