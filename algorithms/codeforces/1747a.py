# https://codeforces.com/contest/1747/problem/A

def check(seq):
    return abs(sum(seq))

t = int(input())
for _ in range(t):
    input()
    seq = tuple(map(int, input().split()))
    print(check(seq))