# https://codeforces.com/problemset/problem/1335/B

def check(n, a, b):
    tmp = [chr(x) for x in range(ord('a'), ord('z')+1)]
    tmp = tmp[:b]
    tmp = tmp * (n // b + 1)
    return ''.join(tmp[:n])

for _ in range(int(input())):
    n, a, b = map(int, input().split())
    print(check(n, a, b))