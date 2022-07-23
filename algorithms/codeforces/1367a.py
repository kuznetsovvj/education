# https://codeforces.com/problemset/problem/1367/A

def check(w):
    return w[0] + w[1:-1:2] + w[-1]

t = int(input())
for _ in range(t):
    print(check(input().strip()))