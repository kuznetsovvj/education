# https://codeforces.com/problemset/problem/1095/A

input()
w = input()
l, d = 0, 1
res = []
while l < len(w):
    res.append(w[l])
    l += d
    d += 1
print(''.join(map(str, res)))