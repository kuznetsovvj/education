# https://codeforces.com/problemset/problem/732/A

k, r = map(int, input().split())

fl = True
for z in range(1, 10):
    if (k % 10) * z % 10 == r or (k % 10) * z % 10 == 0:
        fl = False
        print(z)
        break
if fl:
    print(10)