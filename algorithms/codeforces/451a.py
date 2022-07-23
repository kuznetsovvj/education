# https://codeforces.com/problemset/problem/451/A

n, m = map(int, input().split())
if min(n, m) % 2 == 0:
    print('Malvika')
else:
    print('Akshat')