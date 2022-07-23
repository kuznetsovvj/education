# https://codeforces.com/problemset/problem/69/A

t = int(input())
a, b, c = 0, 0, 0
for tt in range(t):
    x, y, z = map(int, input().split())
    a += x
    b += y
    c += z
if a == 0 and b == 0 and c == 0:
    print("YES")
else:
    print("NO")