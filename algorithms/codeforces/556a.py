# https://codeforces.com/problemset/problem/556/A


input()
c0, c1 = 0, 0
for i in input():
    if i == '0':
        c0 += 1
    else:
        c1 += 1
print(abs(c1 - c0))