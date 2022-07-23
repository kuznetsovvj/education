# https://codeforces.com/problemset/problem/71/A

def sol(w):
    if len(w) > 10:
        return f"{w[0]}{len(w)-2}{w[-1]}"
    return w

t = int(input())
for tt in range(t):
    print(sol(input()))