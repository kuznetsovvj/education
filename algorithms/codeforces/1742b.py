# https://codeforces.com/contest/1742/problem/B


def check(seq):
    a = set()
    for item in seq:
        if item in a:
            return "NO"
        a.add(item)
    return "YES"
    
t = int(input())
for _ in range(t):
    input()
    seq = tuple(map(int, input().split()))
    print(check(seq))