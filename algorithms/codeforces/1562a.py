# https://codeforces.com/problemset/problem/1562/A
 
def check(l, r):
    b = max(r // 2 + 1, l)
    a = r - b
    return a % b
 
for _ in range(int(input())):
    print(check(*map(int, input().split())))