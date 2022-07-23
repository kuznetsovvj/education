# https://codeforces.com/problemset/problem/467/A

t = int(input())
res = 0
for tt in range(t):
    x, y = map(int, input().split())
    if x + 2 <= y:
        res += 1
print(res)