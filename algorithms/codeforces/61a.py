# https://codeforces.com/problemset/problem/61/A

a, b = input(), input()
res = [-1 for i in range(len(a))]
for i in range(len(a)):
    if a[i] == b[i]:
        res[i] = 0
    else:
        res[i] = 1
print(''.join(map(str, res)))