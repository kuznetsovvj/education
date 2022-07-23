# https://codeforces.com/problemset/problem/41/A

a, b = input(), input()
if a[::-1] == b:
    print('YES')
else:
    print('NO')