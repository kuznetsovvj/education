# https://codeforces.com/contest/1742/problem/A

def check(seq):
    seq.sort()
    if seq[-1] != seq[0] + seq[1]:
        return "NO"
    return "YES"


t = int(input())
for _ in range(t):
    seq = list(map(int, input().split()))
    print(check(seq))