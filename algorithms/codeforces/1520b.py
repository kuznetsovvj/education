# https://codeforces.com/contest/1520/problem/B

def sol(x):
    t = str(x)
    reg = x // int("1"*len(t))
    return reg + (len(t) - 1) * 9

t = int(input())
for tt in range(t):
    print(sol(int(input().strip())))