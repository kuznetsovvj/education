# https://codeforces.com/problemset/problem/1671/A


def sol(x):
    cnt, prev = 1, x[0]
    for i in range(1, len(x)):
        if x[i] == prev:
            cnt += 1
        else:
            if cnt == 1:
                return "NO"
            cnt, prev = 1, x[i]
    if cnt == 1:
        return "NO"
    return "YES"

t = int(input())
for tt in range(t):
    print(sol(input()))