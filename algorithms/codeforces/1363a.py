# https://codeforces.com/problemset/problem/1363/A

def check(n, seq):
    even, odd = 0, 0
    for item in seq:
        if item % 2 == 0:
            even += 1
        else:
            odd += 1
    if odd == 0:
        return "NO"
    if odd % 2 == 0 and n == len(seq):
        return "NO"
    if n % 2 == 0 and even == 0:
        return "NO"
    return "YES"


for _ in range(int(input())):
    _, x = map(int, input().split())
    seq = tuple(map( int, input().split()))
    print(check(x, seq))