# https://codeforces.com/problemset/problem/268/B

c = int(input())
r = 0
for i in range(1, c):
    r += i * (c - i)
r += c
print(r)