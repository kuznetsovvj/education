# https://codeforces.com/contest/1475/problem/A

def sol(x):
    while x % 2 == 0:
        x = x // 2
    if x == 1:
        return "NO"
    return "YES"

t = int(input())
for tt in range(t):
    print(sol(int(input().strip())))
