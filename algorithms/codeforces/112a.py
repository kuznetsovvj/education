# https://codeforces.com/problemset/problem/112/A

a1, a2 = input().lower(), input().lower()
if a1 == a2:
    print(0)
elif a1 > a2:
    print(1)
else:
    print(-1)