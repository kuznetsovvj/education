# https://codeforces.com/problemset/problem/231/A

t = int(input())
s = 0
for _ in range(t):
    t = sum(tuple(map(int, input().split())))
    if t >= 2:
        s += 1
print(s)