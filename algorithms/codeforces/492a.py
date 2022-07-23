# https://codeforces.com/problemset/problem/492/A

n = int(input())
t = 0
s = 1
while n - s >= 0:
    n -= s
    t += 1
    s += (t + 1)
print(t)    