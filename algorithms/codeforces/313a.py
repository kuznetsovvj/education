# https://codeforces.com/problemset/problem/313/A

a = int(input())
if a >= 0:
    print(a)
else:
    a = str(a)
    a1 = int(a[:-1])
    a2 = int(a[:-2] + a[-1])
    print(max(a1, a2))
