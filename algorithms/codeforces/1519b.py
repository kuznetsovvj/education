# https://codeforces.com/problemset/problem/1519/B

def check(x, y, k):
    m = [[0 for _ in range(y)] for _ in range(x)]
    for i in range(x):
        for z in range(y):
            if i == 0 and z == 0:
                continue
            if z == 0:
                m[i][z] = m[i-1][z] + 1
                continue
            m[i][z] = m[i][z-1] + i + 1
    if m[x-1][y-1] == k:
        return "YES"
    else:
        return "NO"
            

for _ in range(int(input())):
    print(check(*map(int, input().split())))