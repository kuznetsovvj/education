# https://codeforces.com/problemset/problem/1772/B
 
def check(a, b, c, d):
    if check2(a, b, c, d):
        return "YES"
    if check2(c, a, d, b):
        return "YES"
    if check2(d, c, b, a):
        return "YES"
    if check2(b, d, a, c):
        return "YES"
    return "NO"
 
def check2(a, b, c, d):
    if a < b and a < c and c < d and b < d:
        return 1
    return 0
 
for _ in range(int(input())):
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    print(check(a, b, c, d))