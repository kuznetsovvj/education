# https://codeforces.com/problemset/problem/1690/A


def check(n):
    if n % 3 == 0:
        return f"{n // 3} {n // 3 + 1} {n // 3 - 1}"
    if n % 3 == 1:
        return f"{n // 3} {n // 3 + 2} {n // 3 - 1}"
    return f"{n // 3 + 1} {n // 3 + 2} {n // 3 - 1}"

for _ in range(int(input())):
    print(check(int(input())))