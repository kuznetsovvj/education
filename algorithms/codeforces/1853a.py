# https://codeforces.com/contest/1853/problem/A

def check(seq):
    d = float('inf')
    for i in range(1, len(seq)):
        d = min(d, seq[i] - seq[i-1])
    if d < 0:
        return 0
    return d // 2 + 1

for _ in range(int(input())):
    input()
    seq = tuple(map(int, input().split()))
    print(check(seq))