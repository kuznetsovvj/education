# https://codeforces.com/problemset/problem/1519/A

def check(a, b, d):
    mn, mx = min(a, b), max(a, b)
    if mn * (1 + d) >= mx:
        return "YES"
    return "NO"
    
for _ in range(int(input())):
    print(check(*map(int, input().split())))