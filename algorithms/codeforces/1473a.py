# https://codeforces.com/problemset/problem/1473/A

def check(d, seq):
    seq.sort()
    if seq[0] + seq[1] <= d or seq[-1] <= d:
        return "YES"
    return "NO"

for _ in range(int(input())):
    _, d = map(int, input().split())
    seq = list(map(int, input().split()))
    print(check(d, seq))