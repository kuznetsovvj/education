# https://codeforces.com/problemset/problem/996/A

a = int(input())
res = 0
z = [100, 20, 10, 5, 1]
for k in z:
    res += a // k
    a = a % k
print(res)