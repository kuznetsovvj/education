# https://codeforces.com/problemset/problem/1389/A

def check(l, r):
    if r < 2*l:
        return "-1 -1"
    return f"{l} {2*l}"

for _ in range(int(input())):
    print(check(*map(int, input().split())))