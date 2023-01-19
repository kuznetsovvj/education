# https://codeforces.com/problemset/problem/1692/B


def check(n, s):
    if (n - len(s)) % 2 == 0:
        return len(s)
    return len(s) - 1

for _ in range(int(input())):
    n = int(input())
    s = set(map(int, input().split()))
    print(check(n, s))
