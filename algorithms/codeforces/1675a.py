# https://codeforces.com/contest/1675/problem/A

def sol(a, b, c, x, y):
    if a > x and b > y:
        return "YES"
    x_s = max(x - a, 0)
    y_s = max(y - b, 0)
    if c >= x_s + y_s:
        return "YES"
    return "NO"

t = int(input())
for tt in range(t):
    a, b, c, x, y = map(int, input().strip().split())
    print(sol(a, b, c, x, y))