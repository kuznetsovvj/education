# https://codeforces.com/problemset/problem/1555/A

def check(n):
    if n <= 6:
        return 15
    return n / 2 * 5

for _ in range(int(input())):
    print(check(int(input())))

