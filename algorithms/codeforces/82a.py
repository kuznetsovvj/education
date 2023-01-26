# https://codeforces.com/problemset/problem/82/A

i = int(input())
z = 0
s = 5

while i > s:
    i -= s
    z += 1
    s = 5 * (2**z)


z = (i - 1) // (2**z)

if z == 0:
    print('Sheldon')
elif z == 1:
    print('Leonard')
elif z == 2:
    print('Penny')
elif z == 3:
    print('Rajesh')
elif z == 4:
    print('Howard')
else:
    print('error')
