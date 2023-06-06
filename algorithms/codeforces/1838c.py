# https://codeforces.com/contest/1838/problem/C
 
 
def check(n, m):
    res = [[0 for _ in range(m)] for _ in range(n)]
    t = 1
    for i in range(1, n, 2):
        for j in range(m):
            res[i][j] = t
            t += 1
 
    for i in range(0, n, 2):
        for j in range(m):
            res[i][j] = t
            t += 1
        
    for i in range(n):
        print(" ".join(map(str, res[i])))
 
def check2(n):
    for i in range(2, int(n**0.5) + 2):
        if n % i == 0:
            return False
    return True
 
for _ in range(int(input())):
    n, m = map(int, input().split())
    check(n, m)