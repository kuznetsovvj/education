# https://codeforces.com/problemset/problem/1701/A

def check(a, b, c, d):
    # если все нули
    if a + b + c + d == 0:
        return 0
    if a + b + c + d == 4:
        return 2
    return 1

for _ in range(int(input())):
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    print(check(a, b, c, d))
