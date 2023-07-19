# https://codeforces.com/contest/1843/problem/C

def check(n):
    s = 0
    while n != 1:
        s += n
        if n % 2 == 0:
            n = n // 2
        else:
            n = (n - 1) // 2
    return s + 1

for _ in range(int(input())):
    print(check(int(input())))