# https://codeforces.com/problemset/problem/486/A

a, t = int(input()), 1
if a % 2 == 1:
    t = -1
print(t*a//2)