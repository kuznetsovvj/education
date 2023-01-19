# https://codeforces.com/problemset/problem/1716/A

def check(n):
    if n == 1:
        return 2
    t = n % 3 != 0
    return n // 3 + t

for _ in range(int(input())):
    print(check(int(input())))