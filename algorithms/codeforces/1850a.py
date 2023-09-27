# https://codeforces.com/contest/1850/problem/A

def check(seq):
    seq.sort()
    if seq[1] + seq[2] >= 10:
        return "YES"
    return "NO"

for _ in range(int(input())):
    a = list(map(int, input().split()))
    print(check(a))