# https://codeforces.com/problemset/problem/16/A

def sol(x, y, mat):
    for item in mat:
        for i in range(1, len(item)):
            if item[i] != item[0]:
                return "NO"
    for z in range(1, x):
        if mat[z][0] == mat[z-1][0]:
            return "NO"
    return "YES"


x, y = map(int, input().split())
mat = []
for xx in range(x):
    mat.append(input())
print(sol(x, y, mat))