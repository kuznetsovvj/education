# https://codeforces.com/contest/1547/problem/B

def sol(w):
    s = ord('a') + len(w) - 1
    while s >= ord('a'):
        if chr(s) != w[0] and chr(s) != w[-1]:
            return "NO"
        if chr(s) == w[0]:
            w = w[1:]
        else:
            w = w[:-1]
        s -= 1
    return "YES"


t = int(input())
for tt in range(t):
    print(sol(input().strip()))