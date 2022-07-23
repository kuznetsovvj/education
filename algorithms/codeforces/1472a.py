# https://codeforces.com/problemset/problem/1472/A

def check(w, h, n):
    c = 1
    while w % 2 == 0:
        c *= 2
        w = w // 2
    while h % 2 == 0:
        c *= 2
        h = h // 2
    if c >= n:
        return "YES"
    return "NO"

t = int(input())
for _ in range(t):
    print(check(*map(int, input().split())))
