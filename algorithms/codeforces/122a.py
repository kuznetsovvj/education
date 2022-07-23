# https://codeforces.com/problemset/problem/122/A

s = [4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777]
a = int(input())
fl = False

for item in s:
    if a % item == 0:
        fl = True
        break

if fl:
    print('YES')
else:
    print('NO')