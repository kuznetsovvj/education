# https://codeforces.com/problemset/problem/133/A

s = {'H', 'Q', '9'}
a = input()
fl = False
for i in range(len(a)):
    if a[i] in s:
        fl = True
        break
if fl:
    print('YES')
else:
    print('NO')