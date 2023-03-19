# https://codeforces.com/contest/1807/A

def check(a, b, c):
    if a + b == c:
        return "+"
    if a - b == c:
        return "-"

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    print(check(a, b, c))