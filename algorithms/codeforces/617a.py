# https://codeforces.com/problemset/problem/617/A

a = int(input())
if a % 5 == 0:
    print(a // 5)
else:
    print(a // 5 + 1)