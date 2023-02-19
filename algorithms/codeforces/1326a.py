# https://codeforces.com/problemset/problem/1326/A

def check(n):
    if n == 1:
        return -1
    if (n - 1) % 3 != 0:
        return "2" * (n - 1) + "3"
    return "2" * (n - 2) + "33"


for _ in range(int(input())):
    print(check(int(input())))