# https://codeforces.com/problemset/problem/540/A

input()
a = input().strip()
b = input().strip()
res = 0
for i in range(len(a)):
    k = int(a[i])
    z = int(b[i])
    res += min(abs(k-z), 10 - abs(k-z))
print(res)