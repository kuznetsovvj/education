# https://codeforces.com/problemset/problem/1672/A


def sol(seq):
    s = 0
    for item in seq:
        if item != 1:
            s += item - 1
    if s % 2 == 1:
        return "errorgorn"
    return "maomao90"

t = int(input())
for tt in range(t):
    input()
    print(sol(tuple(map(int, input().split()))))