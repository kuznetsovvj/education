# https://codeforces.com/problemset/problem/1328/A

t = int(input())
for tt in range(t):
    x, y = map(int, input().split())
    if x % y == 0:
        res = 0
    else:
        res = y - (x % y)
    print(res)