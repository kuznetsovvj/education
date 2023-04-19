# https://codeforces.com/contest/1811/problem/D
 
def check(n, x, y):
    if n == 1:
        return "YES"
        
    if y > f[n-1] and y <= f[n]:
        return "NO"
    next_x = y
    if y > f[n]:
        next_x = y - f[n]               
        
    return check(n-1, next_x, x)
 
# сгенерим числа Фибоначчи
f = [0]*46
f[0], f[1] = 1, 1
for i in range(2, len(f)):
    f[i] = f[i-1] + f[i-2]
 
for _ in range(int(input())):
    n, x, y = map(int, input().split())
    print(check(n, x, y))