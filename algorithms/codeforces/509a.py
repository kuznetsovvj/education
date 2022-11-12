# https://codeforces.com/problemset/problem/509/A

n = int(input())
m = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    m[0][i] = 1
    m[i][0] = 1



for i in range(1, n):
    for k in range(1, n):
        m[i][k] = m[i-1][k] + m[i][k-1]

print(m[n-1][n-1])