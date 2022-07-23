# https://codeforces.com/problemset/problem/1684/A

def sol(n):
    seq = tuple(map(int, list(n)))
    if len(seq) == 2:
        return seq[1]
    return min(seq)

t = int(input())
for tt in range(t):
    print(sol(input()))