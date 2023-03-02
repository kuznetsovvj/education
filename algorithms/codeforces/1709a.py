# https://codeforces.com/problemset/problem/1709/A

def check(n, seq):
    d1 = seq[n-1]
    if d1 == 0:
        return "NO"
    if seq[d1-1] == 0:
        return "NO"
    return "YES" 

for _ in range(int(input())):
    n = int(input())
    seq = tuple(map(int, input().split()))
    print(check(n, seq))