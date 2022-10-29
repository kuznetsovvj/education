# https://codeforces.com/contest/1741/problem/B

def check(n):
    if n % 2 == 0:
        return list(range(1, n+1))[::-1]
    if n == 3:
        return [-1]
    return [n-1, n] + list(range(1, n-1))

t = int(input())
for _ in range(t):
    n = int(input())
    print(' '.join(map(str, check(n))))