# https://codeforces.com/contest/58/problem/A

a = input()
c = ['h','e','l','l','o']
idx = 0

for i in range(len(a)):
    if idx < len(c) and a[i] == c[idx]:
        idx += 1

if idx == 5:
    print('YES')
else:
    print('NO')