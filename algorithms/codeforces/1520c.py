# https://codeforces.com/contest/1520/problem/C
 
# ходил вокруг и около идеи "шахматной раскраски", но не смог её сформулировать в идею алгоритма
 
def check(n):
    if n == 2:
        print(-1)
        return
    if n == 1:
        print(1)
        return
    tmp = 1
    m = [[0 for _ in range(n)] for _ in range(n)]
    for j in range(n):
        for i in range(n):
            if (j + i) % 2 == 0:
                m[j][i] = tmp
                tmp += 1
    for j in range(n):
        for i in range(n):
            if m[j][i] == 0:
                m[j][i] = tmp
                tmp += 1
    for j in range(n):
        print(' '.join(map(str, m[j])))
 
        
 
for _ in range(int(input())):
    check(int(input()))