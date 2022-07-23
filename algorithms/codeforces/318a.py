# https://codeforces.com/problemset/problem/318/A

n, k = map(int, input().split())

if n % 2 == 0:
    if k <= (n // 2):
        print(k*2 - 1)
    else:
        print((k - n//2)*2)
else:
    if k <= (n // 2) + 1:
        print(k*2 - 1)
    else:
        print((k - (n // 2) - 1)*2)
