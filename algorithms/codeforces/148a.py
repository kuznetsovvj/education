# https://codeforces.com/problemset/problem/148/A

a = int(input())
b = int(input())
c = int(input())
d = int(input())
n = int(input())

s = {i for i in range(1, n+1)}

cnt = 0
z = a
while z <= n:
    if z in s:
        s.remove(z)
        cnt +=1
    z += a

z = b
while z <= n:
    if z in s:
        s.remove(z)
        cnt +=1
    z += b

z = c
while z <= n:
    if z in s:
        s.remove(z)
        cnt +=1
    z += c
    
z = d
while z <= n:
    if z in s:
        s.remove(z)
        cnt +=1
    z += d

print(cnt)