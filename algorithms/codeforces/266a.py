# https://codeforces.com/problemset/problem/266/A

input()
a = input()
prev = a[0]
s = 0
for i in range(1, len(a)):
    if a[i] == prev:
        s += 1
    else:
        prev = a[i]
print(s)