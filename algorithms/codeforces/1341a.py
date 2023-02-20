# https://codeforces.com/problemset/problem/1341/A

def check(n, a, b, c, d):
    if (c - d) > (a + b) * n or (c + d) < (a - b) * n:
        return "No"
    return "Yes"

for _ in range(int(input())):
    print(check(*map(int, input().split())))