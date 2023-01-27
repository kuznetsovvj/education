# https://codeforces.com/problemset/problem/1541/A

def check(n):
    res = [0 for _ in range(n)]
    for i in range(n):
        if i % 2 == 0:
            res[i] = i + 2
        else:
            res[i] = i
    if n % 2 == 1:
        res[-1] = n-1
        res[-2] = n-2
        res[-3] = n
    return " ".join(map(str, res))

for _ in range(int(input())):
    n = int(input())
    print(check(n))