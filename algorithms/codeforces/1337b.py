# https://codeforces.com/problemset/problem/1337/B

def check(h, n, m):
    while n and h >= 20:
        h = h // 2 + 10
        n -= 1
    h -= m * 10
    if h > 0:
        return "NO"
    else:
        return "YES"

for _ in range(int(input())):
    print(check(*map(int, input().split())))