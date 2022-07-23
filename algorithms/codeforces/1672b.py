# https://codeforces.com/problemset/problem/1672/B

def sol(w):
    ca, cb = 0, 0
    for i in range(len(w)):
        if w[i] == 'A':
            ca += 1
        else:
            cb += 1
        if cb > ca:
            return "NO"
    if cb == 0:
        return "NO"
    if w[-1] == 'A':
        return "NO"
    return "YES"

t = int(input())
for tt in range(t):
    print(sol(input()))