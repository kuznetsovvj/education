# https://codeforces.com/problemset/problem/1680/B

def sol(mat):
    if mat[0][0] == 'R':
        return 'YES'
    up, left = 0, 0
    for i in range(len(mat)):
        if not up:
            t = mat[i].find('R')
            if t != -1:
                up = (i, t)
        t = mat[i].find('R')
        if t != -1:
            if not left:
                left = (i, t)
            else:
                if left[1] > t:
                    left = (i, t)
    
    if left[0] == up[0] and left[1] == up[1]:
        return 'YES'
    return 'NO'


t = int(input())
for tt in range(t):
    seq = []
    x, y = tuple(map(int, input().split()))
    for l in range(x):
        seq.append(input())
    print(sol(seq))