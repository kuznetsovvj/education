# https://codeforces.com/contest/1841/problem/0

def check(n):
    if n <= 4:
        return "Bob"
    return "Alice"

for _ in range(int(input())):
    print(check(int(input())))