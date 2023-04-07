# https://codeforces.com/problemset/problem/1400/A

def check(n, w):
    return n*w[n-1]

for _ in range(int(input())):
    n = int(input())
    w = input()
    print(check(n, w))