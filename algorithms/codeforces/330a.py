# https://codeforces.com/problemset/problem/330/A
 
def check(mx):
    e_line, e_column = 0, 0
    for line in mx:
        if "S" not in line:
            e_line += 1
    for i in range(len(mx[0])):
        fl = False
        for j in range(len(mx)):
            if mx[j][i] == 'S':
                fl = True
                break
        if not fl:
            e_column += 1
    return e_line * len(mx[0]) + e_column * len(mx) - e_line * e_column
 
 
n, m = map(int, input().split())
mx = []
for _ in range(n):
    mx.append(input())
print(check(mx))