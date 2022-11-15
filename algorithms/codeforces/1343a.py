# https://codeforces.com/problemset/problem/1343/A

def check(n):
    for i in range(2, 31):
        if n % (2**i - 1) == 0:
            return n // (2**i - 1)

for _ in range(int(input())):
    print(check(int(input())))
