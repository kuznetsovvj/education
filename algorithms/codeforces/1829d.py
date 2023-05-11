# https://codeforces.com/contest/1829/problem/D

def check(n, m):
    if n == m:
        return "YES"
    t = set()
    t.add(m)
    while t:
        c = set()
        for item in t:
            if item * 3 <= n:
                c.add(item * 3)
            if item % 2 == 0 and (item * 3) // 2 <= n:
                c.add(item * 3 // 2)
        if n in c:
            return "YES"
        t = c
    return "NO"

for _ in range(int(input())):
    print(check(*map(int, input().split())))