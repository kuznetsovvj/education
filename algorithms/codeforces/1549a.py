# https://codeforces.com/problemset/problem/1549/A

def check(n):
    if n == 5:
        return "2 4"
    return f"{2} {(n - 1) // 2}"

for _ in range(int(input())):
    print(check(int(input())))